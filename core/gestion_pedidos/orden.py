class Orden:
    def __init__(self, carrito):
        self.carrito = carrito
        self.productos = []
        self.total = 0.0
        self.generada = False
        self.pago = None

    def generar_pedido(self):
        if len(self.carrito.productos) == 0:
            return "No se puede generar un pedido con el carrito vacío."

        self.productos = self.carrito.productos.copy()
        self.total = self.carrito.calcular_total
        self.generada = True
        return f"Pedido generado correctamente. Total: {self.total} pesos"

    def asignar_pago(self, pago):
        if not self.generada:
            return "No se puede asignar pago: la orden aún no ha sido generada."

        self.pago = pago
        self.pago.asignar_orden(self)
        return "El pago fue asociado correctamente a la orden."

    def procesar_pago(self):
        if not self.generada:
            return "La orden no ha sido generada."

        if self.pago is None:
            return "No hay un pago asociado a la orden."

        if self.pago.monto != self.total:
            return "El monto del pago no coincide con el total de la orden."

        exito = self.pago.procesar()
        if exito:
            return "Pago procesado correctamente."
        return "No se pudo procesar el pago."