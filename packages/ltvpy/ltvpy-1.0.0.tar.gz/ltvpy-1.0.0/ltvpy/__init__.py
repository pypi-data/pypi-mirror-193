__version__ = '1.0.0'

import io

from .encode import LiteVectorEncoder
from .decode import LiteVectorDecoder


def dump(value, w: io.BufferedWriter) -> None:
    """ Dump a value to a litebuffer writer """
    cls = LiteVectorEncoder(w)
    return cls.encode(value)


def dumpb(value) -> bytes:
    """ Dump a value to a litebuffer bytes array """
    w = io.BytesIO()
    dump(value, w)
    return w.getvalue()


def load(r: io.BufferedReader):
    """ Load litebuffer from a BufferedReader """
    cls = LiteVectorDecoder(r)
    return cls.decode()


def loadb(b: bytes):
    """ Load litebuffer from a bytes array """
    return load(io.BytesIO(b))
