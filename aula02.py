# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

import re

text = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

pat1 = r'João|Maria|adultos'
print(re.findall(pat1, text))

pat2 = r'João|Maria|ad....s'
print(re.findall(pat2, text))

pat3 = r'[Jj]oão|[a-zA-Z0-9]aria|ad....s'
print(re.findall(pat3, text))

pat4 = r'jOãO|mAriA'
print(re.findall(pat4, text, flags=re.IGNORECASE))