from fractions import Fraction
from decimal import Decimal


result = Fraction(1, 3) * Fraction(2, 3)

print(result)

print(Fraction(1.0 / 3.0))

print(Fraction(Decimal('1.0') / Decimal('3.0')))
