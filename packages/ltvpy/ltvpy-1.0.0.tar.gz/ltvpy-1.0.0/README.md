# ltvpy
A small implementation of the [LiteVectors](https://litevectors.org/) serializer in Python.
[NumPy](https://numpy.org/) is used for numeric arrays. 

## Usage

```python
encoded = ltvpy.dumpb({'Name': 'data', 'values': [1, 2, 3]})

decoded = ltvpy.loadb(encoded)
```

## Notes:
Deterministic serialized field order relies on the new default behavior for dictionaries in Python 3.7+ which maintains a fields by insertion order. If you need struct fields serialized in a specific order, use Python 3.7 or higher.


## Testing
This package runs the LiteVector test vectors and other unit tests with the standard Python unittest framework, which can be run from the project root:

```
python3 -m unittest
```