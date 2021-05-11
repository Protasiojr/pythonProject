texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'n':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)