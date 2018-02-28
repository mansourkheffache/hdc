import numpy as np
import random

random.seed()

class Vector:

    v_size = 10000                                            # size of HDC vector

    # init random HDC vector
    def __init__(self):
        self.value = np.random.randint(2, size=self.v_size)

    # print vector
    def __repr__(self):
        return np.array2string(self.value)

    # print vector
    def __str__(self):
        return np.array2string(self.value)

    # addition
    def __add__(self, a):
        b = Vector();
        b.value = self.value + a.value
        # b.value /= 2.0
        b.value[b.value == 1] = np.random.randint(2, size=len(b.value[b.value == 1]))
        b.value[b.value == 2] = np.ones(len(b.value[b.value == 2]))
        return b

    # multiplication
    def __mul__(self, a):
        b = Vector()
        b.value = np.bitwise_xor(self.value, a.value)
        return b

    # distance
    def dist(self, a):
        b = self * a
        return (np.sum(b.value[b.value == 1]) / float(self.v_size))


class Space:

    def __init__(self, size=32, rep='bsc'):
        self.size = size;
        self.rep = rep;
        self.vectors = {}

    def _random_name(self):
        return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(8))

    def add(self, name=None, v=None):
        if v == None:
            v = Vector()
        if name == None:
            name = self._random_name()

        self.vectors[name] = v
        return name, v

    def __repr__(self):
        return ''.join("'%s' , %s\n" % (v, self.vectors[v]) for v in self.vectors)

    def __getitem__(self, x):
        # if isinstance(x, str):
        return self.vectors[x]
        # elif isinstance(x, Vector):
        #     d = 1.0
        #     match = None
        #     for v in self.vectors:
        #         if self.vectors[v].dist(x) < d:
        #             match = v
        #             d = self.vectors[v].dist(x)
        #     return match
        # else:
        #     raise ValueError

    def find(self, x):
        d = 1.0
        match = None

        for v in self.vectors:
            if self.vectors[v].dist(x) < d:
                match = v
                d = self.vectors[v].dist(x)
        print d
        return match
