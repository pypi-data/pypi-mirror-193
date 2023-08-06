# Parse the canonical test vectors

import unittest
from dataclasses import dataclass
import numpy as np

import ltvpy


class TestRoundTripping(unittest.TestCase):

    def test_dict(self):
        d1 = {
            "null": None,
            "postitive_int": 5,
            "negative_int": -128,
            "max_int64":   9223372036854775807,
            "min_int64": -9223372036854775808,
            "max_uint64": 18446744073709551615,
            "bool_true": True,
            "bool_false": False,
            "a_list": [1, 2, 3],
            "nested_object": { 
                "subthing": "string"
            },
            "float": 1234.4567,
            "binary_data": (1024).to_bytes(4, byteorder='little'),
        }

        bin = ltvpy.dumpb(d1)
        d2 = ltvpy.loadb(bin)

        self.assertDictEqual(d1, d2)

    def test_dataclass(self):
        @dataclass
        class AClass:
            strdata: str
            fdata: float
            int_data: int = 77

        d1 = AClass("ThatClass", 99.9)
        bin = ltvpy.dumpb(d1)
        d2 = ltvpy.loadb(bin)

        self.assertEqual(d1.strdata, d2['strdata'])
        self.assertEqual(d1.fdata, d2['fdata'])
        self.assertEqual(d1.int_data, d2['int_data'])


    def test_numpy_vectors(self):
        d1 = {
            "u8": np.ones(20, dtype="uint8"),
            "u16": np.ones(20, dtype="uint16"),
            "u32": np.ones(20, dtype="uint32"),
            "u64": np.ones(20, dtype="uint64"),
            "i8": np.ones(20, dtype="int8"),
            "i16": np.ones(20, dtype="int16"),
            "i32": np.ones(20, dtype="int32"),
            "i64": np.ones(20, dtype="int64"),
            "f32": np.ones(20, dtype="float32"),
            "f64": np.ones(20, dtype="float64"),
        }

        bin = ltvpy.dumpb(d1)
        d2 = ltvpy.loadb(bin)

        # Note: a numpy array of u8 round trips to the 'bytes' type.
        self.assertEqual(d1["u8"].tobytes(), d2['u8'])

        self.assertTrue(np.array_equal(d1["u16"], d2['u16']))
        self.assertTrue(np.array_equal(d1["u32"], d2['u32']))
        self.assertTrue(np.array_equal(d1["u64"], d2['u64']))

        self.assertTrue(np.array_equal(d1["i8"], d2['i8']))
        self.assertTrue(np.array_equal(d1["i16"], d2['i16']))
        self.assertTrue(np.array_equal(d1["i32"], d2['i32']))
        self.assertTrue(np.array_equal(d1["i64"], d2['i64']))

        self.assertTrue(np.array_equal(d1["f32"], d2['f32']))
        self.assertTrue(np.array_equal(d1["f64"], d2['f64']))


if __name__ == '__main__':
    unittest.main()
