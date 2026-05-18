from .menu import Menu

class Usuario:
    def __init__(self, id: str, nombre: str, email: str) -> None:
        self.id = id
        self.nombre = nombre
        self.email = email

    def autenticar(self) -> bool:
        return bool(self.id and self.nombre and self.email)


class Estudiante(Usuario):
    def __init__(self, id: str, nombre: str, email: str, codigo: str) -> None:
        super().__init__(id, nombre, email)
        self.codigo = codigo
        self.historial = []

    def ver_historial(self):
        if not self.historial:
            return "No hay pedidos en el historial."
        return "\n".join(str(item) for item in self.historial)


class Administrador(Usuario):
    def __init__(self, id: str, nombre: str, email: str, nivel: str, turno: str) -> None:
        super().__init__(id, nombre, email)
        self.nivel = nivel
        self.turno = turno

    def gestionar_menu(self, accion: str, nombre_kiosko: str, producto=None, indice: int | None = None):
        menu = Menu.filtrar_por_kiosko(nombre_kiosko)

        if menu is None:
            return f"No existe un menú registrado para el kiosko '{nombre_kiosko}'."

        accion = accion.lower()

        if accion == "ver":
            menu.mostrar_menu()
            return f"{self.nombre} consultó el menú del kiosko '{nombre_kiosko}'."

        if accion == "agregar":
            if producto is None:
                return "Debes proporcionar un producto para agregar."
            menu.agregar_producto(producto)
            return f"Producto agregado al menú del kiosko '{nombre_kiosko}'."

        if accion == "eliminar":
            if indice is None:
                return "Debes proporcionar un índice para eliminar."
            if indice < 1 or indice > len(menu.productos):
                return f"El índice {indice} no existe en el menú."
            eliminado = menu.productos.pop(indice - 1)
            return f"Se eliminó '{eliminado.nombre}' del menú del kiosko '{nombre_kiosko}'."

        if accion == "ver_producto":
            if indice is None:
                return "Debes proporcionar un índice para ver el producto."
            menu.ver_producto(indice)
            return f"{self.nombre} consultó un producto del menú."

            return f"La acción '{accion}' no es válida."