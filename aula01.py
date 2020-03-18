# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

import re

string = "Este é um teste de expressões regulares."

pattern = r'teste'

count = 1

print('>>> SEARCH:')
print(re.search(pattern, string))

print('>>> FINDALL:')
print(re.findall(pattern, string))

print('>>> SUB (count = {}):'.format(count))
print(re.sub(pattern, 'ABCD' ,string, count=count))

print('>>> COMPILE:')
regexp = re.compile(pattern)
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('ABCD', string, count=count))