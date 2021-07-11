
import re

source = 'Young Frankenstein'

m = re.sub('n', '?', source)
print(m)  # sub returns a string
