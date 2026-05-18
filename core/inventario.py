class Inventario:
    def __init__(self):
        self.stock = {}
        self.alertas = []

    def agregar_stock(self, producto, cantidad: int):
        if producto not in self.stock:
            self.stock[producto] = 0
        self.stock[producto] += cantidad
        producto.disponibilidad = (self.stock[producto] > 0)

    def descontar(self, producto, cantidad: int) -> bool:
        disponible = self.stock.get(producto, 0)

        if disponible < cantidad:
            self.generar_alerta(f"Stock insuficiente para {producto.nombre}")
            producto.disponibilidad = disponible > 0
            return False
        
        self.stock[producto] -= cantidad
        producto.disponibilidad = self.stock[producto] > 0

        if self.stock[producto] <= 2:
            self.generar_alerta(f"Stock bajo de {producto.nombre}: quedan {self.stock[producto]}")
        
        return True

    def verificar_disponible(self, producto, cantidad: int = 1) -> bool:
        return (self.stock.get(producto, 0) >= cantidad)

    def generar_alerta(self, mensaje: str):
        self.alertas.append(mensaje)

    def mostrar_alertas(self):
        if not self.alertas:
            print("No hay alertas de inventario.")
            return

        print("Alertas de inventario: ")
        for alerta in self.alertas:
            print(f"- {alerta}")
    