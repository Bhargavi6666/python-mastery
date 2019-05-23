import os
p = print

p(os)
p(os.error) # Alias for OSError builtin exception

# SYSTEM
p('name:', os.name) # posix, nt, java
uname = os.uname()
p('sysname:', uname.sysname) # Operating System Type
p('nodename:', uname.nodename) # Computer Name
p('release:', uname.release) # OS Release number
p('version:', uname.version) # Os Version
p('machine:', uname.machine) # Processor Type

# ENVIRONMENT
# p(dir(os))
print(os.ctermid()) # /dev/tty - filename of the controlling terminal of the process
# p(os.environ) # A mapping object representing the string environment
# p(os.environb) # Bytes Version
# p(dict(os.environ).keys())

# os.putenv('NEW_VAR', 'New Value')
os.environ['NEW_VAR'] = 'New Value' # Adds a new env var to the process
p(os.environ['NEW_VAR'])
p(os.getenv('NEW_VAR')) # Same
p(os.unsetenv('NEW_VAR'))

# DIRECTORIES
p(os.getcwd()) # Get the current working directory
os.chdir('../') # Change directories
p(os.getcwd()) # Get the current working directory

p(os.fsencode('README.md')) # Encode a path-like filename to the filesystem encoding

file = os.fsencode('README.md')
p(os.fsdecode(file)) # The inverse function
p(os.fspath(os.getcwd())) # return the file system rep of the path
p(os.PathLike.__mro__)
p(os.get_exec_path(env=os.environ)) # The list of directories that will be searched for a named executable, similar shell when launching a process. Env is optional.

# SUPPORT CONSTANTS
p(os.supports_bytes_environ)
p(os.supports_dir_fd)
p(os.supports_effective_ids) # Builtins that support effective ids
p(os.supports_fd) # Builtins that support fd
p(os.supports_follow_symlinks) # Builtins that support following symlinks


# PROCESS, GROUP, and USER IDS
p(os.getegid()) # Get he effective group id f the current process.
p(os.geteuid()) # Return the current process's effective user id.
p(os.getgid()) # Get the current processes real group id
p(os.getgrouplist(os.getlogin(), os.getgid()))
p(os.getgroups()) # return list of supplemental group ids associated with the current process
p(os.getlogin()) # Return the name of the user logged in on the controlling terminal of the process

# PROCESS ID
p(os.getpgid(os.getpid()))
p(os.getpid())
p(os.getpgrp())
p(os.getppid())

# PROCESS SCHEDULING PRIORITY
p(os.getpriority(os.PRIO_PROCESS, os.getpid()))
p(os.getpriority(os.PRIO_PGRP, os.getpid()))
# p(os.getpriority(os.PRIO_USER, os.getpid()))

p(os.getuid()) # get the current processes real user id
# p(os.umask(mask)) # Set umask, return the prev


# FILE OBJECT CREATION