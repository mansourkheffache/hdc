import numpy as np
import random

random.seed()

class Vector:

    # deifne operations depending on representation

    # binary
    def __init_bsc(size):
        return np.random.randint(2, size=size)

    def __add_bsc(x, y):
        z = x + y
        z[z == 1] = np.random.randint(2, size=len(z[z == 1]))
        z[z == 2] = np.ones(len(z[z == 2]))
        return z

    def __mul_bsc(x, y):
        z = np.bitwise_xor(x, y)
        return z

    def __dist_bsc(x ,y):
        z = np.bitwise_xor(x, y)
        return (np.sum(z[z == 1]) / float(len(z)))

    # biploar
    def __init_bipolar(size):
        return np.random.choice([-1.0, 1.0], size=size)

    def __add_bipolar(x, y):
        z = x + y
        z[z > 1] = 1.0
        z[z < -1] = -1.0
        z[z == 0] = np.random.choice([-1.0, 1.0], size=len(z[z == 0]))
        return z

    def __mul_bipolar(x, y):
        return x * y

    def __dist_bipolar(x, y):
        return (len(x) - np.dot(x, y)) / (2 * float(len(x)))

    # operations list
    __OPERATIONS = {
        'bsc': {
            'init': __init_bsc,
            'add': __add_bsc,
            'mul': __mul_bsc,
            'dist': __dist_bsc
        },
        'bipolar': {
            'init': __init_bipolar,
            'add': __add_bipolar,
            'mul': __mul_bipolar,
            'dist': __dist_bipolar
        }
    }

    # init random HDC vector
    def __init__(self, size, rep):
        self.rep = rep
        self.size = size
        self.value = self.__OPERATIONS[rep]['init'](size)

    # print vector
    def __repr__(self):
        return np.array2string(self.value)

    # print vector
    def __str__(self):
        return np.array2string(self.value)

    # addition
    def __add__(self, a):
        b = Vector(self.size, self.rep);
        b.value = self.__OPERATIONS[self.rep]['add'](self.value, a.value)
        return b

    # multiplication
    def __mul__(self, a):
        b = Vector(self.size, self.rep);
        b.value = self.__OPERATIONS[self.rep]['mul'](self.value, a.value)
        return b

    # distance
    def dist(self, a):
        return self.__OPERATIONS[self.rep]['dist'](self.value, a.value)


class Space:

    def __init__(self, size=32, rep='bsc'):
        self.size = size;
        self.rep = rep;
        self.vectors = {}

    def _random_name(self):
        return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(8))

    def __repr__(self):
        return ''.join("'%s' , %s\n" % (v, self.vectors[v]) for v in self.vectors)

    def __getitem__(self, x):
        return self.vectors[x]

    def add(self, name=None):
        if name == None:
            name = self._random_name()

        v = Vector(self.size, self.rep)

        self.vectors[name] = v
        return v

    def insert(self, v, name=None):
        if name == None:
            name = self._random_name()

        self.vectors[name] = v

        return name

    def find(self, x):
        d = 1.0
        match = None

        for v in self.vectors:
            if self.vectors[v].dist(x) < d:
                match = v
                d = self.vectors[v].dist(x)

        # print d
        return match, d
