
def multiplica(n1, n2):
    res = float(n1) / (1 / float(n2))
    print('{} * {} = {}'.format(n1, n2, res))

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

multiplica(n1, n2)

