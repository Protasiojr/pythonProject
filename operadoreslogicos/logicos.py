"""
OPERADORES LOGICOS

AND 'e'
OR 'ou'
NOT 'nao'
IN 'contem dentro da string'
NOT IN 'nao contem dentro da string'
"""

letra = input('Digite uma letra: ')
nome = 'João Protásio'

if letra in nome:
    print(f'Existe dentro de {nome}')
elif letra == 'a':
    print(f'A letra a existe, porem vc precisa especificar o acento {nome}')
else:
    print(f'Não existe dentro de nome {nome}')