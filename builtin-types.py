# Comparisons #######################################
# print(1 > 2)
# print(1 <= 2)
# print(2 <= 2)
# print(1 > 2)
# print(1 >= 2)
# print(2 >= 2)
# print(3 >= 2)
# print(2 == 1)
# a = 1
# print(a is 1)
# print(a is not 2)

# Numeric Types #####################################
x = 1
y = 2
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y) # Floored quotient of x and y
# print(x % y) # Remainer of x / y
# print(-x)
# print(+x)
# print(abs(-x))
# print(int(x))
# print(float(x))
# print(complex(2, 2))
# print(complex(2,2).conjugate())
# print(divmod(x, y)) # The pair x // y, x % y
# print(pow(x, y))
# print(x ** y)

# BITWISE OPERATIONS #####################################
# print(bin(x | y), bin(x), bin(y))
# print(bin(x ^ y), bin(x), bin(y))
# print(bin(x & y), bin(x), bin(y))
# print(bin(~255), ~255)
# print(x << 3)
# print(x << 8)
# print(y << 7)
# print(x.bit_length())
# print(y.bit_length())
# print((255).to_bytes(1, byteorder='big'))
# print((255).to_bytes(2, byteorder='little'))
# print(int.from_bytes(b'\x00\x10', byteorder='big'))
# print((2.5).as_integer_ratio())
# print((2.0).is_integer())
# print((2.1).is_integer())
# print((2.1).hex())

# Iterator (Generator) Types ##############################
# container = [1,2,3]
# x = container.__iter__()
# print(x)
# print(x.__iter__())
# print(x.__next__())

# Sequences ###############################################
# a = [1,2,3]
# b = 'testing'

# print(1 in a)
# print(1 not in a)
# print(a + [4])
# print(a * 3)
# print(a[1], a[1:2], a[1:3], a[0:2:2])
# print(len(a))
# print(min(a), max(a))
# print(b.index('ing'))
# print(b.index('t', 7)) # ValueError: substring not found
# print(b.index('t', 2, 7))
# print(b.index('t', 2))

# TEXT SEQUENCE TYPE ######################################
a = '\tthe quick brown fox'
b = 'thequickbrownfox'
# print(a.capitalize())
# print(a.casefold())
# print(a.center(50, '+'))
# print(a.count('t'))
# print(a.encode(encoding='utf-8', errors='strict'))
# print(a.endswith('x'))
# print(a.expandtabs(tabsize=4))
# print(a.find('qu', 0, 10))
# print('the sum of 1 +  2 is {0}'.format(1+2))
# print('{name} was born in {country}'.format_map({'name':'Guy', 'country': 'Netherlands'}))
# print(a.index('test')) # ValueError
# print(a.find('test')) # -1
# print(b.isalnum())
# print(b.isalpha())
# print(a.isalpha())
# print(a.isascii())
# print(a.isdecimal())
# print('123'.isdecimal())
# print('123.123'.isdecimal())
# print('123.123'.isdigit())
# print('123'.isdigit())
# print(a.islower())
# print(''.isprintable())
# print(''.isspace())
# print(' '.isspace())
# print('\t\n '.isspace())
# print(a.istitle())
# print(a.isupper())
# print(''.join(['a', 'b', 'c']))
# print(a.ljust(50, '_'))
# print(a.lower())
# print(a.lstrip())
# print(a.replace('t', 'T', 1))
# print(a.rfind('x', 0, 99))
# print(a.rindex('x', 0, 99))
# print(a.rjust(50, '='))
# print(a.rsplit(' '))
# print(a.rstrip(['\n','ast']))
# print(a.splitlines())
# print(a.startswith('t', 0, 1))
# print(a.strip())
# print(a.swapcase())
# print(a.title())
# print(a.upper())
# print(a.strip().zfill(50))
# print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number": 2})

# String Formatting ########################################
# #: The value conversion will use the alternate form.
# 0: The conversion will be zero padded for numeric values
# -: The converted value is left adjusted
#  : A blank should be left before a positive number
# +: A sign char will precede the conversion (overrides the blank flag)

# d, i: signed integer decimal
# o: signed octal value
# x, X: signed hexadecimal
# e, E: Floating point exponential format
# f, F: Floating point decimal format
# g, G: Floating point format. Uses exponential format if exponent is less than -4.
# c: single byte
# b: bytes
# %: no argument is converted, results in a '%' char in the result.

# SETS ####################################################
# s = {0,1,2,3}
# x = {2,3,4}
# y = {4,5,6}
# d = {1,2,3,4,5,6}
# print(len(s))
# print(2 in s)
# print(4 not in s)
# print(s.isdisjoint(x))
# print(s.isdisjoint(y))
# print(s.issubset(d))
# print(d.issuperset(s))
# print(s.union(x,y,d))
# print(d.difference(s))
# print(s.symmetric_difference(d))
# print(s.copy())
# s.update(x)
# print(s)
# s.difference_update(x)
# print(s)
# s.symmetric_difference_update(x)
# print(s)
# s.add(9)
# print(s)
# s.remove(9)
# print(s)
# # s.remove(9) # KeyError
# s.discard(9)
# print(s.pop())
# print(s.pop())
# s.clear()
# print(s)

# MAPPING TYPES ###########################################
a = dict(one=1, two=2, three=3)
c = dict(zip(['one', 'two'], (1, 2)))
print(len(a))
print(a['one'])
a['four'] = 4
print(a)
del a['four']
print(a)
print('four' not in a)
print('three' in a)
print(list(iter(a)))
b = a.copy()
a.clear()
print(a)
print(b)
print(a.fromkeys(['one', 'five'], None))
print(c.get('one'))
print(c.keys())
print(c.items())
print(c.values())
print(list(c.items()))
print(list(c.keys()))
print(list(c.values()))
print(c.pop('one'))
print(c)
print(c.popitem())
print(c.setdefault('one', 99))
c.update({'two': 2})
print(c)

# SPECIAL ATTRIBUTES ######################################
# print(object.__dict__)
instance = dict()
# print(instance.__class__)
# print(dict.__bases__)
# print(dict.__base__)
# print(dict.__name__)
# print(dict.__qualname__)
# print(dict.__mro__)
# print(dict.mro())
# print(dict.__subclasses__())