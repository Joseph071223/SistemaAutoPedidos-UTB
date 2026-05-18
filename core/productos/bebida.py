from .productos import Producto

class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, volumen: int):
        self.nombre = nombre
        self.precio = precio
        self.volumen = volumen

    def mostrar_info(self):
        return(f"{self.nombre} ({self.volumen} ml), precio: {self.precio}")