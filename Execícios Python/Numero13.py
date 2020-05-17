lista = []
maior = 0
x = 0
for x in range(0,10):
    lista.append(int(input('Digite um número: ')))
    if maior < lista[x]:
        maior = lista[x]
    x += 1

print('\nMaior: {}'.format(maior))
x = 0
for x in range(0,10):
    if maior == lista[x]:
        print('Posição: {}'.format(x))
    x += 1
