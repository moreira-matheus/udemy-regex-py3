# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação


import re

cpf = '147.852.963-12'

pat1 = r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$'
print(re.findall(pat1, cpf))

pat2 = r'[^0-9]+'
print(re.findall(pat2, cpf))

pat3 = r'[^0-9a-zA-Z.]+'
print(re.findall(pat3, cpf))