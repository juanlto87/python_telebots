def es_primo(n):
    """Determina si un número es primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Ingrese un número: "))
print(f"Números primos del 1 al {n}:")
for i in range(1, n+1):
    if es_primo(i):
        print(i)

# Ejercicio 2: Menú interactivo

import datetime

while True:
    print("\nMenú:")
    print("1. Mostrar una frase motivacional")
    print("2. Mostrar la fecha actual")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("🚀 ¡Tú puedes con todo! Sigue luchando por tus sueños.")
    elif opcion == "2":
        print("📅 La fecha actual es:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    elif opcion == "3":
        print("👋 ¡Hasta pronto, te saluda Belén Villavicencio de la clase de PYTHON!")
        break
    else:
        print("❌ Opción no válida. Intenta de nuevo.")

    