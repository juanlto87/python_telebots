import datetime

def es_primo(num):
    """Verifica si un número es primo."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    n = int(input("Ingrese un número entero positivo: "))
    if n < 1:
        print("Por favor ingrese un número entero positivo.")
    else:
        print(f"Números primos del 1 al {n}:")
        for numero in range(2, n + 1):
            if es_primo(numero):
                print(numero, end=" ")
        print()  # Salto de línea al final
except ValueError:
    print("Entrada inválida. Por favor ingrese un número entero.")

def mostrar_menu():
    """Muestra un menú interactivo con opciones."""
    
    ejecutar = True
    
    while ejecutar:
        print("\n=== MENÚ INTERACTIVO ===")
        print("1. Mostrar una frase motivacional")
        print("2. Mostrar la fecha actual")
        print("3. Salir del programa")
        
        try:
            opcion = int(input("\nSeleccione una opción (1-3): "))
            
            if opcion == 1:
                print("\n'El único modo de hacer un gran trabajo es amar lo que haces.' - Steve Jobs")
            elif opcion == 2:
                fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
                print(f"\nLa fecha actual es: {fecha_actual}")
            elif opcion == 3:
                print("\n¡Hasta pronto!")
                ejecutar = False
            else:
                print("\nOpción no válida. Por favor, seleccione una opción del 1 al 3.")
        except ValueError:
            print("\nEntrada inválida. Por favor ingrese un número.")

mostrar_menu()
