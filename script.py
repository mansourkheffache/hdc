from hdc import Space

s = Space(rep='bsd')
u = s.add('USA')
d = s.add('DOLLAR')
m = s.add('MEXICO')
p = s.add('PESOS')

x = s.add('COUNTRY')
y = s.add('CURRENCY')

a = x * u + y * d
b = x * m + y * p
