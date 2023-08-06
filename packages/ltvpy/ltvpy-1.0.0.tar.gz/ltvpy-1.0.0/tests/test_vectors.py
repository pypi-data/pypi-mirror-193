# Parse the canonical test vectors

import unittest
import os
import ltvpy


POSITIVE_VECTORS = os.path.join(os.path.dirname(os.path.realpath(__file__)), "litevectors_positive.txt")
NEGATIVE_VECTORS = os.path.join(os.path.dirname(os.path.realpath(__file__)), "litevectors_negative.txt")


class TestVectors(unittest.TestCase):
    def process_vectors(self, fileName: str, positive: bool):
        with open(fileName) as fin:
            while True:
                desc = fin.readline().strip()
                data = fin.readline()
                if not desc:
                    break
                with self.subTest(msg=desc):
                    if positive:
                        # Positive vectors should load without problem
                        ltvpy.loadb(bytes.fromhex(data))
                    else:
                        # Negative vectors should raise an exception
                        with self.assertRaises(Exception):
                            ltvpy.loadb(bytes.fromhex(data))

    def test_positive_vector(self):
        self.process_vectors(POSITIVE_VECTORS, True)

    def test_negative_vectors(self):
        self.process_vectors(NEGATIVE_VECTORS, False)


if __name__ == '__main__':
    unittest.main()
