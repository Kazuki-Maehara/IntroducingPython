import re

source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''

m = re.search(r'(. dish\b).*(\bfish)', source)
print(
    m.group()
)
print(
    m.groups()
)

mm = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)

print(
    mm.group()
)

print(
    mm.groups()
)

print(
    mm.group('DISH')
)

print(
    mm.group('FISH')
)
