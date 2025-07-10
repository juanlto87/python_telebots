print("Hola, soy Andrea Yánez y estoy en la clase 1")

""""
Identificar si un numero es primo y mostrar todos los números primos hasta n

"""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def mostrar_primos_hasta_n(n):
    print("Números primos del 1 al n:")
    for n in range(1, n + 1):
        if es_primo(n):
            print(n, end=" ")

""""
Solicitar al usuario que ingrese un número

"""
try:
    n = int(input("Ingrese un número mayor a 1: "))
    if n < 1:
        print("Por favor, ingrese un número mayor que 1")
    else:
        mostrar_primos_hasta_n(n)
except ValueError:
    print("Entrada inválida. Debe ser un número entero")
