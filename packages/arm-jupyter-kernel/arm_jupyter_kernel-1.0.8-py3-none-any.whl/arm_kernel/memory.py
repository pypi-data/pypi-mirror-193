# Memory manages the virtual memory of the kernel emulator.
# 
# There are three main regions of memory:
# - Scratch pad: Where the codeblocks are executed: 500KB
# - Subroutines: Readonly block to store custom subroutines: 1MB
# - Main Memory: Pages of memory according to config.

# Sources:
# - Memory class from bad-address/iasm
# - https://docs.python.org/3/library/stdtypes.html

from collections import namedtuple
from enum import Enum
from struct import pack
from sortedcontainers import SortedList
from unicorn import *
from unicorn.arm_const import *

ALIGNMENT = 4 * 1024

def next_aligned(n: int, alignment: int = ALIGNMENT) -> int:
    return (n + alignment) & -(alignment-1)

STACK_ADDR = 0x0
STACK_SZ = 1024*1024

# Default profile
DEFAULT_BASE = 0x400000
DEFAULT_CODEPAD_MEM_START = DEFAULT_BASE
DEFAULT_CODEPAD_MEM_SZ = 500 * (1 << 10) #500kb
DEFAULT_SUBROUTINE_MEM_START = next_aligned(DEFAULT_CODEPAD_MEM_START + DEFAULT_CODEPAD_MEM_SZ)
DEFAULT_SUBROUTINE_MEM_SZ = 1 << 20 #1Mb
DEFAULT_MAIN_MEM_START = next_aligned(DEFAULT_SUBROUTINE_MEM_START + DEFAULT_SUBROUTINE_MEM_SZ)
DEFAULT_MAIN_MEM_SZ = 4 * (1 << 20) #4Mb
DEFAULT_PAGE_SZ = 1 << 10 #1Kb

DEFAULT_RW_MEM_START = DEFAULT_MAIN_MEM_START
DEFAULT_RW_MEM_SZ = DEFAULT_PAGE_SZ
DEFAULT_RO_MEM_START =  next_aligned(DEFAULT_RW_MEM_START + DEFAULT_RW_MEM_SZ)
DEFAULT_RO_MEM_SZ = DEFAULT_PAGE_SZ

class MemoryType(Enum):
    CODE = 1
    MAIN = 2
    RO = 3
    RW = 4
    SUBROUTINE = 5 
    STACK = 6

class ItemType(Enum):
    BYTE = 1
    HWORD = 2
    WORD = 4
    INT = 10
    STRING = 20
    SPACE = 0

ITEM_BYTE_SZ = {
    ItemType.BYTE: 1,
    ItemType.HWORD: 2,
    ItemType.WORD: 4,
    ItemType.INT: 4,
    ItemType.STRING: 1,
    ItemType.SPACE: 1
}

# Item: Tuple("label", type, access, size, content)
class MemoryItem:

    def __init__(self, label: str, type: ItemType, access: MemoryType, size: int = 1, content = None):
        self.label = label
        self.type = type
        self.access = access
        self.content = content
        self.size = size
        self.byte_size = self.calculate_bytes_count()

    def _type_bytes(self, type: ItemType) -> int:
        return ITEM_BYTE_SZ[type]

    def calculate_bytes_count(self):
        byte_count = self._type_bytes(self.type)

        # Handle strings
        if self.type is ItemType.STRING:
            if isinstance(self.content, list):
                raise ValueError("Only strings must be single, not lists.")
            return len(self.content) + 1 # null terminate
            
        # Handle SPACE
        elif self.type is ItemType.SPACE:
            return self.size * self.byte_count

        # Handle other types
        elif isinstance(self.content, list):
            return max(self.size * byte_count, len(self.content) * byte_count)
        else:
            return byte_count

    # ref: [https://www.geeksforgeeks.org/how-to-convert-int-to-bytes-in-python/]    
    def to_bytes(self):
        bytes_per_val = self._type_bytes(self.type)

        # Handle space
        if self.type is ItemType.SPACE:
            return bytes([0] * bytes_per_val * self.size)
        # Handle strings
        elif self.type is ItemType.STRING:
            if isinstance(self.content, list):
                raise ValueError("Only single strings are supported.")
            return bytes(self.content, 'ascii') + b'\x00'

        # Handle list
        if isinstance(self.content, list):
            byte_ls = []
            for val in self.content:
                words = val.to_bytes(bytes_per_val, 'little')
                for byte in words:
                    byte_ls.append(byte)
            return bytes(byte_ls)
        else:
            return self.content.to_bytes(bytes_per_val, 'little')
    
    def initialize(self, init):
        for i in init:
            if i['type'] == 'memory_i32':
                # %s replaced with number of integers expected                
                # # < means little-endian                
                data = pack('<%si' % len(i['data']), *i['data'])
                # assumes address in JSON is in hexadecimal string form                
                self._mu.mem_write(int(i['address'], 16), data)
            elif i['type'] == 'memory_i8':
                # %s replaced with number of integers expected                
                # < means little-endian                
                data = pack('<%sb' % len(i['data']), *i['data'])
                # assumes address in JSON is in hexadecimal string form                s
                self._mu.mem_write(int(i['address'], 16), data)
            elif i['type'] == 'memory_string':
                # %s replaced with number of integers expected                
                # < means little-endian               
                data = bytes(i['string'], 'ascii') + b'\x00'                
                # assumes address in JSON is in hexadecimal string form                
                self._mu.mem_write(int(i['address'], 16), data)


class MemoryPage:

    def __init__(self, type: MemoryType, start: int, capacity: int):
        self.type = type
        self.start = start
        self.capacity = capacity
        self.size = 0
        self.next_address = start
        self.labels = []
        self.is_full = False

    def __repr__(self) -> str:
        return f"""
        Memory Page @ 0x{self.start:x}:
        Type: {self.type},
        Capacity: {self.capacity} B,
        Size: {self.size} B,
        Next Addrs: 0x{self.next_address:x},
        Full: {self.is_full}
        Labels: {len(self.labels)}
        """

    def add_item(self, mu: unicorn.Uc, item: MemoryItem):
        mu.mem_write(self.next_address, item.to_bytes())
        self.labels.append((item.label, self.next_address))
        
        self.next_address = next_aligned(self.next_address + item.byte_size, 4)
        if self.next_address >= self.start + self.capacity:
            self.is_full = True
        self.size = min(self.capacity, self.next_address - self.start)
        
class Memory:
    def __init__(self, mu: unicorn.Uc):
        self._mu = mu

        # Setup main memory regions map
        self._mem_regions = {
            MemoryType.STACK: (STACK_ADDR, STACK_ADDR + STACK_SZ - 1),
            MemoryType.CODE: (DEFAULT_CODEPAD_MEM_START, DEFAULT_CODEPAD_MEM_START + DEFAULT_CODEPAD_MEM_SZ - 1), 
            MemoryType.SUBROUTINE: (DEFAULT_SUBROUTINE_MEM_START, DEFAULT_SUBROUTINE_MEM_START + DEFAULT_SUBROUTINE_MEM_SZ - 1),
            MemoryType.MAIN: (DEFAULT_MAIN_MEM_START, DEFAULT_MAIN_MEM_START +  DEFAULT_MAIN_MEM_SZ - 1)
        }

        self._mu.mem_map(address=DEFAULT_CODEPAD_MEM_START, size=DEFAULT_CODEPAD_MEM_SZ, perms=UC_PROT_EXEC | UC_PROT_READ)
        self._memset(self._mem_regions[MemoryType.CODE])
        self._mu.mem_map(address=DEFAULT_SUBROUTINE_MEM_START, size=DEFAULT_SUBROUTINE_MEM_SZ, perms=UC_PROT_EXEC | UC_PROT_READ)
        self._memset(self._mem_regions[MemoryType.SUBROUTINE])
        # Configure stack
        self._mu.mem_map(address=STACK_ADDR, size=STACK_SZ)
        self._memset(self._mem_regions[MemoryType.STACK])
        self._mu.reg_write(UC_ARM_REG_SP, STACK_ADDR + STACK_SZ)
        self._mu.reg_write(UC_ARM_REG_FP, STACK_ADDR + STACK_SZ)

        # Setup pages map
        self._rw_pages = SortedList(iterable=[
            MemoryPage(MemoryType.RW, DEFAULT_RW_MEM_START, DEFAULT_RW_MEM_SZ)
        ], key=lambda x: x.start)

        self._ro_pages = SortedList(iterable=[
            MemoryPage(MemoryType.RO, DEFAULT_RO_MEM_START, DEFAULT_RO_MEM_SZ)
        ], key=lambda x: x.start)

        self._mu.mem_map(DEFAULT_RW_MEM_START, DEFAULT_RW_MEM_SZ)
        self._memset((DEFAULT_RW_MEM_START, DEFAULT_RW_MEM_START + DEFAULT_RW_MEM_SZ - 1))
        self._mu.mem_map(DEFAULT_RO_MEM_START, DEFAULT_RO_MEM_SZ, perms=UC_PROT_READ)
        self._memset((DEFAULT_RO_MEM_START, DEFAULT_RO_MEM_START + DEFAULT_RO_MEM_SZ - 1))

        self._items = {}

    @property
    def codepad_address(self) -> int:
        return self._mem_regions[MemoryType.CODE][0]

    @property
    def stack_region(self) -> tuple[int, int]:
        return self._mem_regions[MemoryType.STACK]

    # ref: mem.py in https://book-of-gehn.github.io/articles/2021/01/09/Interactive-Assembler.html
    def _memset(self, region: tuple[int, int], val: int = 0):
        step = 0x2000  # 8k
        if val:
            data = bytes([val]) * step
        else:
            data = bytes(step)  # null initialized
        for addr in range(region[0], region[1] + 1, step):
            if addr + step > region[1] + 1:
                data = data[:region[1] - addr + 1]
            self._mu.mem_write(addr, data)

    def _find_page(self, access: MemoryType, size: int) -> MemoryPage:
        # Find memory list
        list = SortedList()
        if access is MemoryType.RO:
            list = self._ro_pages
        else:
            list = self._rw_pages
        
        for page in list:
            if page.capacity - page.size >= size:
                return page
        
        #TODO: Create new page if no page found
        raise Exception("No page found") # this will be substituted by the creation of a new page

    def write_code(self, code: bytes):
        address = self._mem_regions[MemoryType.CODE][0]
        self._mu.mem_write(address, code)  

    def add_item(self, item: MemoryItem):
        #TODO: Validate item.

        # get page with space
        page = self._find_page(item.access, item.byte_size)

        # Add content to memory
        addrs = page.next_address
        try:
            page.add_item(self._mu, item)
        except Exception as error:
            raise Exception(f"Error writing content to memory: {str(error)}")
        else:
            self._items[item.label] = (addrs, item.byte_size)
    
    def read_item(self, label: str) -> bytearray:
        item = self._items[label]
        print(item)
        content = self._mu.mem_read(item[0], item[1])
        return content

    def find_item(self, label: str) -> tuple[int, int] | None:
        return self._items.get(label)

    def read_address(self, address: int, size: int = 4) -> bytearray:
        try:
            return self._mu.mem_read(address, size)
        except Exception as e:
            raise Exception("Error reading from memory: %s" % str(e))



