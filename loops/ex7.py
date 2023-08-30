mas = 0
fem = 0
sexo = ''

while (sexo != 'sair'):
    sexo = input('digite seu sexo (M para masculino e F para feminino): ').lower()
    if (sexo == 'm'):
        mas += 1
    elif (sexo == 'f'):
        fem += 1
    else:
        print('sexo invalido!')
        
print('quantidade de mulheres:', fem, '\nquantidade de homens:', mas)