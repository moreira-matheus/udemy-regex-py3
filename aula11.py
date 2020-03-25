import re

# Regex101: https://regex101.com/r/SpIQ5b/2

pattern = r"(?:\(\d{2}\)\s)?(?:9\s)?(?:\d{4}-\d{4})"
regex = re.compile(pattern, flags=re.M)

test_str = ("(21) 9 8852-5214\n"
	        "(11) 9955-1231\n"
	        "(35) 9 9975-4521\n"
	        "(31)    3851-5213\n" # Inválido!
	        "9 8571-5213\n"
	        "1234-5647")

for telefone in regex.findall(test_str):
    print('Telefone: ', telefone)
