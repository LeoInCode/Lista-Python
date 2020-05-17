listaNome = []
listaNota = []

print('Digite 0 no nome do aluno para sair!')
while True:
    listaNome.append(input('Digite o nome do aluno: '))
    if '0' in listaNome:
        listaNome.pop()
        break
    listaNota.append((float(input('Digite a nota do aluno: '))))

print(listaNome)
print(listaNota)