#while
contador = 0
while contador < 2:
    contador += 1
    primeiro_algarismo = input('Digite o primeiro algarismo: ')
    segundo_algarismo = input('Digite o segundo algarismo: ')
    operador = input('Digite o operador: ')
    sair = input('Deseja sair? Digite [S]im ou [N]ão: ')

    if sair == 's':
        print('Você saiu do programa!')
        break

    if not primeiro_algarismo.isnumeric() or not segundo_algarismo.isnumeric():
        print('Você precisa digitar um numero valido: ')
        continue

    primeiro_algarismo = int(primeiro_algarismo)
    segundo_algarismo = int(segundo_algarismo)

    if operador == '+':
        print(f'O resultado é: {primeiro_algarismo + segundo_algarismo}')
    if operador == '-':
        print(f'O resultado é: {primeiro_algarismo - segundo_algarismo}')
    if operador == '*':
        print(f'O resultado é: {primeiro_algarismo * segundo_algarismo}')
    if operador == '/':
        print(f'O resultado é: {primeiro_algarismo / segundo_algarismo}')
    else:
        print('Você precisa digitar um operador valido: ')


