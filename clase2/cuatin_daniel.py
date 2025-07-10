
""" 
La clase Heroe representa a un superhéroe con un nombre y un poder.
Tiene un método para presentarse.
Elegimos esta clase para ilustrar el concepto de clases en Python, es una forma 
sencilla de entender cómo funcionan los objetos y métodos.
"""
# Ejercio 1: Definición de una clase Heroe
class Heroe:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

    def presentar(self):
        print(f"Soy {self.nombre} y tengo el poder de {self.poder}.")

""" 
La clase Celular representa un teléfono móvil con atributos como marca, modelo, año y color.
Tiene métodos para realizar llamadas, enviar mensajes y mostrar información del celular.
"""
class Celular:
    def __init__(self, marca, modelo, year, color):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.color = color

    def llmar(self, numero):
        print(f"Llamando al número {numero} desde el celular {self.marca} {self.modelo}.")
    
    def enviar_mensaje(self, numero, mensaje):
        print(f"Enviando mensaje '{mensaje}' al número {numero} desde el celular {self.marca} {self.modelo}.")
    
    def mostrar_info(self):
        print(f"Celular: {self.marca} {self.modelo}")
        
# Ejercicio 2: Listas y diccionarios

class Pelicula:
    def __init__(self, titulo, director, anio):
        self.titulo = titulo
        self.director = director
        self.anio = anio

    def mostrar_info(self):
        print(f"{self.titulo} ({self.anio}), dirigido por {self.director}.")
        
    
        
# Ejercicio 3: Trivia con POO

class Pregunta:
    def __init__(self, pregunta, opciones, respuesta_correcta):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta

    def verificar_respuesta(self, respuesta_usuario):
        try:
            return self.opciones[int(respuesta_usuario) - 1] == self.respuesta_correcta
        except (ValueError, IndexError):
            return False

class Trivia:
    def __init__(self):
        self.preguntas = []
    
    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)
    
    def iniciar_trivia(self):
        for pregunta in self.preguntas:
            print(pregunta.pregunta)
            for i, opcion in enumerate(pregunta.opciones, 1):
                print(f"{i}. {opcion}")
            respuesta_usuario = input("Selecciona la opción correcta: ")
            if pregunta.verificar_respuesta(respuesta_usuario):
                print("¡Respuesta correcta!")
            else:
                print(f"Respuesta incorrecta. La respuesta correcta era: {pregunta.respuesta_correcta}")    
    
if __name__ == "__main__":
    # Ejercicio 1: Crear un héroe y presentarlo
    heroe = Heroe("Superman", "volar")
    heroe.presentar()

    # Ejercicio 2: Crear un celular y mostrar su información
    celular = Celular("Samsung", "Galaxy S21", 2021, "Negro")
    celular.mostrar_info()
    celular.llmar("123456789")
    celular.enviar_mensaje("987654321", "Hola, ¿cómo estás?")
    
    # Ejercicio 2: Crear una lista de películas
    peliculas = [
        Pelicula("Toy Story", "John Lasseter", 1995),
        Pelicula("Forrest Gump", "Robert Zemeckis", 1994),
        Pelicula("Insidious", "James Wan", 2010),
        Pelicula("El Padrino", "Francis Ford Coppola", 1972),
    ]
    for pelicula in peliculas:
        pelicula.mostrar_info()

    # Ejercicio 3: Crear una trivia y iniciarla
    trivia = Trivia()
    pregunta1 = Pregunta(
        "¿Cuál es la capital de Francia?",
        ["Berlín", "Madrid", "París", "Roma"],
        "París"
    )
    trivia.agregar_pregunta(pregunta1)
    pregunta2 = Pregunta(
        "¿Cuál es el océano más grande del mundo?",
        ["Atlántico", "Índico", "Ártico", "Pacífico"],
        "Pacífico"
    )
    trivia.agregar_pregunta(pregunta2)
    pregunta3 = Pregunta(
        "¿Quién escribió 'Cien años de soledad'?",
        ["Gabriel García Márquez", "Mario Vargas Llosa", "Jorge Luis Borges", "Pablo Neruda"],
        "Gabriel García Márquez"
    )
    trivia.agregar_pregunta(pregunta3)
    trivia.iniciar_trivia()
