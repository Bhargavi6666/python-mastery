p = print

# return the absolute value of a number.
# p(abs(-1))

# return True if all the elements of the iterable are true, or the iterable is empty.
# p(all([True, 1]))
# p(all([]))
# p(all(1))
# p(all([False]))

# return True if any element of the iterable is true. If the iterable is empty, return false
# p(any([True, 1, False]))
# p(any([]))
# p(any([False]))

# As repr, return an ASCII escaped string for a value
# p(ascii(any))
# p(ascii('£'))
# p(repr('£'))

# Convert an integer to a binary string prefixed with 0b. Also works if the value has an __index__() method that returns an integer.
# p(bin(3))
# p(bin('W')) # TypeError
# p(format(14, 'b'))

# Return a Boolean value by evaluating an expressions truthiness
# p(bool('A'))
# p(bool(True))
# p(bool(False))
# p(bool(-1))
# p(bool(0))

# This function drops you into the debugger at the call site.
# a = [1,2,3]
# breakpoint()

# Return a new array of bytes, using a specified encoding for strings.
# p(bytearray(1))
# p(bytearray('word', 'utf-8'))

# Return a new bytes object, which is an immutable sequence of integers in the range 0-256
# p(bytes('seven', 'utf-8'))
# p(bytes([1,2,3]))

# Return True if the object arkgument appears callable, False if not.
# p(callable(1))
# p(callable('test'))
# p(callable(callable))

# Return the string representing a character whose Unicode code point is the integer i.
# This is this inverse of ord()
# p(ord('£'))
# p(chr(21))
# p(chr(88))
# p(chr(240))
# p(ord('W'))

# Transform a method into a class method, which is callable on the class, or an instance of the class
# class C:
#     @classmethod
#     def f(cls, test):
#         print(cls)
#         print(test)
#     def g(self, test):
#         print(self, test)

# C.f('Test')
# C.g('Instance', 'Test') # requires instantiation, or to pass an instance as an argument

# Compile the souce in to a code or AST object. Code objects can be executed with exec() or eval()
# compile()

# Return a complex number with the value real + imag*1j or convert a string or number to a complex number.
# p(complex(1))
# p(complex('test')) # Value Error

# The function deletes the named attribute, provided the object allows it.
# class B:
#     x = 12
# p(B.x)
# del B.x
# # p(B.x) # AttributeError: type object 'B' has no attribute 'x'
# B.x = 12
# p(B.x)
# delattr(B, 'x')
# p(B.x) # AttributeError: type object 'B' has no attribute 'x'

# Create a new dictionary
# d = dict(test='Test')
# p(d)
# g = dict([1,2,3]) # TypeError: cannot convert dictionary update sequence element #0 to a sequence.
# p(g)
# y = dict({'tes////t': 12})
# p(y)

# Without args, return a list of names in the current local scope.
# With an arg, attempt to return a list of valid attributes for that object
# def test():
#     ex = 12
#     print(ex)
#     return dir()
# p(test())
# p(dir(callable))
# p(dir(y))
# p(dir())
# p(__builtins__)
# p(__package__)
# p(__name__)

# Take two numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.
# p(divmod(1.123, 3))
# p(divmod(25, 5))
# p(divmod(100, 11))

# Return an enumerate object. Iterable must be a sequnce, an iterator, or some othe object which supports iteration.
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# e = enumerate(seasons)
# p(e)
# p(list(enumerate(seasons)))
# p(e.__next__())
# p(e.__next__())
# p(list(e))
# p(e.__next__()) # StopIteration. Enumerate object is exhausted by call to list(e).