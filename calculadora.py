import math

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b

def raiz_quadrada(a):
    if a == 0:
        raise ValueError("Não é possível calcular a raiz quadrade 0!")
    
    if a < 0:
        raise ValueError("N]ao é possível calcular a raiz quadrada de um número negativo!")
    
    return math.sqrt(a)

