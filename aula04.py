import re

text = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

# RegEx ambígua!
pat = r'<[a-z]{1,3}>.*<\/[a-z]{1,3}>'

print(re.findall(pat, text))

# Forma NÃO gulosa (add ?)
pat = r'<[a-z]{1,3}>.*?<\/[a-z]{1,3}>'

print(re.findall(pat, text))
