"""
um numero e par ou impar
"""

numero = input('Digite um numero: ')

if numero.isnumeric():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'É um numero par')
    else:
        print(f'É um numero impar')
else:
    print(f'Não é um, número inteiro...')

"""
hora e saudação 0-11 bom dia 12-17 boa tarde 18-23 boa noite 
"""

hora = input('Digite a hora: ')



if hora.isnumeric():
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print(f'Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa Noite!')
else:
    print(f'Não é um caracter valido, digite novamente: ')



nome = input('Digite seu nome: ')
nome = len(nome)

if nome <= 4:
    print('Seu nome é curto!')
elif nome <= 5 or nome >= 6:
    print('Seu nome é normal')
elif nome >= 7:
    print('Seu nome é grande')