# SHORTHANDS
# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A (re.ASCII)
# \W -> [^a-zA-Z0-9À-ú_]
# \W -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t]
# \S -> [^ \r\n\f\v\t]
# \b -> borda
# \B -> não borda

import re

text = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# Gambiarra
pat_gamb = r'[a-zA-z0-9À-ú]+'
print(re.findall(pat_gamb, text))
print('-'*50)

# Shorthand p/ Python
pat1 = r'\w+'
print(re.findall(pat1, text))
print('-'*50)

pat2 = r'\W+'
print(re.findall(pat2, text, flags=re.ASCII))
print('-'*50)

pat3 = r'\s+'
print(re.findall(pat3, text))
print('-'*50)

# Palavras que iniciam com 'e'
pat4 = r'\be\w+'
print(re.findall(pat4, text))
print('-'*50)

# Palavras que terminam com 'e'
pat5 = r'\w+e\b'
print(re.findall(pat5, text))
print('-'*50)

# Palavras com exatamente 4 letras
pat6 = r'\b\w{4}\b'
print(re.findall(pat6, text))
print('-'*50)

pat7 = r'flo\B'
print(re.findall(pat7, text))
print('-'*50)

print('\n')


#FLAGS
# re.A = re.ASCII
# re.I = re.IGNORECASE
# re.M = re.MULTILINE
# re.S = re.DOTALL (. reconhece tb \n)
# Mais aqui: https://docs.python.org/2/library/re.html

text2 = '''
131.768.460-53 ABC
055.123.060-50 DEF
955.123.060-90
'''

# Não vai achar
pat8 = r'^\d{3}.\d{3}.\d{3}-\d{2}$'
print(re.findall(pat8, text2))

# Encontra o último (flag re.MULTILINE), pois analisa linha a linha
print(re.findall(pat8, text2, flags=re.M))

print('-'*50)

text3 = 'João gosta de folia \n E adora ser amado'

pat9 = r'^J.*o$'
print(re.findall(pat9, text3, flags=re.I | re.S))
