import re

# Regex101: https://regex101.com/r/AZLmbb/3

pattern = r"^(?:[+-]?)\d+(?:\.\d+)?$"

regex = re.compile(pattern, flags=re.M)

test_str = ("Válidos\n"
	"0.0\n"
	"00.00\n"
	"000.000\n"
	"+0.0\n"
	"-00.00\n"
	"+000.000\n"
	"10\n"
	"50\n"
	"8.5\n"
	"-8.5\n"
	"+10.5005412136\n"
	"1231345458.54654564\n"
	"-133215646589.6543215648978977\n"
	"+1.11123123\n"
	"-0.154987\n"
	"1.121654987\n"
	"10.123\n"
	"10.1\n"
	"-1.1\n"
	"Inválidos\n"
	"10..2\n"
	"++1213\n"
	"--1235050\n"
	".124546\n"
	"-.1231324\n"
	"10.\n"
	".1\n"
	".10\n"
	"10.\n"
	"+10.\n"
	"-10.\n"
	"5a\n"
	"b5")

# Imprime números válidos
for num in regex.findall(test_str):
    print('Num: ', num)

print('*'*50)
print('\n\n')

float_pat = r'^[+-]?\d+(?:\.\d+)?$'
is_float = lambda st: bool(re.search(float_pat, st))

int_pat = r'^[+-]?\d+$'
is_int = lambda st: re.search(int_pat, st)

while True:
    num = input('Digite um número: ')

    if is_int(num):
        num_int = int(num)
        print(f'O número {num_int} foi convertido para int.\n')
    elif is_float(num):
        num_float = float(num)
        print(f'O número {num_float} foi convertido para float.\n')
    else:
        print('Impossível converter.')
        