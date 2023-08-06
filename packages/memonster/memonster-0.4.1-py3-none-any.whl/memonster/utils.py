import struct
import ctypes

def is_power_of_two(n: int) -> bool:
    return n != 0 and (n & (n-1) == 0)

def py_to_pointer(x) -> int:
    return struct.unpack("P", ctypes.pointer(x))[0]
