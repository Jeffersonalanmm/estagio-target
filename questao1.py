def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def numeroPertence(n):
    numeroFibonacci = fibonacci(n)
    if n == numeroFibonacci:
        return f'{n} pertence a sequência de Fibonacci'
    else:
        return f'{n} não pertence a sequência de Fibonacci'



n = int(input('Digite um numero inteiro positivo: '))
print(numeroPertence(n))