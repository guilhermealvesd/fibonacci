#Função

def calcular_fibonacci(n):

    if n <= 1:
        return n
    else:
        return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

#Programa Principal

n = int(input('Informe o número de sequências: '))

print(calcular_fibonacci(n))

for x in range(n):
    print(calcular_fibonacci(x))