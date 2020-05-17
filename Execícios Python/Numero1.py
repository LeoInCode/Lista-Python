class Error(Exception):
    pass #ele permite que a classe, ou método, não execute nada sem dar erro

class InputError(Error):
    def __init__(self,message):
        self.message = message


if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um valor para n1: '))
            n2 = int(input('Digite um valor para n2: '))

            if n1 > n2:
                 raise InputError('Tente novamente!')
            break
        except BaseException:
            print("n2 precisa ser maior que n1")

    while n1 < n2-1:
        n1 += 1
        print(n1)

