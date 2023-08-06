from enum import IntEnum

NOP_TAG = 0xFF


class TypeCode(IntEnum):
    NIL     = 0
    STRUCT  = 1
    LIST    = 2
    END     = 3
    STRING  = 4
    BOOL    = 5
    U8      = 6
    U16     = 7
    U32     = 8
    U64     = 9
    I8      = 10
    I16     = 11
    I32     = 12
    I64     = 13
    F32     = 14
    F64     = 15


class SizeCode(IntEnum):
    SINGLE  = 0
    SIZE_1  = 1
    SIZE_2  = 2
    SIZE_4  = 3
    SIZE_8  = 4
