# Hyperdimensional Computing (HDC) Framework

HOWTO:

```python
from hdc import Space

# create a new hyper-space with default values (1000 dimensions, binary spatter codes representation)
s = Space()

# add a few hyper-vectors into the space
s.add()               # with randomly generated name
s.add('SoHyper')      # named hyper-vector

u = s.add()           # add a new hyper-vector and store it in a variable
v = s.add('v')

# retrieve hyper-vector
x = s['SoHyper']

# HDC operations
# *   binding
# +   bundling
A = x * u + v

# distance calculation
A.dist(v)

# clean-up memory, i.e. similarity check
B = A * u
s.find(B)
```
