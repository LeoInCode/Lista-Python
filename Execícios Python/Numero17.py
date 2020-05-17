listaNome = []
listaNum = []
class Agenda:
    def inserirContato(self):
        listaNome.append(input('Digite o nome: '))
        listaNum.append(int(input('Digite o número: ')))
    def excluirContato(self,nome):
        num = listaNome.index(nome)
        listaNome.remove(nome)
        listaNum.pop(num)
    def buscarContato(self,nome):
        num = listaNome.index(nome)
        print(nome+' -> {}'.format(listaNum.__getitem__(num)))
    def listarContatos(self):
        indice = 0
        for x in listaNome:
            print('{} - '.format(indice)+listaNome.__getitem__(indice)+' -> {}'.format(listaNum.__getitem__(indice)))
            indice += 1
    def removerIndice(self,num):
        listaNome.pop(num)
        listaNum.pop(num)

def menu():
    print('1 - Inserir Contato')
    print('2 - Remover Contato')
    print('3 - Buscar Contato')
    print('4 - Remover Índice')
    print('5 - Visualizar Contatos')
    print('0 - Sair')

def opcao(op,agenda):
    if op == 1:
        agenda.inserirContato()
    elif op == 2:
        nome = input('Contato: ')
        agenda.excluirContato(nome)
    elif op == 3:
        nome = input('Contato: ')
        agenda.buscarContato(nome)
    elif op == 4:
        num = int(input('Índice: '))
        agenda.removerIndice(num)
    else:
        agenda.listarContatos()


if __name__ == '__main__':
    agenda = Agenda()
    while True:
        menu()
        op = int(input('Digite a opção desejada: '))
        if op == 0:
            break
        opcao(op,agenda)
        print('\n')
