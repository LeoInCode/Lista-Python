tupla = (5, 1, 4, 2, 6, 8, 4, 24, 3, 10)

num = int(input('Digite um número: '))
x = 0
for x in range(0,10):
    if num == tupla[x]:
        print('Posição: {}'.format(x))  # deveria ter funcionado, sei lá
        break;
    x += 1
