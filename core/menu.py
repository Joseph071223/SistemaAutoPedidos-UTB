from __future__ import annotations
from typing import ClassVar

class Menu:
    kioskos: ClassVar[dict[str, "Menu"]] = {}

    def __init__(self, kiosko: str):
        self.productos = []
        self.kiosko: str = kiosko
        type(self).kioskos[kiosko] = self
    
    def mostrar_menu(self):
        print("Menu de hoy:")
        for i, x in enumerate(self.productos):
            info = x.mostrar_info()
            print(f"{i+1}. {info}")

    def ver_producto(self, i:int) -> None:
        if i < 1 or i > len(self.productos):
            print(f"El indice {i} esta fuera de rango.")
            return
        else:
            print(f"{i}. {self.productos[i-1].mostrar_info()}")

    def agregar_producto(self, producto):
        self.productos.append(producto)

    @classmethod
    def filtrar_por_kiosko(cls, nombre_kiosko: str) -> Menu | None:
        return cls.kioskos.get(nombre_kiosko)
            
