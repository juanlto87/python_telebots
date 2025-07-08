# ---------------------------
# Fundamentos de Python
# ---------------------------

# Variables y tipos de datos

# Operadores básicos
a = 10
b = 3
print('Suma:', a + b)
print('Resta:', a - b)
print('Multiplicación:', a * b)
print('División:', a / b)
print('División Entera:', a // b)
print('Módulo:', a % b)
print('Potencia:', a ** b)

# ---------------------------
# Estructuras de control
# ---------------------------

# Condicionales

# numero = int(input("Ingresa un número: "))
numero = 5  # Puedes cambiar este valor para probar diferentes condiciones
if numero > 0:
    print("Es positivo")
elif numero < 0:
    print("Es negativo")
else:
    print("Es cero")

# Comparaciones
x = 15
y = 20
print(x == y)  # False
print(x != y)  # True
print(x < y)   # True

# Booleanos
llueve = True
tengo_paraguas = False

if llueve and tengo_paraguas:
    print("Puedo salir tranquilo")
elif llueve and not tengo_paraguas:
    print("Me voy a mojar")
else:
    print("Día soleado")

# ---------------------------
# Bucles
# ---------------------------

# Bucle for
for i in range(5):
    print("Número:", i)

# Bucle while
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

# ---------------------------
# Funciones
# ---------------------------

def saludar(nombre, apellido=""):
    return f"Hola, {nombre} {apellido}!"

print(saludar("John"))
print(saludar("John", "Doe"))

def suma(x, y):
    return x + y

print("Suma:", suma(3, 4))

# ---------------------------
# Manejo de errores
# ---------------------------

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Fin del bloque try-except")
