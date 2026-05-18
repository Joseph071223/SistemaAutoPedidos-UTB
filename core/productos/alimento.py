from .productos import Producto

class Alimento(Producto):
    def __init__(self, categoria: str, nombre: str, precio: float, peso: int):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.peso = peso
        self.disponibilidad = True

    def mostrar_info(self):
        return(f"{self.categoria}: {self.nombre} ({self.peso} gr), precio: {self.precio} pesos")