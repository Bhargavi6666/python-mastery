import string
p = print

# STRING CONSTANTS #############################################################
p(string.ascii_letters)
p(string.ascii_lowercase)
p(string.ascii_uppercase)
p(string.digits)
p(string.hexdigits)
p(string.octdigits)
p(string.punctuation)
p(string.printable)

# CUSTOM STRING FORMATTER ######################################################
f = string.Formatter()
format_string = 'Sphinx of black quartz, judge my {vow}. First, thou shalt count to {0}, then {1}.'
args = [1, 2]
kwargs = {'vow': 'lie'}

# p(f.parse(format_string).__next__())
# p(f.get_field(format_string, *args, **kwargs))
p(f.format(format_string, *args, **kwargs)) # .format() is a wrapper for vformat

# BUILT IN STRING FORMATTER ####################################################
# Positional Aguments
p('{1}, {2}, {0}'.format('c', 'a', 'b'))
p('{}, {}, {}'.format('a', 'b', 'c'))
p('{0}, {1}, {2}'.format(*'abc'))
p('{0}{1}{0}'.format('abra', 'cad'))

# Keyword Arguments
p('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
coordinates = {'latitude':'37.24N', 'longitude':'-115.81W'}
p('Coordinates: {latitude}, {longitude}'.format(**coordinates))

# Accessing argument attributes
c = 3-5j
p(('The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.').format(c))

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)

p(str(Point(4, 2)))

# Accessing arguments' items
coord = (3, 5)
p('X: {0[0]}; Y: {0[1]}'.format(coord))

# Showing repr() and str()
p('repr() shows quotes: {!r}; str() doesn\'t: {!s}'.format('repr()', 'str()'))

# Alignment and width:
p('{:<50}'.format('left aligned, 50 chars wide.'))
p('{:>50}'.format('right aligned, 50 chars wide.'))
p('{:^50}'.format('centered, 50 chars wide.'))
p('{:*^50}'.format('fill with *, centered, 50 chars wide.'))

# Signed numbers
p('Show either sign: {:+f}; {:+f}'.format(3.14, -3.14))
p('Show positive sign only: {: f}; {: f}'.format(3.14, -3.14))
p('Show negative sign only: {:-f}; {:-f}'.format(3.14, -3.14))

# Changing bases
p('int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}'.format(42))
p('(Prefixed) int: {0:d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}'.format(42))

# Thousands separator
p('{:,f}'.format(1234567890.987654))

# Percentages to a specific precision
points = 19
total = 22
p('Correct answers: {:.4%}'.format(points/total))

# Type specific formatting
import datetime
d = datetime.datetime(3020, 6, 3, 12, 16, 58, 999999)
p('{:%Y-%m-%d %H:%M:%S.%s}'.format(d))

# Complex formatting examples
for align, text in zip('<^>', ['left', 'center', 'right']):
    p('{0:{fill}{align}16}'.format(text, fill=align, align=align))

octets = [192, 168, 0, 1]
p('{:02X}{:02X}{:02X}{:02X}'.format(*octets))

width = 5
for num in range(5, 12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

# String substitution
s = string.Template('$who likes $what')
p(s.substitute(who='tim', what='kung pao'))
p(s.safe_substitute(who='tim'))

# Helper functions
p(str.capitalize(format_string.format(1,2, vow='lie')))
p(string.capwords(format_string.format(1,2, vow='lie')))