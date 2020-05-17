lista = []
num = 0
while True:
    num = int(input('Digite um número: '))
    if num in lista:
        break
    lista.append(num)

lista.sort()
print(lista)
lista.reverse()
print(lista)