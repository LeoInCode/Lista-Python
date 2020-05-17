num = int(input('Informe um número para ser fatorado: '))
x = 1
soma = 1
while num > x: ## Seria muito chato usar for, perda de tempo. Melhor caminho para o resultado
    soma *= num
    print('Fatoração: {} -> {}'.format(num,soma))
    num -= 1