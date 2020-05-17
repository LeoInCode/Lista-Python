x = 0
maior = 0
menor = 999999
lista = []
while x < 10:
    lista.append(int(input('Digite um valor: ')))
    if maior < lista.__getitem__(x):
        maior = lista.__getitem__(x)
    elif menor > lista.__getitem__(x):
        menor = lista.__getitem__(x)
    x += 1

print(maior)
print(menor)

### OU ###
### De forma mais prática, isso excluiria 4 linhas de código
### do laço de repetição

print('\n'+max(lista))
print(min(lista))