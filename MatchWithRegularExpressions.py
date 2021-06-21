import re
result = re.match('You', 'Young Frankenstein')
print(result)

youPattern = re.compile('You')
result = youPattern.match('Young Frankenstein')
print(result)
