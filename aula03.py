# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+

import re

text = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
Jã
'''

pat1 = r'jo+ão+'
print(re.findall(pat1, text, flags=re.IGNORECASE))
#print(re.sub(pat1, 'Felipe', text, flags=re.IGNORECASE))

pat2 = r'jo*ão*'
print(re.findall(pat2, text, flags=re.IGNORECASE))
#print(re.sub(pat2, 'Felipe', text, flags=re.IGNORECASE))

pat3 = r'jo?ão?'
print(re.findall(pat3, text, flags=re.IGNORECASE))

pat4 = r'jo{,7}ão{1,7}'
print(re.findall(pat4, text, flags=re.IGNORECASE))

pat5 = r'jo{,9}ão{,7}'
print(re.findall(pat5, text, flags=re.IGNORECASE))

pat6 = r've{3}m{1,2}'
print(re.findall(pat6, text, flags=re.IGNORECASE))

text2 = 'João ama ser amado'

pat7 = r'ama[do]{,2}'
print(re.findall(pat7, text2, flags=re.IGNORECASE))