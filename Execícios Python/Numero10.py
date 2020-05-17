total = int(input('Número de jogadores do time de futebol: '))
soma = 0
for x in range(0,total):
    altura = float(input('Digite a altura do jogador {}: '.format(x+1)))
    soma += altura

print('Altura média dos jogadores: {:.2f}'.format(soma/total))