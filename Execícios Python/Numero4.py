soma = 0
x = 0
while True:
    idade = int(input('Digite um numero inteiro: '))
    if idade == 0:
        break
    soma += idade
    x += 1

print('Media das idades {:.2f}'.format(soma/x))