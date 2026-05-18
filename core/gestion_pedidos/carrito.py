from core.productos.productos import Producto

class Carrito:
    def __init__(self):
        self.productos = []

    @property
    def calcular_total(self):
        total = 0
        for i, x in enumerate(self.productos):
            total += x.precio
        return total

    def info_carrito(self):
        print("Carrito de compras:")
        if len(self.productos) == 0:
            print("El carrito de compras esta vació.")
        else:
            for i, x in enumerate(self.productos):
                    info = x.mostrar_info()
                    print(f"{i+1}. {info}")
            print(f"Total: {self.calcular_total} pesos")

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def eliminar_producto(self, i: int) -> None:
        if i < 1 or i > len(self.productos):
            print(f"El indice {i} no esta en el carrito.")
            return
        else:
            self.productos.pop(i-1)