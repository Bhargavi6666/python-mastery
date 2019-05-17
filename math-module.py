import math

# Sign Manipulation
print(math.copysign(-2, -1)) # Copy the sign of the second arg to the first and return it.
print(math.fabs(-2)) # Return the absolute value

# Sequences
print(math.factorial(5)) # Return the value of !5

# Working with Floats
print(math.frexp(5))
print(math.ldexp(.625, 3))
print(sum([.1]*10)) # Precision limited to 16 decimal points.
print(math.fsum([.1]*10)) # Accurately sum floats to infinite precision

# Modulus
print(math.fmod(-1e-100, 1e100)) # Accurate modulus for working with floats
print(math.modf(5.123456))
print(math.remainder(37.123, 7))
print(37.123 % 7)

# Factoring
print(math.gcd(35, 3500), math.gcd(42, 2996))

# Testing for numeric attributes
print(math.isfinite(math.inf))
print(math.isfinite(0.0))
print(math.isinf(math.inf))
print(math.isnan(float('nan')))
print(math.isclose(sum([.1]*10), math.fsum([.1]*10), rel_tol=.5, abs_tol=0.0))
print(math.isclose(sum([.1]*10), math.fsum([.1]*10), rel_tol=1e-16, abs_tol=0.0))

# CONSTANTS ####################################################################
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)

# Rounding and truncation
print(math.trunc(math.pi))
print(round(math.pi, 2)) # Round to 2 decimal points
print(math.ceil(1.1)) # Round up to the nearest int
print(math.floor(2.9)) #Round down to the nearest int

# Logarithmic Functions
x = 2
y = 3
base = 10
print(math.log(x, base))
print(math.log1p(x))
print(math.log2(x))
print(math.log(x, 2))
print(math.log10(2))
print(math.pow(x, y))
print(math.sqrt(x))

# Trigonometric functions
print(math.cos(x))
print(math.acos(0.64)) # In radians
print(math.sin(x))
print(math.asin(0.64))
print(math.tan(x))
print(math.atan(0.64))
print(math.atan2(y,x))
print(math.cos(x))
print(math.hypot(x,y))

# Angular Conversion
print(math.degrees(math.cos(x))) # Convert radians to degrees
print(math.radians(math.degrees(math.cos(x))))

# Hyperbolic Functions
print(math.acosh(x))
print(math.asinh(x))
print(math.atanh(x))
print(math.cosh(x))
print(math.sinh(x))
print(math.tanh(x))