from decimal import Decimal


x = 10.0 / 3
print(x)

price = Decimal('19.99')
tax = Decimal('0.06')

total = price + price * tax
print(total)

penny = Decimal('0.01')
print(total.quantize(penny))
