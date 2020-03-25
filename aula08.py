import re
from pprint import pprint


text = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

# Pega apenas os IPs
pat1 = r'\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+\w+\s+\w+'
print(re.findall(pat1, text))

print('-'*50)

# Positive Lookahead (retorna os IPs ativos)
pat2 = r'\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+\w+\s+(?=active)'
print(re.findall(pat2, text))

print('-'*50)

# Negative look ahead (retorna os IPs não ativos)
pat3 = r'\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+\w+\s+(?!active)'
print(re.findall(pat3, text))

print('-'*50)

# Positive lookahead (retorna as linhas com IPs ativos)
pat4 = r'(?=.*\bactive).+'
print(re.findall(pat4, text))

print('-'*50)

# Positive lookbehind (retorna IPs com status ONLINE)
pat5 = r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+'
print(re.findall(pat5, text))

print('-'*50)

# Negative lookbehind (retorna IPs com status não ONLINE)
pat6 = r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+'
print(re.findall(pat6, text))

print('-'*50)

# Positive lookbehind (retorna linhas com status ONLINE - sem grupo!)
pat6 = r'\w+(?<=ONLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+'
print(re.findall(pat6, text))

# Positive lookbehind (retorna linhas com status ONLINE - omite status -> sem \w+)
pat7 = r'(?<=ONLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+'
print(re.findall(pat7, text))
