
# soma com função recursiva
def soma_recursiva(n1, n2=0):
    try:
        res = n1[n2]
        n2+=1
        return res + soma_recursiva(n1,n2)
        
    except:
        return 0

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

print(soma_recursiva([n1,n2]))