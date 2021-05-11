# WHILE PRECISA DE UM CONTADOR PARA FUNCIONAR OU QUE A CONDIÇÃO SEJA VERDADEIRA

contador = 1
acumulador = 0

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
    print('Segue a contagem!')

print('Saiu do while!')