# Clase que representa un celular
class Celular:
    def __init__(self, marca, modelo, año, color):
        """Constructor del objeto celular."""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def llamar(self, numero):
        """Simula una llamada a un número."""
        print(f"Llamando al {numero} desde un {self.marca} {self.modelo}...")

    def enviar_mensaje(self, numero, mensaje):
        """Simula el envío de un mensaje a un número."""
        print(f"Enviando mensaje a {numero}: {mensaje}")


# Crear una instancia (objeto) de la clase Celular
mi_celular = Celular("Apple", "iPhone 13", 2021, "Negro")

# Operaciones con el objeto
mi_celular.llamar("0987654321")
mi_celular.enviar_mensaje("0987654321", "Hola, ¿cómo estás?")

# Explicación del objeto
"""
Este objeto representa un celular. Lo elegí porque es un dispositivo con el que interactuamos a diario.
Tiene atributos como marca, modelo, año y color, y puede realizar acciones como llamar y enviar mensajes.
Esto muestra cómo en POO los objetos agrupan datos y funciones relacionados.
"""
