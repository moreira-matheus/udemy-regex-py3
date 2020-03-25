#Formatos IPv4
# 0.0.0.0 255.255.255.255
#Formatos CPF
# 025.258.963-10 02525896310

import re

cpfs = '''
025.258.963-10
02525896310
'''

# Acha os CPFs nos dois formatos
pat_cpf = r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$'
cpf_reg_exp = re.compile(pat_cpf, flags=re.M)
print(cpf_reg_exp.findall(cpfs))

print('-'*50)

pat_ip = r'''
    ^
    (?:
        (?:
            25[0-5]| #   250-255
            2[0-4]\d| #  200-249
            1\d{2}| #    100-199
            [1-9][\d]| #   10-99
            \d #             0-9
        )
        \.
    ){3}
    (?: 25[0-5]|2[0-4]\d|1\d{2}|[1-9][\d]|\d)
    $
'''

# flag re.X = re.VERBOSE -> permite comentarios no pattern
ip_reg_exp = re.compile(pat_ip, flags=re.VERBOSE)

# Imprime os IPs válidos
for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    if ip_reg_exp.findall(ip):
        print(ip)
