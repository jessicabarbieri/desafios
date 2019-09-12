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

# def soma_bitwise(x, y):
#     while (y != 0):
#         z = x & y
#         x = x ^ y
#         y = z << 1
#     return x
# x = int(input('Digite o primeiro numero: '))
# y = int(input('Digite o segundo numero: '))
# print(soma_bitwise(x, y))


# import sys
# sys.setrecursionlimit(100000)
def soma_bitwise(a, b):
    if b == 0:
        return a
    sum = a ^ b
    carry = (a & b) << 1
    return soma_bitwise(sum, carry)

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))

print(soma_bitwise(a, b)) 
