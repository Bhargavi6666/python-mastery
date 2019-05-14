# # try|except|else|finally
# try:
#     assert True, 'Failed to evaluate True to True.'
# except AssertionError as error:
#     print(error)
# else:
#     print('The assertion didn\'t fail.')
# finally:
#     print('Always run this code, disregarding exceptions.')

# # Execution doesn't stop after caught exceptions
# try:
#     assert False, 'Failed to evaluate False to True.'
# except AssertionError as error:
#     print(error)
# print('Execution continues...')

# # Execution stops for uncaught errors (AssertionError)
# assert False, 'Failed to evaluate False to True.' # Execution stops here.

# # ZeroDivisionError - Manually construct the error output.
# try:
#     print(0 / 0)
# except Exception as err:
#     message = '{0}: {1}\nerr: {2}\nerr.args: {3}\ndir(err.__traceback__): {4}\nerr.__traceback__.tb_frame: {5}'.format( \
#         type(err).__name__, \
#         err, \
#         err.args, \
#         dir(err.__traceback__), \
#         err.__traceback__.tb_frame,
#         err.__cause__ \
#     )
#     print(message)
#     # digging into the traceback
#     frame = err.__traceback__.tb_frame
#     # breakpoint()

# Manually raise an exception
try:
    raise Exception('You manually raised an Exception. This is it\'s message.')
except Exception as error:
    print(type(error).__name__, ':', error)

import sys
try:
    assert ('linux' in sys.platform), "This code runs on linux only."
except Exception as error:
    print(type(error).__name__, ':', error)

# Exception Base Classes
# raise BaseException(': BaseException manually raised.')
# raise Exception(': Exception manually raised.')
# raise ArithmeticError(': ArithmeticError manually raised.')
# raise BufferError(': BufferError manually raised.')
# raise LookupError(': LookupError manually raised.')
# raise BaseException(': BaseException manually raised.')

# Concrete Exceptions
try:
    raise AssertionError(': AssertionError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise AttributeError(': AttributeError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise EOFError(': EOFError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise FloatingPointError(': FloatingPointError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
# try:
#     raise GeneratorExit(': GeneratorExit manually raised.')
# except Exception as error:
#     print(type(error).__name__, ':', error)
try:
    raise ImportError(': ImportError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise ModuleNotFoundError(': ModuleNotFoundError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise IndexError(': IndexError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise KeyError(': KeyError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise NameError(': NameError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise NotImplementedError(': NotImplementedError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise OverflowError(': OverflowError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise RecursionError(': RecursionError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise ReferenceError(': ReferenceError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise RuntimeError(': RuntimeError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise StopIteration(': StopIteration manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise StopAsyncIteration(': StopAsyncIteration manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise SyntaxError(': SyntaxError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise IndentationError(': IndentationError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise TabError(': TabError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise SystemError(': SystemError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
# try:
#     raise SystemExit(': SystemExit manually raised.')
# except Exception as error:
#     print(type(error).__name__, ':', error)
try:
    raise TypeError(': TypeError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise UnboundLocalError(': UnboundLocalError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise UnicodeError(': UnicodeError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise UnicodeEncodeError(': UnicodeEncodeError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise UnicodeDecodeError(': UnicodeDecodeError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise UnicodeTranslateError(': UnicodeTranslateError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise ValueError(': ValueError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise ZeroDivisionError(': ZeroDivisionError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise EnvironmentError(': EnvironmentError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise IOError(': IOError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)

# OS Exceptions
try:
    raise BlockingIOError(': BlockingIOError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise ChildProcessError(': ChildProcessError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise ConnectionError(': ConnectionError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise BrokenPipeError(': BrokenPipeError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise ConnectionAbortedError(': ConnectionAbortedError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise ConnectionError(': ConnectionError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise ConnectionRefusedError(': ConnectionRefusedError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise ConnectionResetError(': ConnectionResetError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise FileExistsError(': FileExistsError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise IsADirectoryError(': IsADirectoryError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise NotADirectoryError(': NotADirectoryError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise PermissionError(': PermissionError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise ProcessLookupError(': ProcessLookupError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise TimeoutError(': TimeoutError manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)

# Warnings
try:
    raise Warning(': Warning manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise UserWarning(': UserWarning manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise DeprecationWarning(': DeprecationWarning manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise PendingDeprecationWarning(': PendingDeprecationWarning manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise SyntaxWarning(': SyntaxWarning manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise RuntimeWarning(': RuntimeWarning manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise FutureWarning(': FutureWarning manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise ImportWarning(': ImportWarning manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise UnicodeWarning(': UnicodeWarning manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise BytesWarning(': BytesWarning manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)
try:
    raise ResourceWarning(': ResourceWarning manually raised.')
except Exception as error:
    print(type(error).__name__, ':', error)




# Exception Hierarchy
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning


