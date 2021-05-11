usuario = input('Digite seu usuario: ')
usuario_db = 'Carlos'
senha = input('Digite sua senha:')
senha_db = '123456'
senha_minima = len(senha)


def validacao_usuario():
    if usuario == usuario_db:
        print(f'O {usuario} esta no banco!')
    else:
        print(f'O {usuario} não está cadastrado ou incorreto...')

def valida_senha():
    if str(senha) == senha_db:
        print(f'A senha, está OK!')
    else:
        print(f'A senha, está incorreta...')


def valida_minima():
    if senha_minima >= 6:
        print(f'A senha está atendendo os caracteres minimos!')
    else:
        print(f'A senha não está atendendo os caracteres minimos para validação...')

validacao_usuario()
valida_senha()
valida_minima()





