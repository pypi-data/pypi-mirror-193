import io
import struct
import numpy as np

from .protocol import TypeCode, SizeCode, NOP_TAG

_BUFFER_LENGTHS = [0, 1, 2, 4, 8]

_INT_CODES = {
    TypeCode.U8:  (1, False),
    TypeCode.U16: (2, False),
    TypeCode.U32: (4, False),
    TypeCode.U64: (8, False),
    TypeCode.I8:   (1, True),
    TypeCode.I16:  (2, True),
    TypeCode.I32:  (4, True),
    TypeCode.I64:  (8, True),
}

_NP_TAG_DTYPES = {
    TypeCode.BOOL: np.dtype(bool),
    TypeCode.I8: np.dtype(np.int8),
    TypeCode.U8: np.dtype(np.uint8),
    TypeCode.I16: np.dtype(np.int16),
    TypeCode.U16: np.dtype(np.uint16),
    TypeCode.I32: np.dtype(np.int32),
    TypeCode.U32: np.dtype(np.uint32),
    TypeCode.I64: np.dtype(np.int64),
    TypeCode.U64: np.dtype(np.uint64),
    TypeCode.F32: np.dtype(np.float32),
    TypeCode.F64: np.dtype(np.float64),
}


def decode_tag(tag: int) -> [TypeCode, SizeCode]:
    return [(tag & 0xF0) >> 4,  (tag & 0x0F)]


class LiteVectorDecoder:

    def __init__(self, r: io.RawIOBase) -> None:
        self.r = r

    def read_bytes(self, size: int) -> bytes:
        b = self.r.read(size)
        if b is None or len(b) != size:
            raise EOFError
        return b

    def read_int(self, size: int, signed=False) -> int:
        return int.from_bytes(self.read_bytes(size), "little", signed=signed)

    def read_tag(self):
        tag = NOP_TAG
        while tag == NOP_TAG:
            b = self.r.read(1)
            if b is None or len(b) == 0:
                return None
            tag = int.from_bytes(b, "little", signed=False)
        return tag

    def read_buffer(self, tag: int) -> bytes:
        size_code = (tag & 0x0F)
        if size_code == SizeCode.SINGLE or size_code > SizeCode.SIZE_8:
            raise ValueError("Invalid vector size code", size_code)

        len_size = _BUFFER_LENGTHS[size_code]
        buf_len = self.read_int(len_size)
        return self.read_bytes(buf_len)

    def decode_string(self, tag: int) -> str:
        """ Streamlined 'decode_one' that verifies we got a string """
        type_code, size_code = decode_tag(tag)

        if type_code != TypeCode.STRING:
            raise(ValueError("Expected string key while decoding"))

        if size_code == SizeCode.SINGLE:
            return str(self.read_bytes(1))
        else:
            return self.read_buffer(tag).decode('utf-8', errors='strict')

    def decode_one(self, tag: int):
        type_code, size_code = decode_tag(tag)

        if size_code == 0:
            # Standalone values

            # None
            if type_code == TypeCode.NIL:
                return None

            # One byte string
            elif type_code == TypeCode.STRING:
                return self.decode_string(tag)

            # Bool
            elif type_code == TypeCode.BOOL:
                return struct.unpack("?", self.read_bytes(1))[0]

            # Map
            elif type_code == TypeCode.STRUCT:
                s = {}
                tag = self.read_tag()
                type_code, size_code = decode_tag(tag)
                while type_code != TypeCode.END:
                    key = self.decode_string(tag)
                    val = self.decode_one(self.read_tag())
                    s[key] = val
                    tag = self.read_tag()
                    type_code, size_code = decode_tag(tag)
                return s

            # List
            elif type_code == TypeCode.LIST:
                v = []
                tag = self.read_tag()
                type_code, size_code = decode_tag(tag)
                while type_code != TypeCode.END:
                    v.append(self.decode_one(tag))
                    tag = self.read_tag()
                    type_code, size_code = decode_tag(tag)
                return v

            # Int
            elif TypeCode.U8 <= type_code <= TypeCode.I64:
                (length, signed) = _INT_CODES[type_code]
                return self.read_int(length, signed)

            # Float
            elif type_code == TypeCode.F32:
                return struct.unpack("<f", self.read_bytes(4))[0]

            elif type_code == TypeCode.F64:
                return struct.unpack("<d", self.read_bytes(8))[0]

        else:
            # Vectors

            # String
            if type_code == TypeCode.STRING:
                return self.read_buffer(tag).decode('utf-8', errors='strict')

            # Bytes
            elif type_code == TypeCode.U8:
                return self.read_buffer(tag)
            
            # Numeric arrays
            elif type_code >= TypeCode.BOOL:
                len_size = _BUFFER_LENGTHS[size_code]
                buf_len = self.read_int(len_size)
                buf = self.read_bytes(buf_len)
                return np.frombuffer(buf, dtype=_NP_TAG_DTYPES[type_code])
            
        raise ValueError(f'Unknown LiteVector type_code: {type_code}, size_code: {size_code}')

    def read_one(self):
        """ Read one element from the stream """
        tag = self.read_tag()
        if tag is None:
            return None
        return self.decode_one(tag)

    def decode(self):
        v = []
        while True:
            tag = self.read_tag()
            if tag is None:
                break
            v.append(self.decode_one(tag))
        if len(v) == 0:
            return None
        elif len(v) == 1:
            return v[0]
        return v
