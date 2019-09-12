
def soma(n1, n2):
    res = -(-n1 - n2) if n1 // 1 == n1 and n2 // 1 == n2 else print('valor invalido')
    print('{} + {} = {}'.format(n1, n2, res))
        
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

soma(n1, n2)
