#clase 1 carlos bodero
#print("Clase 1")
from datetime import datetime

def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True

def numeros_primos_hasta(numero):
    primos = []
    for i in range(2, numero + 1):
        if es_primo(i):
            primos.append(i)
    return primos

def menu():
    print("Bienvenido")
    print("1) Frase motivacional")
    print("2) Fecha actual")
    print("3) salir")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        print("¡Sigue adelante, cada día es una nueva oportunidad!")
    elif opcion == "2":
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Fecha actual: {fecha_actual}")
    else:
        print("Saliendo del programa.")
    

if __name__ == "__main__":
    #ejercicio 1
    elnumero = int(input("Ingrese un numero entero positivo: "))
    if elnumero < 0:
        print("Por favor, ingrese un numero entero positivo.")
    elif elnumero < 2:
        print("Por favor, ingrese un numero mayor o igual a 2.")
    else:
        primos = numeros_primos_hasta(elnumero)
        print(f"Numeros primos hasta {elnumero}: {primos}")
    #ejercicio 2
    menu()

