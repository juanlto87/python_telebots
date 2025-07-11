class Atleta:
    def __init__(self, nombre, edad, deporte, altura, peso):
        self.nombre = nombre
        self.edad = edad
        self.deporte = deporte
        self.altura = altura  # en metros
        self.peso = peso  # en kg
        self.records = {}
        self.medallas = 0
    
    def entrenar(self, horas):
        return f"{self.nombre} ha entrenado {horas} horas en {self.deporte}."
    
    def competir(self, evento):
        return f"{self.nombre} ha competido en {evento} de {self.deporte}."
    
    def ganar_medalla(self):
        self.medallas += 1
        return f"{self.nombre} ha ganado una medalla. Total: {self.medallas}"
    
    def establecer_record(self, categoria, valor):
        self.records[categoria] = valor
        return f"Nuevo récord en {categoria}: {valor}"
    
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return round(imc, 2)
    
    def mostrar_info(self):
        info = f"Atleta: {self.nombre}\n"
        info += f"Edad: {self.edad} años\n"
        info += f"Deporte: {self.deporte}\n"
        info += f"Altura: {self.altura} m\n"
        info += f"Peso: {self.peso} kg\n"
        info += f"IMC: {self.calcular_imc()}\n"
        info += f"Medallas: {self.medallas}\n"
        if self.records:
            info += "Records personales:\n"
            for categoria, valor in self.records.items():
                info += f"  - {categoria}: {valor}\n"
        return info

# Crear un atleta
usain = Atleta("Usain Bolt", 35, "Atletismo", 1.95, 94)

# Realizar operaciones con el atleta
print(usain.entrenar(5))
print(usain.competir("100 metros planos"))
print(usain.establecer_record("100m", "9.58s"))
print(usain.ganar_medalla())
print("\nInformación completa del atleta:")
print(usain.mostrar_info())


# Lista de 3 películas favoritas
peliculas_favoritas = ["El Padrino", "Interestelar", "Matrix"]

# Diccionario con nombre, género y año
mi_info = {"nombre": "Juan", "genero": "Masculino", "año": 2023}

# Imprimir las operaciones
print("\nMis películas favoritas:")
for pelicula in peliculas_favoritas:
    print(f"- {pelicula}")

print("\nMi información personal:")
for clave, valor in mi_info.items():
    print(f"{clave.capitalize()}: {valor}")


    # Definir la clase Pregunta
    class Pregunta:
        def __init__(self, enunciado, opciones, respuesta):
            self.enunciado = enunciado
            self.opciones = opciones
            self.respuesta = respuesta
        
        def mostrar_pregunta(self):
            print(self.enunciado)
            for i, opcion in enumerate(self.opciones, 1):
                print(f"{i}. {opcion}")
        
        def verificar_respuesta(self, respuesta_usuario):
            if respuesta_usuario == self.respuesta:
                return True
            return False

    # Crear una pregunta de ejemplo
    pregunta1 = Pregunta(
        "¿Cuál es la capital de Francia?",
        ["Madrid", "París", "Roma", "Berlín"],
        2  # La respuesta correcta es París, que es la opción 2
    )

    # Mostrar la pregunta
    print("\n--- Juego de Preguntas ---")
    pregunta1.mostrar_pregunta()

    # Solicitar respuesta al usuario
    respuesta_usuario = int(input("Ingrese el número de su respuesta: "))

    # Verificar si la respuesta es correcta
    if pregunta1.verificar_respuesta(respuesta_usuario):
        print("¡Correcto! Esa es la respuesta correcta.")
    else:
        print(f"Incorrecto. La respuesta correcta era: {pregunta1.opciones[pregunta1.respuesta-1]}")

    # Ejemplo adicional solicitado por el usuario
    numero = int(input("Ingrese número: "))
    print(f"El número ingresado es: {numero}")