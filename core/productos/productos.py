from abc import ABC, abstractmethod

class Producto(ABC):
    nombre: str
    precio: float
    disponibilidad: bool

    @abstractmethod
    def mostrar_info():
        pass

    # @abstractmethod
    #def calcular_precio():
    #    pass