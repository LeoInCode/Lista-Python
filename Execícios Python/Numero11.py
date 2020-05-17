tupla = ()
lista = []
soma = 0
maior = 0
menor = 9999999
for x in range(0,5):
    lista.append(int(input('Digite um valor: ')))
    if maior < lista.__getitem__(x):
        maior = lista.__getitem__(x)
    elif menor > lista.__getitem__(x):
        menor = lista.__getitem__(x)
    soma += lista.__getitem__(x)

tupla = lista
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
print('Média: {}'.format(soma/5))
