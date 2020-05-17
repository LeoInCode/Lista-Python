from Numero1 import Error, InputError

cand1 = 0
cand2 = 0
cand3 = 0
x = 0
total = int(input('Digite o número total de votandes: '))
while x < total:
    print('\nCandidatos: 1 - Leonardo, 2 - Anderson, 3 - Dean')
    try:
        cand = int(input('Digite o número do candidato: '))
        if cand != 1 and cand != 2 and cand != 3:
             raise InputError('Digite Novamente!')
        else:
            if cand == 1:
                cand1 += 1
            elif cand == 2:
                cand2 += 1
            else:
                cand3 += 1
        x += 1
    except BaseException:
        print("Número dos candidatos variam de 1 a 3!")

print('\nCandidato 1 - Leonardo: {} votos'.format(cand1))
print('Candidato 2 - Anderson: {} votos'.format(cand2))
print('Candidato 3 - Dean: {} votos'.format(cand3))