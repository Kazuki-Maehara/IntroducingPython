import re

source = 'Young Frankenstein'

m = re.search('Frank', source)
if m:   # search returns an object
    print(m.group())
