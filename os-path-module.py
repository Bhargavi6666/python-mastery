from os import path, curdir
p = print

p(path.abspath('.')) # Get the absolute path of the argument, in this case the cwd.
p(path.abspath('README.md'))
p(path.basename(path.abspath('.'))) # Get the name of the directory or file at the end of a relative or absolute path
p(path.basename(path.abspath('README.md')))

# Get the longest common sub-path of each pathname in a sequence paths.
# Requires all pathnames to be either relative or absolute.
p(path.commonpath(['/Users/tom/Projects/_research', '/Users/tom/Desktop/temp/img.png']))
p(path.commonprefix(['/Users/tom/Projects/_research', '/Users/tom/Desktop/temp/img.png']))

# Return the path up to the containing directory from a relative or absolute path.
p(path.dirname(path.abspath('.')))
p(path.dirname('/Users/tom/Desktop/temp/img.png'))

p(path.exists('/Users/tom/Desktop/temp/img.png')) # False
p(path.lexists('/Users/tom/Desktop/temp/img.png')) # False
p(path.exists('/Users/Shared/')) # True
p(path.lexists('/Users/Shared/')) # True

p(path.expanduser('~/Desktop')) # Epand ~ to an absolute path
p(path.expandvars('$USER')) # Get the value of an env var
p(path.expandvars('$SHELL'))

# Get the last accessed time for a path
import datetime
accessed_time = path.getatime(path.abspath('README.md'))
accessed_time = path.getatime('README.md')
p(datetime.datetime.utcfromtimestamp(accessed_time).strftime('%Y-%m-%d %H:%M:%S'))

created_time = path.getctime('README.md')
p(datetime.datetime.utcfromtimestamp(created_time).strftime('%Y-%m-%d %H:%M:%S'))

p(path.getsize('README.md')) # Filesize in bytes

# Check if a path is an absolute path
p(path.isabs('README.md'))
p(path.isabs('/'))

# Check for various path attributes
p(path.isfile('README.md'))
p(path.islink('README.md'))
p(path.ismount('/Volumes/mirror'))
p(path.samefile('README.md', path.abspath('README.md')))
p(path.supports_unicode_filenames)

p(path.normcase(path.join(path.expanduser('~'), 'Desktop')))
p(path.normpath('/mnt//test/..')) # /mnt
p(path.realpath(path.expanduser('~/Google Drive')))

# Get path relative to an arbitrary absolute path
p(path.relpath(path.abspath('README.md'), start=path.abspath(path.expanduser('~'))))



p(path.join(path.expanduser('~'), 'Desktop'))
p(path.split(path.abspath('README.md')))
p(path.split(path.abspath('.'))) # Split the basepath and end dir or file into a tuple
p(path.splitdrive(path.abspath('.'))) # On windows, split off the drive from a path.
p(path.splitext(path.abspath('README.md'))) # Split the extension from a filename
p(path.splitext(path.abspath('.'))) # index 1 in the returned tuple will be an empty string.