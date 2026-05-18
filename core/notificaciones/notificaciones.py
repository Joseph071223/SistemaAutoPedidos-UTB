class Notificacion:
    def __init__(self, mensaje: str, canal: str):
        self.mensaje = mensaje
        self.canal = canal
        self.leido = False

    def enviar(self) -> str:
        return f"Enviando por {self.canal}: {self.mensaje}"

    def marcar_leida(self) -> None:
        self.leido = True