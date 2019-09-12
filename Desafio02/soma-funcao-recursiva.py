#soma com função recursiva
# def soma (x,y):
#     if ( x == 0):
#         return print(y)
#     if ( y == 0):
#         return print(x)
#     (soma((-(-x-1)),((y-1))))
# x = int(input('Digite o primeiro numero: '))
# y = int(input('Digite o segundo numero: '))
# soma(x,y)

def soma_bitwise(x, y):
    while y:
        x, y = (x ^ y), (x & y) << 1
    return x

x = int(input('Digite o primeiro numero: '))
y = int(input('Digite o segundo numero: '))

print(soma_bitwise(x, y)) 
