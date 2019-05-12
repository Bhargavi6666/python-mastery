# The false value of the bool type.
# False = 'false' # SyntaxError
# print(type(False)) # <class 'bool'>

# The true value of the bool type.
# True = 'true' # SyntaxError
# print(type(True)) # <class 'bool'>

# The sole value of the type NoneType.
# None is frequently used to represent the absence of a value, as when default arguments are not passed to a function.
# None = 'null' # SyntaxError
# print(type(None)) # <class 'NoneType'>

# Special value that should be returned by dunder methods to indicate that the operation is not implemented with respect to the other type.
# NotImplemented = 'NotImplemented' # Succeeds...
# print(type(NotImplemented)) # NotImplementedType

# The same as the ellipsis literal "..."
# print(Ellipsis)
# print(type(Ellipsis))

# The constant is true if Python was not started with an -o option.
# print(__debug__)
# print(type(__debug__))

# Python meta:
# print(copyright)
# print(credits)
# print(license())

# Terminate the interpreter
# quit()
# exit()