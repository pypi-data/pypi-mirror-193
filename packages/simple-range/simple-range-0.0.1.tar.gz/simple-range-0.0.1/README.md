# simple-range
Weka-inspired index range using human-readable 1-based indices and placeholders, 
e.g.: `first-last`, `1-10,12,20-last`

Available placeholders:
* `first` - the first index
* `second` - the second index
* `third` - the third index
* `last_2` - the third to last index
* `last_1` - the second to last index
* `last` - the last index


## Installation

```
pip install simple-range
```

## Examples

The following code:

```python
from simple_range import Range

r = Range("1-3", maximum=10)
print(r, "-->", r.indices())
r = Range("first-last", maximum=10) 
print(r, "-->", r.indices(zero_based=False))
r = Range("first-3,11,14-14,30,last", maximum=40)
print(r, "-->", r.indices())
print(r, "-->", r.indices(zero_based=False))
```

Will generate this output:

```
1-3 --> [0, 1, 2]
first-last --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first-3,11,14-14,30,last --> [0, 1, 2, 10, 13, 29, 39]
first-3,11,14-14,30,last --> [1, 2, 3, 11, 14, 30, 40]
```
