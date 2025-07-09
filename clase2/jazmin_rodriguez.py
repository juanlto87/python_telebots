class Animal:
    def __init__(self, tipo, nombre=""):
        self.tipo = tipo
        self.nombre = nombre

    def correr(self):
        if self.tipo == "Felino":
            print(f"El felino {self.nombre} corre más rápido")
        elif self.tipo == "Canino":
            print(f"El canino {self.nombre} corre con resistencia")
        elif self.tipo == "Ave":
            print(f"El ave {self.nombre} vuela en lugar de correr")
            
    def alimentar(self):
        if self.tipo == "Felino":
            print(f"El felino {self.nombre} come carne")
        elif self.tipo == "Canino":
            print(f"El canino {self.nombre} come croquetas")
        elif self.tipo == "Ave":
            print(f"El ave {self.nombre} come semillas")
            
    def object(self):
        return {
            "tipo": self.tipo,
            "nombre": self.nombre, 
        }
        
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

class Felino(Animal):
    def __init__(self, nombre):
        super().__init__("Felino", nombre)
        
class Canino(Animal):
    def __init__(self, nombre):
        super().__init__("Canino", nombre)
        
if __name__ == "__main__":
    
    tigre = Animal("Felino", "Tigre")
    tigre.correr()
    lobo = Animal("Canino", "Lobo")
    lobo.correr()
    aguila = Animal("Ave")
    aguila.correr()
    
    leon = Felino("León")
    leon.correr()
    leon.alimentar()
    perro = Canino("Perro")
    perro.alimentar()
    lobo.cambiar_nombre("Lobo de Montaña")
    print("Lobo actualizado:", lobo.nombre)
    lobo_objeto_json = lobo.object()
    nombre_lobo = lobo_objeto_json["nombre"]
    print("Lobo en formato JSON:", lobo_objeto_json)
    print("Lobo en formato JSON nombre:", nombre_lobo)
    lobo_objeto_json["nombre"] = "Lobo de la Noche"
    lobo_objeto_json["tipo"] = "Perro salvaje"
    nuevo_lobo = lobo_objeto_json["nombre"]
    print("nuevo lobo:", lobo_objeto_json["tipo"])
    
