# Python Standard Library Mastery

In depth exploration of the Python 3 standard library, one built-in function, type, exception, and module at a time.

## 1. Built-in Functions

abs | all | any | ascii | bin | bool | breakpoint | bytearray | bytes | callable | chr | classmethod | compile | complex | delattr | dict | dir | divmod | enumerate | eval | exec | filter | float | format | frozenset | getattr | globals | hasattr | hash | help | hex | id | input | int | isinstance | issubclass | iter | len | list | locals | map | max | memoryview | min | next | object | oct | open | ord | pow | print | property | range | repr | reversed | round | set | setattr | slice | sorted | staticmethod | str | sum | super | tuple | type | vars | zip | __import__()

## 2. Built-in Constants

False | True | None | NotImplemented | Ellipsis | __debug__ | copyright | credits | license | quit | exit

## 3. Built-in Types

and | or | not

### Numerics

int | float | complex

### Sequences

list | tuple | range | str | bytes | bytearray | memoryview | set | frozenset

### Mappings

dict

### Classes

module | class | code | type

===

## 4. Built-In Exceptions

Base classes | Concrete exceptions | Warnings | Exception hierarchy

raise | assert | try | catch | else | finally

AssertionError | AttributeError | EOFError | FloatingPointError | GeneratorExit | ImportError | ModuleNotFoundError | IndexError | KeyError | NameError | NotImplementedError | OverflowError | RecursionError | ReferenceError | RuntimeError | StopIteration | StopAsyncIteration | SyntaxError | IndentationError | TabError | SystemError | SystemExit | TypeError | UnboundLocalError | UnicodeError | UnicodeEncodeError | UnicodeDecodeError | UnicodeTranslateError | ValueError | ZeroDivisionError | EnvironmentError | IOError | BlockingIOError | ChildProcessError | ConnectionError | BrokenPipeError | ConnectionAbortedError | ConnectionError | ConnectionRefusedError | ConnectionResetError | FileExistsError | IsADirectoryError | NotADirectoryError | PermissionError | ProcessLookupError | TimeoutError | Warning | UserWarning | DeprecationWarning | PendingDeprecationWarning | SyntaxWarning | RuntimeWarning | FutureWarning | ImportWarning | UnicodeWarning | BytesWarning | ResourceWarning

## 5. Text Processing Services

string | re | difflib | textwrap | unicodedata | stringprep | readline | rlcompleter

## 6. Binary Data Services

struct | codecs

## 7. Data Types

datetime | calendar | collections | collections.abc | heapq | bisect | array | weakref | types | copy | pprint | reprlib | enum

## 8. Numeric and Mathematical Modules

numbers | math | cmath | decimal | fractions | random | statistics

### `math` Module

copysign | fabs | factorial | frexp | ldexp | fsum | fmod | modf | remainder | gcd | isfinite | inf | isinf | isnan | isclose | pi | e | tau | nan | trunc | ceil | floor | log | log1p | log2 | log10 | pow | sqrt | cos | acos | sin | asin | tan | atan | atan2 | hypot | degrees | radians | acosh | asinh | atanh | cosh | sinh | tanh

## 9. Functional Programming Modules

itertols | functols | operator

## 10. File and Directory Access

pathlib | os.path | fileinput | stat | filecmp | tempfile | glob | fnmatch | linecache | shutil

### `os.path` Module

abspath | basename | commonpath | commonprefix | dirname | exists | lexists | expanduser | expandvars | getatime | getctime | getsize | isabs | isfile | islink | ismount | samefile | supports_unicode_filenames | normcase | join | normpath | realpath | relpath | split | splitdrive | splitext

## 11. Data Persistence

pickli | copyreg | shelve | marshal | dbm | sqlite3

## 12. Data Compression and Achiving

zlib | gzip | bz2 | lzma | tarfile

## 13. File Formats

csv | configparser | netrc | xdrlib | plistlib

### `csv` Module

Dialect | DictReader | DictWriter | Error | OrderedDict | QUOTE_ALL | QUOTE_MINIMAL | QUOTE_NONE | QUOTE_NONNUMERIC | Sniffer | StringIO | excel | excel_tab | field_size_limit | get_dialect | list_dialects | re | reader | register_dialect | unix_dialect | unregister_dialect | writer

## 14. Cryptographic Services

hashlib | hmac | secrets

## 15. Generic Operating System Services

os | io | time | argparse | getopt | logging | logging.config | logging.handlers | getpass | curses | curses.textpad | curses.ascii | curses.panel | platform | errno | ctypes

### `os` Module

abc | abort | access | altsep | chdir | chflags | chmod | chown | chroot | close | closerange | confstr | confstr_names | cpu_count | ctermid | curdir | defpath | device_encoding | devnull | dup | dup2 | environ | environb | error | execl | execle | execlp | execlpe | execv | execve | execvp | execvpe | extsep | fchdir | fchmod | fchown | fdopen | fork | forkpty | fpathconf | fsdecode | fsencode | fspath | fstat | fstatvfs | fsync | ftruncate | fwalk | get_blocking | get_exec_path | get_inheritable | get_terminal_size | getcwd | getcwdb | getegid | getenv | getenvb | geteuid | getgid | getgrouplist | getgroups | getloadavg | getlogin | getpgid | getpgrp | getpid | getppid | getpriority | getsid | getuid | initgroups | isatty | kill | killpg | lchflags | lchmod | lchown | linesep | link | listdir | lockf | lseek | lstat | major | makedev | makedirs | minor | mkdir | mkfifo | mknod | name | nice | open | openpty | pardir | path | pathconf | pathconf_names | pathsep | pipe | popen | pread | putenv | pwrite | read | readlink | readv | register_at_fork | remove | removedirs | rename | renames | replace | rmdir | scandir | sched_get_priority_max | sched_get_priority_min | sched_yield | sendfile | sep | set_blocking | set_inheritable | setegid | seteuid | setgid | setgroups | setpgid | setpgrp | setpriority | setregid | setreuid | setsid | setuid | spawnl | spawnle | spawnlp | spawnlpe | spawnv | spawnve | spawnvp | spawnvpe | st | stat | stat_result | statvfs | statvfs_result | strerror | supports_bytes_environ | supports_dir_fd | supports_effective_ids | supports_fd | supports_follow_symlinks | symlink | sync | sys | sysconf | sysconf_names | system | tcgetpgrp | tcsetpgrp | terminal_size | times | times_result | truncate | ttyname | umask | uname | uname_result | unlink | unsetenv | urandom | utime | wait | wait3 | wait4 | waitpid | walk | write | writev

## 16. Concurrent Execution

threading | multiprocessing | concurrent | concurrent.futures | subprocess | sched | queue | _thread | _dummy_thread | dummy_threading | contextvars

## 17. Networking and Interprocess Communication

asyncio | socket | ssl | select | selectors | asyncore | asynchat | signal | mmap

## 18. Internet Data Handling

email | json | mailcap | mailbox | mimetypes | base64 | binhex | binascii | quopri | uu

## 19. Structured Markup Prcussing Tools

html | html.parser | html.entities | xml | xml.etree.ElementTree | xml.dom

## 20. Internet Protocols and Support

webbrowser | cgi | cgitb | wsgiref | urllib | urllib.request | urllib.response | urllib.parse | urllib.error | http | http.client | ftplib | poplib | imaplib | nntplib | smtplib | smtpd | telnetlib | uuid | socketserver | http.server | http.cookies | http.cookiejar | xmlrpc | ipaddress

## 21. Multimedia Services

audioop | aifc | sunau | wave | chunk | colorsys | imghdr | sndhdr | ossaudiodev

## 22. Internationalization

gettext | local

## 23. Development Tools

turtle | cmd | shlex

## 24. Debugging and Profiling

bdb | faulthandler | pdb | timeit | trace | tracemalloc

## 25. Software Packaging and Distribution

distutils | ensurepip | venv | zipapp

## 26. Python Runtime Services

sys | sysconfig | builtins | __main__ | warnings | dataclasses | contextlib | abc | atexit | traceback | __future__ | gc | inspect | site

## 27. Importing Modules

zipimport | pkgutil | modulefinder | runpy | importlib

## 28. Python Language Services

parser | ast | symtable | symbol | token | keyword | tokenize | tabnanny | pyclbr | py_compile | compileall | dis | pickletools
