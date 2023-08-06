import io
import struct

import numpy
import numpy.ma

from .protocol import TypeCode, SizeCode

_MIN_INT8   = -128
_MAX_INT8   = 127
_MIN_INT16  = -32768
_MAX_INT16  = 32767
_MIN_INT32  = -2147483648
_MAX_INT32  = 2147483647
_MIN_INT64  = -9223372036854775808
_MAX_INT64  = 9223372036854775807

_MAX_UINT8  = 255
_MAX_UINT16 = 65535
_MAX_UINT32 = 4294967295
_MAX_UINT64 = 18446744073709551615

_NUMPY_TYPES = [
    [numpy.int8, TypeCode.I8, "int8"],
    [numpy.uint8, TypeCode.U8, "uint8"],
    [numpy.int16, TypeCode.I16, "int16"],
    [numpy.uint16, TypeCode.U16, "uint16"],
    [numpy.int32, TypeCode.I32, "int32"],
    [numpy.uint32, TypeCode.U32, "uint32"],
    [numpy.int64, TypeCode.I64, "int64"],
    [numpy.uint64, TypeCode.U64, "uint64"],
    [numpy.float16, None, "float16"],
    [numpy.float32, TypeCode.F32, "float32"],
    [numpy.float64, TypeCode.F64, "float64"],
]


def _compute_length_code(length: int):
    if length <= _MAX_UINT8:
        return SizeCode.SIZE_1, 1
    elif length <= _MAX_UINT16:
        return SizeCode.SIZE_2, 2
    elif length <= _MAX_UINT32:
        return SizeCode.SIZE_4, 4
    else:
        return SizeCode.SIZE_8, 8


def bt(val: int) -> bytes:
    return val.to_bytes(1, byteorder='little')


def is_simple_array(a: numpy.ndarray) -> bool:
    """ Check whether an ndarray is simple 1-D or advanced. """
    if a.ndim > 1:
        return False

    if isinstance(a, numpy.ma.masked_array):
        return False

    if a.dtype == numpy.float16:
        return False

    return True


def find_numpy_descriptor(a: numpy.ndarray):
    for d in _NUMPY_TYPES:
        if d[0] == a.dtype:
            return d
    return None


class LiteVectorEncoder:

    def __init__(self, w: io.BufferedWriter) -> None:
        self.w = w

    def write_vector(self, type_code: TypeCode, buf: bytes):
        buf_size = len(buf)
        if buf_size > _MAX_UINT64:
            raise(ValueError("buffer size larger than maximum"))

        size_code, len_size = _compute_length_code(buf_size)

        self.write_tag(type_code, size_code)
        self.w.write(int.to_bytes(buf_size, length=len_size, byteorder='little', signed=False))
        self.w.write(buf)

    def write_tag(self, type_code: TypeCode, size_code: SizeCode = SizeCode.SINGLE) -> None:
        self.w.write(bt(type_code << 4 | size_code))

    def write_string(self, s: str) -> None:
        self.write_vector(TypeCode.STRING, s.encode('utf-8', errors='strict'))

    def write_numpy_array(self, a: numpy.ndarray):
        v = a.newbyteorder('<')

        dt = find_numpy_descriptor(v)
        if dt is None:
            raise(ValueError("Unsupported numpy data type:", a.dtype))

        if is_simple_array(v):
            self.write_vector(dt[1], v.tobytes())
            return

        raise TypeError(f'unsuppported numpy array of type {a.__class__.__name__} '
                        f'is not LiteVector serializable')

        # TODO: Advanced array protocol

        # # Check for mask
        # mask = None
        # if isinstance(v, numpy.ma.masked_array):
        #     mask = numpy.ma.getmaskarray(v)
        #     v = v.data

        # self.write_tag(TypeCode.STRUCT)
        # self.write_key_value("dtype", dt[2])
        # self.write_key_value("shape", v.shape)

        # self.write_string("data")
        # if dt[1] is not None:
        #     self.write_vector(dt[1], v.tobytes())
        # else:
        #     self.write_vector(TypeCode.U8, v.tobytes())

        # if mask is not None:
        #     self.write_string("mask")
        #     self.write_vector(TypeCode.BOOL, mask.tobytes())

        # self.write_tag(TypeCode.END)
        
    def write_key_value(self, key: str, val):
        self.write_string(key)
        self.encode(val)

    def try_encode_object(self, value) -> bool:
        """" Try to encode value as an object. Returns True if successful """
        # Objects implementing '__dict__' as struct
        try:
            if value.__dict__ is not None:
                self.write_tag(TypeCode.STRUCT)
                for key, val in value.__dict__.items():
                    self.write_key_value(key, val)
                self.write_tag(TypeCode.END)
                return True
        except AttributeError:
            return False
        return False

    def encode(self, value):
    
        # Nil
        if value is None:
            self.write_tag(TypeCode.NIL)

        # Bool
        elif isinstance(value, bool):
            self.write_tag(TypeCode.BOOL)
            if value is True:
                self.w.write(bt(1))
            else:
                self.w.write(bt(0))

        # Int
        elif isinstance(value, int):
            # Python has arbitrarily sized integers - check that we can accommodate this one.
            if value < _MIN_INT64 or value > _MAX_UINT64:
                raise(ValueError("integer out of range: " + str(value)))

            # Goldilocks the number into the smallest storage class that will hold it.
            if value >= 0:
                # Positive integer
                if value <= _MAX_UINT8:
                    self.write_tag(TypeCode.U8)
                    self.w.write(int.to_bytes(value, length=1, byteorder='little', signed=False))
                elif value <= _MAX_UINT16:
                    self.write_tag(TypeCode.U16)
                    self.w.write(int.to_bytes(value, length=2, byteorder='little', signed=False))
                elif value <= _MAX_UINT32:
                    self.write_tag(TypeCode.U32)
                    self.w.write(int.to_bytes(value, length=4, byteorder='little', signed=False))
                else:
                    self.write_tag(TypeCode.U64)
                    self.w.write(int.to_bytes(value, length=8, byteorder='little', signed=False))
            else:
                # Negative integer
                if value >= _MIN_INT8:
                    self.write_tag(TypeCode.I8)
                    self.w.write(int.to_bytes(value, length=1, byteorder='little', signed=True))
                elif value >= _MIN_INT16:
                    self.write_tag(TypeCode.I16)
                    self.w.write(int.to_bytes(value, length=2, byteorder='little', signed=True))
                elif value >= _MIN_INT32:
                    self.write_tag(TypeCode.I32)
                    self.w.write(int.to_bytes(value, length=4, byteorder='little', signed=True))
                else:
                    self.write_tag(TypeCode.I64)
                    self.w.write(int.to_bytes(value, length=8, byteorder='little', signed=True))

        # Float
        elif isinstance(value, float):
            self.write_tag(TypeCode.F64)
            self.w.write(struct.pack("<d", value))

        # Dict
        elif isinstance(value, dict):
            self.write_tag(TypeCode.STRUCT)
            for key, val in value.items():
                self.write_key_value(key, val)
            self.write_tag(TypeCode.END)

        # List
        elif isinstance(value, (list, tuple)):
            self.write_tag(TypeCode.LIST)
            for v in value:
                self.encode(v)
            self.write_tag(TypeCode.END)

        # Byte Array
        elif isinstance(value, (bytes, bytearray)):
            self.write_vector(TypeCode.U8, value)

        # String
        elif isinstance(value, str):
            self.write_string(value)
        
        # Numpy arrays
        elif isinstance(value, numpy.ndarray):
            self.write_numpy_array(value)
        
        # Object
        elif self.try_encode_object(value):
            pass
        else:
            raise(ValueError("Unsupported data type", type(value)))
