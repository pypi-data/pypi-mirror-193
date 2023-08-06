"""Various shared functions and constants"""
import math

UINT_BYTE_SIZES = {1: 'B',
                   2: 'H',
                   4: 'I',
                   8: 'Q'}
INT_BYTE_SIZES = {1: 'b',
                  2: 'h',
                  4: 'i',
                  8: 'q'}


def unpack_uint_format(bitwidth):
    """Return the unpack format qualifier and expected byte size
       for unsigned ints of this bitwidth"""
    assert 1 <= bitwidth <= 32
    bytewidth = math.ceil(bitwidth/8.)
    while bytewidth not in UINT_BYTE_SIZES:
        bytewidth += 1
    return UINT_BYTE_SIZES[bytewidth], bytewidth


def unpack_int_format(bitwidth):
    """Return the unpack format qualifier and expected byte size
       for signed ints of this bitwidth"""
    assert 1 <= bitwidth <= 32
    bytewidth = math.ceil(bitwidth/8.)
    while bytewidth not in INT_BYTE_SIZES:
        bytewidth += 1
    return INT_BYTE_SIZES[bytewidth], bytewidth


class Error(RuntimeError):
    """Base error for all pyscos2000 errors"""
