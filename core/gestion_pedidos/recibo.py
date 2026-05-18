class Recibo:
    def __init__(self, pago):
        self.pago = pago

    def generar_recibo(self):
        if self.pago.estado != "procesado":
            return "No se puede generar recibo: el pago no ha sido procesado."

        if self.pago.orden is None:
            return "No se puede generar recibo: el pago no está asociado a una orden."

        orden = self.pago.orden

        productos_agrupados = {}
        for producto in orden.productos:
            clave = producto.mostrar_info()
            if clave not in productos_agrupados:
                productos_agrupados[clave] = 0
            productos_agrupados[clave] += 1

        lineas = ["RECIBO", "--------------------"]
        for i, (info, cantidad) in enumerate(productos_agrupados.items(), start=1):
            lineas.append(f"{i}. {info} (x{cantidad})")

        lineas.append("--------------------")
        lineas.append(f"TOTAL PAGADO: {self.pago.monto} pesos")
        lineas.append(f"ESTADO DEL PAGO: {self.pago.estado}")
        lineas.append(f"METODO: {self.pago.__class__.__name__}")

        if hasattr(self.pago, "cambio"):
            lineas.append(f"CAMBIO: {self.pago.cambio} pesos")

        return "\n".join(lineas)