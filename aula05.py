# Meta caracteres: ^ $
# ()     \1 (retrovisor)
# () ()  \1 \2
# (())()   \1 \2 \3

import re
from pprint import pprint

text = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

pat1 = r'(<([a-z]{1,3})>(.*?)<\/\2>)'

tags = re.findall(pat1, text)

for tag in tags:
    wholetag, tagtype, tagtext = tag
    print('Tag completa: ', wholetag)
    print('Tipo tag: ', tagtype)
    print('Texto tag: ', tagtext)
    print('-'*20)

print('\n\n')

# Ignorando um grupo (add ?:)
pat2 = r'(<([a-z]{1,3})>(?:.*?)<\/\2>)'
tags = re.findall(pat2, text)

pprint(tags)

print('\n\n')

# Nomeando um grupo
pat3 = r'(<(?P<tag>[a-z]{1,3})>(.*?)<\/(?P=tag)>)'
tags = re.findall(pat3, text)

for tag in tags:
    wholetag, tagtype, tagtext = tag
    print('Tag completa: ', wholetag)
    print('Tipo tag: ', tagtype)
    print('Texto tag: ', tagtext)
    print('*'*20)

print('\n\n')

# Substituindo um grupo

pat4 = r'(<(.+?)>)(.+?)(</\2>)'
repl = r'\1"\3"\4'
print('>>> SUB:')
print(re.sub(pat4, repl, text))

print('\n\n')

cpf = '147.852.963-12'
pat_cpf = r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})'

print(re.findall(pat_cpf, cpf))