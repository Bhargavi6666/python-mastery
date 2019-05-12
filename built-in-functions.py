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

# The expression argument is parsed and evaluated as a Python expression
# p(eval('x+1', {}, {'x': 1}))

# This function supports dynamic execution of Python code. object must be either a string or code object.
# exec()

# Construct an iterator from those elements of iterable for which function returns True.
# def filt(x):
#     if x > 5:
#         return True
# p(list(filter(filt, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# Return a floating point numbers constructed from a number or string
# p(float(1.213))
# p(float())

# Convert a value to a formatted representation as controlled by the second argument
# format_spec values are: s(str), b(bin), c(char), d(dec), o(octal), x(hex), n(number)
# print("The float number is:{:f}".format(123.4567898))
# print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))
# # integer numbers with right alignment
# print("{:5d}".format(12))
# # float numbers with center alignment
# print("{:^10.3f}".format(12.2346))
# # integer left alignment filled with zeros
# print("{:<05d}".format(12))
# # float numbers with center alignment
# print("{:=8.3f}".format(-12.2346))

# Returns a new frozenset object, an immutable and hashable iterable type.
# frozenset([1,2,3])

# Return the value of the named attribute of object. Name must be a string.
# p(getattr(callable, 'test')) # AttributeError
# p(dir(callable))
# p(getattr(callable, '__class__'))

# Return a dictionary representing the current global symbol table.
# This is always the dictionary of the current module.
# p(globals())

# The args are an object and a sting. True if object has named attribute.
# p(hasattr(callable, 'test'))

# Return the hash value of the object (it if has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup.
# A hash is a fixed size integer that identifies a particular value. Each value needs to have its own hash.
# This way, for the same value you you will get the same hash, even if it's not the same object.
# Hash values will change every time the same code is executed.
# p(hash(callable))
# a = {'one': 1, 'two': 7, 'three': 'python'}
# # p(hash(a)) # TypeError: unhashable type: 'dict'
# p(hash(a['one']))
# p(hash(a['two']))
# p(hash(181))
# p(hash(181.23))
# p(hash('python'))
# p(hash(a['three']))

# Invoke the built-in help system. If no arg is given, the interactive help system starts on the interpreter console.
# help()
# help(hash)

# Convert an integer to a lowercase hexadecimal string prefixed with "Ox"
# p(hex(255))
# p(hex(-42))
# p(hex(0))
# p(format(255, 'x'))
# p(format(255, 'b'))

# Return the "identity" of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime.
# This is guaranteed to be unique and constant over its lifetime.
# Collisions are possible across different runs of the same code.
# p(id(hex))
# p(id('test'))
# p(id('test'))
# a = 1
# p(id(a))
# p(id(1))
# p(hash(a))
# p(hash(1))
# a = 2
# p(id(a))

# If the prompt arg is present, written to standard out without a trailing newline
# The function the reads a line from input, converts it to a string and returns that.
# x = input('What you type will become the returned value >>>')
# p(x)

# Return an integer object constructed from a number or string x, or return 0 if no args given.
# Note that int always truncates floats towards 0.
# p(int(.9))
# p(int(-.9))
# p([int(y) for y in [ord(x) for x in 'test']])

# Return true if the object arg is an instance of the classinfo argument, or of a subclass thereof
# p(isinstance(int, object))
# p(type(int))
# p(type(type))
# p(type(object))
# p(type(1))
# p(type('test'))
# p(type([]))
# p(type(()))
# p(type({}))

# Return True if a class is a subclass(direct, indirect, or virtual) of the second ardument.
# A class is a subclass of itself. classinfo cn be a tuple of class objects, in which case all entries will be checked.
# p({}.__class__())
# p(issubclass(str, str))
# p(issubclass(str, type)) # False. wtf???
# p(type(str))
# p(issubclass(str, object))
# p(issubclass(type, type))
# p(isinstance(type, type))
# p(issubclass(type, (object, type)))

# Return an iterator object. The second arg requires that object be callable.
# iter(object, b'sentinel')
# Practical Application: Block reader for binary database files.
# from functools import partial
# with open('mydata.db', 'rb') as f:
#     for block in iter(partial(f.read, 64), b''):
#         process_block(block)

# Return the length of an object. May be any sequence or collection
# p(len('test'))
# p(len(callable)) # TypeError: object of type 'builtin_function_or_method' has no len()'
# p(len([1,2,3]))
# p(len({'one': 1, 'two': 2}))

# Rather than being a function, list is a mutable sequence type.
# p(list(['a', 'b', 'c']))
# p(list('abc'))
# p(list(('a', 'b', 'c')))
# p(list({'ay': 'a', 'be': 'b', 'cee': 'c'})) # Creates the list from keys, not values.

# Update and return a dictionary representing the curren local symbol table.
# Note that at the module level, locals() and globals() are the same dictionary.
# p(locals())
# p(locals({'test': 1})) # TypeError: locals takes no arguments.

# map() Returns an iterator that applies function to every item of iterable, yeilding the results.
# def square(x, y=None):
#     print(y)
#     return x * x
# p(list(map(square, [1, 2, 3])))
# p(list(map(square, [1, 2, 3], [4, 5, 6])))
# p(tuple(map(square, [1, 2, 3], [4, 5, 6])))
# p(dict(map(square, [1, 2, 3], [4, 5, 6]))) #TypeError: cannot convert dictionary update sequence element #0 to a sequence

# Return the largest Item in an iterable or the largest of two or more arguments.
# p(max([1, 2]))
# p(max(1, 2))
# p(max('one', 'two', 'three', 'a')) # 'two' is the max, because of the ord() value of char 'w' vs char 'h'

# Return a memory view object created from the given argument
# p(memoryview(b'a'))

# Return the smalest item in an iterable or the smallest of two or more arguments
# p(min([1, 2]))
# p(min(1, 2))
# p(min('one', 'two', 'three', 'a')) # 'a' is the min because the ord() value of 'a'

# Return the next item from the iterator by calling its __next__() method.
# a = iter([1,2,3])
# p(next(a))
# p(next(a))
# p(next(a))
# # p(next(a)) # StopIteration
# p(next(a, 'Exhausted'))

# Return a new featureless object. Object is a base for all classes.
# It has the methods that are common to all instances of Python calsses. This function does not accept any arguments.
# Note: object dosen't have a __dict__, so you can't assign arbitrary attributes to an instance of the object class.
# p(object())
# p(str(object()))

# Convert an integer number to an octa string prefixed with "Oo"
# p(oct(3))
# p(oct(-56))
# p(oct(ord('a')))

# Open file and return an corresponding file object.
# If the file cannot be opened, an OSError is raised.
# File is a path-like object giving the pathname of the file to be opened.
# Modes: r=read, w=write, x=exclusive creation & fails if exists, a=open for writing by append, b=binary mode, t=text mode, += open a disk file for updating.
# mode:'w+b' - Bianry write mode (overwrite). mode='r+b' - Binary write mode without overwrite.
# buffering=8192 is the default chunk size (from io.DEFAULT_BUFFER_SIZE)
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# file = open('README.md', mode='r')
# p(file)
# p(dir(file))
# p(file.buffer)
# p(file.closed)
# p(file.encoding)
# p(file.line_buffering)
# p(file.name)
# p(file.newlines)
# p(file.write_through)
# p(file._CHUNK_SIZE)
# p(file._finalizing)
# p(file.__dict__)
# p(file.__doc__)
# import io
# p(io.DEFAULT_BUFFER_SIZE)
# import locale
# p(locale.getdefaultlocale())
# p(locale.getlocale())
# p(locale.getpreferredencoding())
# p(locale.ABDAY_1)
# p(locale.ABDAY_2)
# p(chr(locale.CRNCYSTR))

# Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.
# p(ord('a'))
# p(ord('€'))

# Return x to the power of y. If z is present, return x to the power y, modulo z
# p(pow(2, 17))
# p(pow(2, 17, 4)) #???

# Print objects to the text stream file, seperated by sep and followed by end.
# print('Hello world!')
# import sys
# print('one', 'two', 'three', sep=' | ', file=sys.stdout, flush=True)

# Return a property attribute.
# class C:
#     def __init__(self):
#         self._x = None
#     def getx(self):
#         return self._x
#     def setx(self, value):
#         self._x = value
#     def delx(self):
#         del self._x
#     x = property(fget=getx, fset=setx, fdel=delx, doc="The docstring.")

# class Parrot:
#     def __init__(self):
#         self._voltage = 100000
#     @property
#     def voltage(self):
#         """Get the current voltage."""
#         return self._voltage

# # parrot = Parrot()
# # p(parrot.voltage)
# # p(parrot.voltage.__doc__)

# c = C()
# c.setx(100)
# p(c.x.__doc__)
# p(c.x)

# range(): Rather than being a function, range is actually an immutable sequence.
# _stop = 10
# _start = 0
# _step = 2
# p(range(_stop))
# p(list(range(_stop)))
# p('String representation: ' + str(range(_stop)))
# p(range(_start, _stop, _step))
# p(list(range(_start, _stop, _step)))

# Return a string containing a printable representation of an object.
# For many types, this function makes an attempt to return a string that would yeild an object with the same value when passed to eval().
# Otherwise the representation is a string enclosed in angle brackets that contain the name of the type of the object, the name, and address of the object.
# A class can control what this function returns for its instances by defining a __repr__() method.
# p(repr(callable))

# Returns a reverse iterator.
# revl = list(reversed([1,2,3]))
# rev = reversed([1,2,3])
# p(list(revl))
# p(rev.__next__())
# p(next(rev))
# p(next(rev))
# # p(next(rev)) # Stop iteration
# p(list(rev))

# Return number rounded to ndigits precision after the decimal point.
# If no ndigits is provided, returns an int
# p(round(1.123))
# p(round(1.123, 2))
# p(round(1.123, 7)) # returns the most precision it can.
# p(round(1.5)) # 2. If equidistant, rounds towards the nearest even number.
# p(round(2.5)) # 2. If equidistant, rounds towards the nearest even number.

# Return a new set object from an iterable.
# p(set([1, 1, 2, 2, 3, 3]))
# p(set((1, 1, 2, 2, 3, 3)))
# p({1, 1, 2, 2, 3, 3}) # Curly brackets indicate a set, not dict, if there are no key-value pairs.

# setattr()

# slice()

# sorted()

# @staticmethod

# str()

# sum()

# super()

# tuple()

# type()

# vars()

# zip()

# __import__()