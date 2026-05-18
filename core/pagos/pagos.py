from abc import ABC, abstractmethod

class Pago(ABC):
    def __init__(self, monto: float):
        self.monto = monto
        self.estado = "pendiente"
        self.orden = None

    def asignar_orden(self, orden):
        self.orden = orden

    @abstractmethod
    def procesar(self) -> bool:
        pass

    def reembolsar(self) -> bool:
        if self.estado != "procesado":
            return False
        self.estado = "reembolsado"
        return True

class Pago_efectivo(Pago):
    def __init__(self, monto: float, entregado: float):
        super().__init__(monto)
        self.entregado = entregado
        self.cambio = 0.0

    def procesar(self) -> bool:
        if self.entregado < self.monto:
            self.estado = "rechazado"
            return False
        self.cambio = self.entregado - self.monto
        self.estado = "procesado"
        return True

class Pago_tarjeta(Pago):
    def __init__(self, monto: float, num_tarjeta: str) -> None:
        super().__init__(monto)
        self.num_tarjeta = num_tarjeta

    def procesar(self) -> bool:
        if len(self.num_tarjeta) < 4:
            self.estado = "rechazado"
            return False

        self.estado = "procesado"
        return True

class Pago_pse(Pago):
    def __init__(self, monto: float, plataforma: str) -> None:
        super().__init__(monto)
        self.plataforma = plataforma

    def procesar(self) -> bool:
        if not self.plataforma.strip():
            self.estado = "rechazado"
            return False

        self.estado = "procesado"
        return True