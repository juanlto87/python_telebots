

variable = 12

print("Variable:", variable)
print("tipo de variable:", type(variable))

_variable = "Jazmin"
print("Variable:", _variable)
print("tipo de variable:", type(_variable))

variable2 = True
print("Variable:", variable2)
print("tipo de variable:", type(variable2))

frutas = ["manzana", "banana", "naranja"]
print("Lista de frutas:", frutas)
print("tipo de variable:", type(frutas))

frutas.append("kiwi")
frutas.append("pera")
frutas[1] = "fresa"

for i in range(len(frutas)):
    print("Fruta en la posición", i, ":", frutas[i])
    
print("Lista de frutas actualizada:", frutas)  
print("Lista de frutas actualizada:", len(frutas))  

url = "https://www.google.com/search?sca_esv=c9fe79b891b509d9&rlz=1C1RXQR_esEC1090EC1091&sxsrf=AE3TifMdH4J85Z_s9Qlum4GCGZAXUr0aTA:1751936487775&q=google&udm=2&fbs=AIIjpHx4nJjfGojPVHhEACUHPiMQht6_BFq6vBIoFFRK7qchKBv8IM7dq8CEqHDU3BN7lblAhsJT8_A_Kaclg0ioopJQE57ZvFQVMHSTJKIqr7PDTRrW0fpHAhCDoTXrl0eYRFTG3peOHybQI8l8HdNkuZwz9XosjicNKn9Lb56HRH8vx0mIfw_X_9oTgFUwY3gg_BTiuVcEXArhl72GVbPZtlQ52lflPA&sa=X&ved=2ahUKEwjQnZeAiKyOAxVmRDABHVJ2L9kQtKgLKAF6BAgWEAE&biw=1920&bih=911&dpr=1#vhid=1ykoVglribN-pM&vssid=mosaic"
separar_url = url.split(".")
length_url = len(separar_url)
print("URL original:", url)
print("URL separada por puntos:", separar_url)
print("Cantidad de segmentos en la URL:", length_url)
print("ultima parte de la URL:", separar_url[1])
verduras = ("zanahoria", "brócoli", "espinaca")
# verduras[1] = "lechuga"  # Esto generará un error porque las tuplas son inmutables

# verduras.append("lechuga")
# print("Tupla de verduras:", verduras)
# print("Lista de frutas actualizada:", len(verduras))  

# print("tipo de variable:", type(verduras))

carro = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020
}

carro["color"] = "Rojo"
carro["año"] = "2025"
print(  "Diccionario de carro:", carro)
print("tipo de variable:", type(carro))
print("Marca del carro:", carro["marca"])

lista = list(frutas)
print("Lista de elementos:", lista)
print("Tipo de variable:", type(lista))
lista.append(frutas)
print("Lista de elementos actualizada:", lista)

lista1 = ["Hola Mundo", 122, "Programación", True, 3.14, carro]
print("Lista de elementos:", lista1)
print("Tipo de variable:", type(lista1))
lista1.append(frutas)
print("Lista de elementos actualizada:", lista)
tupla = tuple(lista1)
print("Tupla de elementos:", tupla)
print("Tipo de variable:", type(tupla))

# tupla.append(frutas)  # Esto generará un error porque las tuplas son inmutables

def es_primo(num):
    pass

def ejercicio1():
    es_primo()

def ejercicio2():
    pass

if __name__ == "__main__":
    ejercicio1()
    ejercicio2()