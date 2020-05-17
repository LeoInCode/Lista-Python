listaTotal = []
listaPar = []
listaImp = []

for x in range(0,10):
    listaTotal.append(int(input('Digite um número: ')))

for x in range(0,10):
    if listaTotal.__getitem__(x) % 2 == 0:
        listaPar.append(listaTotal.__getitem__(x))
    else:
        listaImp.append(listaTotal.__getitem__(x))

print('Lista completa: {]'.format(listaTotal))
print('Lista par: {}'.format(listaPar))
print('Lista impar: {}'.format(listaImp))