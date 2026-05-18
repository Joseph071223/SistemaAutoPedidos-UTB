import flet as ft
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "proyecto"))
from core.productos.alimento import Alimento
from core.productos.bebida import Bebida
from core.gestion_pedidos.carrito import Carrito as CarritoBackend
from core.gestion_pedidos.orden import Orden
from core.gestion_pedidos.recibo import Recibo
from core.pagos.pagos import Pago_efectivo, Pago_tarjeta, Pago_pse
from core.inventario import Inventario
from core.usuarios import Estudiante, Administrador

#  PALETA — fijos
UTB_BLUE   = "#003DA5"
UTB_BLUE2  = "#0052CC"
ACCENT     = "#FF6B35"
SUCCESS    = "#22C55E"
DANGER     = "#EF4444"

# Dinámicos — se asignan según tema del sistema
WHITE      = "#FFFFFF"
BG         = "#F0F4FF"
CARD_BG    = "#FFFFFF"
TEXT_DARK  = "#0F172A"
TEXT_GRAY  = "#64748B"
TEXT_LIGHT = "#94A3B8"
DIVIDER    = "#E2E8F0"
TAG_BG     = "#EEF2FF"

def set_theme(dark: bool):
    global WHITE, BG, CARD_BG, TEXT_DARK, TEXT_GRAY, TEXT_LIGHT, DIVIDER, TAG_BG
    if dark:
        WHITE      = "#1E293B"
        BG         = "#0F172A"
        CARD_BG    = "#1E293B"
        TEXT_DARK  = "#F1F5F9"
        TEXT_GRAY  = "#94A3B8"
        TEXT_LIGHT = "#475569"
        DIVIDER    = "#334155"
        TAG_BG     = "#2563EB"
    else:
        WHITE      = "#FFFFFF"
        BG         = "#F0F4FF"
        CARD_BG    = "#FFFFFF"
        TEXT_DARK  = "#0F172A"
        TEXT_GRAY  = "#64748B"
        TEXT_LIGHT = "#94A3B8"
        DIVIDER    = "#E2E8F0"
        TAG_BG     = "#EEF2FF"

#  KIOSCOS
KIOSCOS = [
    {"img": "carne.png",    "nombre": "El Asa'o"},
    {"img": "ensalada.png", "nombre": "Punto Fit"},
    {"img": "helado.png",   "nombre": "Alegría"},
    {"img": "antojo.png", "nombre": "Antojos"},
]

# ── Objetos backend ────────────────────────────────────────────────────────
# Antojos
_detodito_nat  = Alimento("Snack", "Detodito natural",    3500, 30)
_detodito_mix  = Alimento("Snack", "Detodito mix",        3500, 30)
_detodito_bbq  = Alimento("Snack", "Detodito BBQ",        3500, 30)
_doritos_qso   = Alimento("Snack", "Doritos queso",       3000, 28)
_doritos_fh    = Alimento("Snack", "Doritos Flaming hot", 3500, 28)
_rizadas_pol   = Alimento("Snack", "Rizadas pollo",       2500, 25)
_rizadas_lim   = Alimento("Snack", "Rizadas limón",       2500, 25)
_rizadas_may   = Alimento("Snack", "Rizadas mayonesa",    2500, 25)
_gol           = Bebida("Gol",                            2000, 300)
_natuchip      = Alimento("Snack", "Natuchip",            3400, 30)
_manimoto      = Alimento("Snack", "Manimoto",            2500, 20)
_dedito_qso    = Alimento("Snack", "Dedito de queso",     3000,  30)
_emp_pollo     = Alimento("Comida","Empanada de pollo",   3700, 120)
_emp_cerdo     = Alimento("Comida","Empanada de cerdo",   3700, 120)
_speed_max     = Bebida("Speed max",                      2000, 250)
_hit_mango     = Bebida("Hit Mango",    2200, 250)
_hit_mora      = Bebida("Hit Mora",     2200, 250)
_hit_narpi     = Bebida("Hit Naranja Piña", 2200, 250)
_pepsi_ant     = Bebida("Pepsi",                          3000, 350)
_colombiana    = Bebida("Colombiana",                     3000, 350)
_postobon_ant  = Bebida("Postobón",                       3000, 350)
_manzana_ant   = Bebida("Postobón Manzana",                        3000, 350)
_agua_ant      = Bebida("Agua",                           2000, 500)

# Alegría
_crispetas     = Alimento("Snack", "Crispetas",           2000,  50)
_piazas        = Alimento("Snack", "Piazza",               800,  15)
_chocomelo     = Alimento("Dulce", "Chocomelo",           2300,  40)
_sand_pol      = Alimento("Comida","Sandwich pollo",      8000, 250)
_sand_ham      = Alimento("Comida","Sandwich jamón y queso", 10000, 280)

_milo          = Bebida("Milo",                          10000, 300)
_limonada      = Bebida("Limonada",                       8000, 400)
_helado_ale    = Alimento("Postre","Helado",             3000, 100)
_natu_malta    = Bebida("Natumalta",                     2500, 250)
_mr_tea        = Bebida("Mr tea",                         2200, 250)
_agua_ale      = Bebida("Agua",                           2000, 500)
_manzana_ale   = Bebida("Postobón Manzana",                        3000, 350)
_uva_ale       = Bebida("Postobón Uva",                            3000, 350)

# Punto Fit
_granola       = Alimento("Saludable","Granola Tosh",          2500, 150)
_ens_frutas    = Alimento("Saludable","Ensalada de frutas",6000,200)
_hatsu         = Bebida("Hatsu",                          5000, 500)
_h2o           = Bebida("H2O",                            2500, 500)

_pepsi_fit     = Bebida("Pepsi",                          3000, 350)
_helado_fit    = Alimento("Postre","Helado fit",          3000, 100)

# El Asa'o
_salchipapa    = Alimento("Comida","Salchipapa",         30000, 400)
_pechuga_papa  = Alimento("Comida","Pechuga con papa",   20000, 450)
_agua_asao     = Bebida("Agua",                           2000, 500)
_uva_asao      = Bebida("Postobón Uva",                            3000, 350)
_jugo_mora     = Bebida("Jugo de mora",                   2000, 300)
_hamburguesa   = Alimento("Comida","Hamburguesa",        20000, 350)

# Inventario global (20 unidades por producto)
INVENTARIO = Inventario()
for _obj in [
    _dedito_qso,_detodito_nat,_detodito_mix,_detodito_bbq,_doritos_qso,_doritos_fh,
    _rizadas_pol,_rizadas_lim,_rizadas_may,_gol,_natuchip,_manimoto,
    _emp_pollo,_emp_cerdo,_speed_max,_hit_mango,_hit_mora,_hit_narpi,_pepsi_ant,_colombiana,
    _postobon_ant,_manzana_ant,_agua_ant,_crispetas,_piazas,_chocomelo,
    _sand_pol,_sand_ham,_milo,_limonada,_helado_ale,_natu_malta,
    _mr_tea,_agua_ale,_manzana_ale,_uva_ale,_granola,_ens_frutas,_hatsu,
    _h2o,_pepsi_fit,_helado_fit,_salchipapa,_pechuga_papa,
    _agua_asao,_uva_asao,_jugo_mora,_hamburguesa,
]:
    INVENTARIO.agregar_stock(_obj, 20)

# Lista UI — organizada por kiosco
PRODUCTOS = [
    # Antojos
    {"img": "detodito_natural.png", "nombre": "Detodito natural",    "precio": 3500,  "kiosco": "Antojos",   "obj": _detodito_nat},
    {"img": "detodito_mix.png", "nombre": "Detodito mix",        "precio": 3500,  "kiosco": "Antojos",   "obj": _detodito_mix},
    {"img": "detodito_bbq.png", "nombre": "Detodito BBQ",        "precio": 3500,  "kiosco": "Antojos",   "obj": _detodito_bbq},
    {"img": "doritos_queso.png", "nombre": "Doritos queso",       "precio": 3000,  "kiosco": "Antojos",   "obj": _doritos_qso},
    {"img": "doritos_fh.png", "nombre": "Doritos Flaming hot", "precio": 3500,  "kiosco": "Antojos",   "obj": _doritos_fh},
    {"img": "rizadas_pollo.png", "nombre": "Rizadas pollo",       "precio": 2500,  "kiosco": "Antojos",   "obj": _rizadas_pol},
    {"img": "rizadas_limon.png", "nombre": "Rizadas limón",       "precio": 2500,  "kiosco": "Antojos",   "obj": _rizadas_lim},
    {"img": "rizadas_mayo.png", "nombre": "Rizadas mayonesa",    "precio": 2500,  "kiosco": "Antojos",   "obj": _rizadas_may},
    {"img": "gol.png", "nombre": "Gol",                 "precio": 2000,  "kiosco": "Antojos",   "obj": _gol},
    {"img": "natuchip.png", "nombre": "Natuchip",            "precio": 3400,  "kiosco": "Antojos",   "obj": _natuchip},
    {"img": "manimoto.png", "nombre": "Manimoto",            "precio": 2500,  "kiosco": "Antojos",   "obj": _manimoto},
    {"img": "empanada_pollo.png",    "nombre": "Empanada de pollo",   "precio": 3700,  "kiosco": "Antojos",   "obj": _emp_pollo},
    {"img": "empanada_cerdo.png",    "nombre": "Empanada de cerdo",   "precio": 3700,  "kiosco": "Antojos",   "obj": _emp_cerdo},
    {"img": "speed_max.png", "nombre": "Speed max",           "precio": 2000,  "kiosco": "Antojos",   "obj": _speed_max},
    {"img": "hit_mango.png",  "nombre": "Hit Mango",        "precio": 2200,  "kiosco": "Antojos",   "obj": _hit_mango},
    {"img": "hit_mora.png",   "nombre": "Hit Mora",         "precio": 2200,  "kiosco": "Antojos",   "obj": _hit_mora},
    {"img": "hit_narpi.png",  "nombre": "Hit Naranja Piña", "precio": 2200,  "kiosco": "Antojos",   "obj": _hit_narpi},
    {"img": "pepsi.png", "nombre": "Pepsi",               "precio": 3000,  "kiosco": "Antojos",   "obj": _pepsi_ant},
    {"img": "colombiana.png", "nombre": "Colombiana",          "precio": 3000,  "kiosco": "Antojos",   "obj": _colombiana},
    {"img": "postobon_manzana.png", "nombre": "Postobón Manzana", "precio": 3000,  "kiosco": "Antojos",   "obj": _manzana_ant},
    {"img": "agua.png", "nombre": "Agua",                "precio": 2000,  "kiosco": "Antojos",   "obj": _agua_ant},
    # Alegría
    {"img": "crispetas.png", "nombre": "Crispetas",           "precio": 2000,  "kiosco": "Alegría",   "obj": _crispetas},
    {"img": "piazas.png", "nombre": "Piazza",              "precio": 800,   "kiosco": "Alegría",   "obj": _piazas},
    {"img": "helado.png",   "nombre": "Chocomelo",           "precio": 2300,  "kiosco": "Alegría",   "obj": _chocomelo},
    {"img": "sandwich_pollo.png",    "nombre": "Sandwich pollo",      "precio": 8000,  "kiosco": "Alegría",   "obj": _sand_pol},
    {"img": "sandwich_ham.png",    "nombre": "Sandwich jamón y queso","precio":10000, "kiosco": "Alegría",   "obj": _sand_ham},
    {"img": "milo.png", "nombre": "Milo",                "precio": 10000, "kiosco": "Alegría",   "obj": _milo},
    {"img": "limonada.png", "nombre": "Limonada",            "precio": 8000,  "kiosco": "Alegría",   "obj": _limonada},
    {"img": "helado.png",   "nombre": "Helado",             "precio": 3000,  "kiosco": "Alegría",   "obj": _helado_ale},
    {"img": "natu_malta.png", "nombre": "Natumalta",          "precio": 2500,  "kiosco": "Alegría",   "obj": _natu_malta},
    {"img": "mr_tea.png", "nombre": "Mr tea",              "precio": 2200,  "kiosco": "Alegría",   "obj": _mr_tea},
    {"img": "agua.png", "nombre": "Agua",                "precio": 2000,  "kiosco": "Alegría",   "obj": _agua_ale},
    {"img": "postobon_manzana.png", "nombre": "Postobón Manzana", "precio": 3000,  "kiosco": "Alegría",   "obj": _manzana_ale},
    {"img": "postobon_uva.png", "nombre": "Postobón Uva",  "precio": 3000,  "kiosco": "Alegría",   "obj": _uva_ale},
    # Punto Fit
    {"img": "granola.png", "nombre": "Granola Tosh",             "precio": 2500,  "kiosco": "Punto Fit", "obj": _granola},
    {"img": "ensalada_frutas.png", "nombre": "Ensalada de frutas",  "precio": 6000,  "kiosco": "Punto Fit", "obj": _ens_frutas},
    {"img": "hatsu.png", "nombre": "Hatsu",               "precio": 5000,  "kiosco": "Punto Fit", "obj": _hatsu},
    {"img": "h2o.png", "nombre": "H2O",                 "precio": 2500,  "kiosco": "Punto Fit", "obj": _h2o},
    {"img": "hit_mango.png",  "nombre": "Hit Mango",        "precio": 2200,  "kiosco": "Punto Fit", "obj": _hit_mango},
    {"img": "hit_mora.png",   "nombre": "Hit Mora",         "precio": 2200,  "kiosco": "Punto Fit", "obj": _hit_mora},
    {"img": "hit_narpi.png",  "nombre": "Hit Naranja Piña", "precio": 2200,  "kiosco": "Punto Fit", "obj": _hit_narpi},
    {"img": "pepsi.png", "nombre": "Pepsi",               "precio": 3000,  "kiosco": "Punto Fit", "obj": _pepsi_fit},
    {"img": "helado.png",   "nombre": "Helado fit",          "precio": 3000,  "kiosco": "Punto Fit", "obj": _helado_fit},
    # El Asa'o
    {"img": "salchipapa.png","nombre": "Salchipapa",         "precio": 30000, "kiosco": "El Asa'o", "obj": _salchipapa},
    {"img": "pechuga_papa.png",    "nombre": "Pechuga con papa",    "precio": 20000, "kiosco": "El Asa'o", "obj": _pechuga_papa},
    {"img": "agua.png", "nombre": "Agua",                "precio": 2000,  "kiosco": "El Asa'o", "obj": _agua_asao},
    {"img": "postobon_uva.png", "nombre": "Postobón Uva",  "precio": 3000,  "kiosco": "El Asa'o", "obj": _uva_asao},
    {"img": "jugo_mora.png", "nombre": "Jugo de mora",        "precio": 2000,  "kiosco": "El Asa'o", "obj": _jugo_mora},
    {"img": "hamburguesa.png","nombre":"Hamburguesa",         "precio": 20000, "kiosco": "El Asa'o", "obj": _hamburguesa},
]

METODOS_PAGO = ["Efectivo", "Tarjeta", "PSE"]

#  ESTADO GLOBAL (integrado con backend)
class Estado:
    def __init__(self):
        # UI state
        self.carrito: list[dict] = []   # [{producto: dict_ui, cantidad: int}]
        self.historial: list[dict] = [] # [{items, total, metodo, recibo_txt}]
        self.kiosco_activo: str | None = None  # None = mostrar todos
        # Backend
        self._carrito_backend = CarritoBackend()
        self.usuario_actual = None  # instancia Estudiante o Administrador

    def agregar(self, producto: dict):
        obj = producto["obj"]
        if not INVENTARIO.verificar_disponible(obj):
            return False  # sin stock
        # UI
        for item in self.carrito:
            if item["producto"]["nombre"] == producto["nombre"]:
                item["cantidad"] += 1
                self._carrito_backend.agregar_producto(obj)
                INVENTARIO.descontar(obj, 1)
                return True
        self.carrito.append({"producto": producto, "cantidad": 1})
        self._carrito_backend.agregar_producto(obj)
        INVENTARIO.descontar(obj, 1)
        return True

    def quitar_uno(self, nombre: str):
        for item in self.carrito:
            if item["producto"]["nombre"] == nombre:
                obj = item["producto"]["obj"]
                item["cantidad"] -= 1
                # devolver al inventario
                INVENTARIO.agregar_stock(obj, 1)
                # reconstruir carrito backend quitando una instancia
                self._carrito_backend.productos.remove(obj)
                if item["cantidad"] <= 0:
                    self.carrito.remove(item)
                return

    def eliminar(self, nombre: str):
        for item in self.carrito:
            if item["producto"]["nombre"] == nombre:
                obj = item["producto"]["obj"]
                cant = item["cantidad"]
                INVENTARIO.agregar_stock(obj, cant)
                for _ in range(cant):
                    self._carrito_backend.productos.remove(obj)
        self.carrito = [i for i in self.carrito if i["producto"]["nombre"] != nombre]

    def total(self) -> int:
        return self._carrito_backend.calcular_total

    def cantidad_carrito(self) -> int:
        return sum(i["cantidad"] for i in self.carrito)

    def confirmar_pedido(self, metodo: str, dato_pago: str = "") -> tuple[bool, str]:
        """Genera orden, procesa pago y retorna (exito, texto_recibo)."""
        if not self.carrito:
            return False, "Carrito vacío."

        orden = Orden(self._carrito_backend)
        msg = orden.generar_pedido()
        if "vacío" in msg:
            return False, msg

        total = orden.total

        if metodo == "Efectivo":
            entregado = float(dato_pago) if dato_pago else total
            pago = Pago_efectivo(total, entregado)
        elif metodo == "Tarjeta":
            pago = Pago_tarjeta(total, dato_pago or "0000")
        else:  # PSE
            pago = Pago_pse(total, dato_pago or "PSE")

        orden.asignar_pago(pago)
        resultado = orden.procesar_pago()

        if "correctamente" not in resultado:
            return False, resultado

        recibo = Recibo(pago)
        recibo_txt = recibo.generar_recibo()

        self.historial.append({
            "items": list(self.carrito),
            "total": total,
            "metodo": metodo,
            "recibo_txt": recibo_txt,
        })
        self.carrito.clear()
        self._carrito_backend = CarritoBackend()
        return True, recibo_txt

    def productos_filtrados(self) -> list[dict]:
        if self.kiosco_activo is None:
            return PRODUCTOS
        return [p for p in PRODUCTOS if p["kiosco"] == self.kiosco_activo]

    def disponible(self, producto: dict) -> bool:
        return INVENTARIO.verificar_disponible(producto["obj"])


#  HELPERS DE UI
def fmt_precio(p: int) -> str:
    return f"${p:,}".replace(",", ".")


def sombra():
    return ft.BoxShadow(
        blur_radius=16,
        spread_radius=0,
        color=ft.colors.with_opacity(0.08, "black"),
        offset=ft.Offset(0, 4),
    )


def sombra_suave():
    return ft.BoxShadow(
        blur_radius=8,
        spread_radius=0,
        color=ft.colors.with_opacity(0.06, "black"),
        offset=ft.Offset(0, 2),
    )


#  COMPONENTES

def tarjeta_restaurante(img: str, nombre: str, activo: bool, on_click) -> ft.Container:
    return ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    width=64, height=64,
                    bgcolor=TAG_BG if not activo else UTB_BLUE,
                    border_radius=32,
                    alignment=ft.alignment.center,
                    content=ft.Image(
                        src=img, width=38, height=38,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    shadow=sombra_suave(),
                    border=ft.border.all(2, UTB_BLUE if activo else "transparent"),
                    animate=ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT),
                ),
                ft.Text(
                    nombre, size=11, text_align="center",
                    width=72, color=UTB_BLUE if activo else "#2563EB",
                    weight="w600" if activo else "w400",
                    max_lines=2, overflow=ft.TextOverflow.ELLIPSIS,
                ),
            ],
            horizontal_alignment="center",
            spacing=6,
        ),
        on_click=on_click,
        ink=True,
        border_radius=8,
        padding=4,
    )


def tarjeta_producto(producto: dict, on_agregar, disponible: bool = True) -> ft.Container:
    boton = ft.Container(
        content=ft.Text("Agotado", size=10, color=TEXT_GRAY, weight="w600")
        if not disponible else
        ft.Icon(ft.icons.ADD_ROUNDED, size=18, color=WHITE),
        bgcolor=TEXT_LIGHT if not disponible else ACCENT,
        border_radius=10,
        width=32, height=32,
        alignment=ft.alignment.center,
        on_click=(lambda e, p=producto: on_agregar(p)) if disponible else None,
        ink=disponible,
        shadow=ft.BoxShadow(
            blur_radius=8, color=ft.colors.with_opacity(0.3, ACCENT),
            offset=ft.Offset(0, 3)
        ) if disponible else None,
    )
    return ft.Container(
        bgcolor=CARD_BG,
        border_radius=18,
        padding=12,
        shadow=sombra(),
        opacity=1.0 if disponible else 0.55,
        content=ft.Column(
            [
                ft.Container(
                    height=90,
                    alignment=ft.alignment.center,
                    content=ft.Image(
                        src=producto["img"],
                        width=90, height=90,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                ),
                ft.Container(height=4),
                ft.Text(
                    producto["nombre"],
                    size=13, weight="bold",
                    text_align="center",
                    color=TEXT_DARK,
                    max_lines=2,
                    overflow=ft.TextOverflow.ELLIPSIS,
                ),
                ft.Container(
                    content=ft.Text(producto["kiosco"], size=10, color=WHITE if CARD_BG != "#FFFFFF" else UTB_BLUE, weight="w500"),
                    bgcolor=TAG_BG, border_radius=6,
                    padding=ft.padding.symmetric(horizontal=8, vertical=3),
                    alignment=ft.alignment.center,
                ),
                ft.Container(height=2),
                ft.Row(
                    [
                        ft.Text(
                            fmt_precio(producto["precio"]),
                            size=15, weight="bold", color=UTB_BLUE,
                        ),
                        boton,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=6,
            horizontal_alignment="center",
        ),
    )


def fila_carrito(item: dict, on_mas, on_menos, on_eliminar) -> ft.Container:
    prod = item["producto"]
    cant = item["cantidad"]
    return ft.Container(
        bgcolor=CARD_BG,
        border_radius=16,
        padding=14,
        shadow=sombra_suave(),
        content=ft.Row(
            [
                ft.Container(
                    width=56, height=56,
                    bgcolor=TAG_BG,
                    border_radius=12,
                    alignment=ft.alignment.center,
                    content=ft.Image(src=prod["img"], width=44, height=44, fit=ft.ImageFit.CONTAIN),
                ),
                ft.Column(
                    [
                        ft.Text(prod["nombre"], size=13, weight="bold", color=TEXT_DARK),
                        ft.Text(fmt_precio(prod["precio"]), size=12, color=UTB_BLUE, weight="w600"),
                    ],
                    spacing=2,
                    expand=True,
                ),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Icon(ft.icons.REMOVE_ROUNDED, size=14, color=UTB_BLUE),
                            bgcolor=TAG_BG, border_radius=8,
                            width=28, height=28,
                            alignment=ft.alignment.center,
                            on_click=lambda e, n=prod["nombre"]: on_menos(n),
                            ink=True,
                        ),
                        ft.Container(
                            content=ft.Text(str(cant), size=13, weight="bold", color=TEXT_DARK),
                            width=28,
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Icon(ft.icons.ADD_ROUNDED, size=14, color=WHITE),
                            bgcolor=UTB_BLUE, border_radius=8,
                            width=28, height=28,
                            alignment=ft.alignment.center,
                            on_click=lambda e, p=prod: on_mas(p),
                            ink=True,
                        ),
                        ft.Container(width=4),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINE_ROUNDED,
                            icon_color=DANGER, icon_size=20,
                            on_click=lambda e, n=prod["nombre"]: on_eliminar(n),
                            padding=0,
                        ),
                    ],
                    spacing=2,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


def fila_historial(pedido: dict, numero: int) -> ft.Container:
    items_txt = ", ".join(
        f"{it['cantidad']}× {it['producto']['nombre']}" for it in pedido["items"]
    )
    return ft.Container(
        bgcolor=CARD_BG,
        border_radius=16,
        padding=16,
        shadow=sombra_suave(),
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(f"#{numero}", size=12, color=WHITE, weight="bold"),
                            bgcolor=UTB_BLUE, border_radius=8,
                            padding=ft.padding.symmetric(horizontal=10, vertical=4),
                        ),
                        ft.Container(expand=True),
                        ft.Container(
                            content=ft.Text(pedido["metodo"], size=11, color=SUCCESS, weight="w600"),
                            bgcolor=ft.colors.with_opacity(0.1, SUCCESS),
                            border_radius=8,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        ),
                    ],
                ),
                ft.Container(height=6),
                ft.Text(items_txt, size=12, color=TEXT_GRAY, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                ft.Container(height=4),
                ft.Row(
                    [
                        ft.Icon(ft.icons.RECEIPT_LONG_ROUNDED, size=14, color=TEXT_LIGHT),
                        ft.Text(fmt_precio(pedido["total"]), size=14, weight="bold", color=TEXT_DARK),
                    ],
                    spacing=4,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=0,
        ),
    )


#  APP PRINCIPAL
#  USUARIOS
USUARIOS = {
    "josmoreno@utb.edu.co":  {"password": "utb2025",  "rol": "estudiante", "nombre": "Joseph",         "codigo": "T00088514"},
    "emangulo@utb.edu.co":  {"password": "utb1234",  "rol": "estudiante", "nombre": "Emmanuel",         "codigo": "T00089058"},
    "admin@utb.edu.co":   {"password": "admin123",  "rol": "admin",      "nombre": "Administrador",  "codigo": "A00000001"},
}

def main(page: ft.Page):
    page.title = "UTB Cafetería"
    page.padding = 0
    is_dark = page.platform_brightness == ft.Brightness.DARK
    set_theme(is_dark)
    page.theme_mode = ft.ThemeMode.DARK if is_dark else ft.ThemeMode.LIGHT
    page.bgcolor = BG
    page.window_width = 400
    page.window_height = 820
    page.window_resizable = False

    estado = Estado()

    badge_ref   = ft.Ref[ft.Text]()
    cuerpo_ref  = ft.Ref[ft.Column]()
    nav_ref     = ft.Ref[ft.NavigationBar]()
    snack_ref   = ft.Ref[ft.SnackBar]()
    saludo_ref  = ft.Ref[ft.Text]()

    snack = ft.SnackBar(
        ref=snack_ref,
        content=ft.Text("", color=WHITE),
        bgcolor=TEXT_DARK,
        duration=1800,
    )
    page.snack_bar = snack

    def mostrar_snack(msg: str, color: str = TEXT_DARK):
        page.snack_bar.content = ft.Text(msg, color=WHITE)
        page.snack_bar.bgcolor = color
        page.snack_bar.open = True
        page.update()

    def mostrar_dialogo_recibo(recibo_txt: str):
        lineas = recibo_txt.split("\n")
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Row(
                [
                    ft.Icon(ft.icons.RECEIPT_LONG_ROUNDED, color=SUCCESS, size=22),
                    ft.Container(width=8),
                    ft.Text("¡Pedido confirmado!", weight="bold", color=TEXT_DARK),
                ],
            ),
            content=ft.Container(
                width=300,
                content=ft.Column(
                    [
                        ft.Container(
                            bgcolor=TAG_BG,
                            border_radius=10,
                            padding=14,
                            content=ft.Column(
                                [
                                    ft.Text(
                                        ln,
                                        size=12,
                                        color=TEXT_DARK if not ln.startswith("---") else TEXT_LIGHT,
                                        weight="bold" if ln.startswith("TOTAL") or ln.startswith("RECIBO") else "w400",
                                        font_family="monospace",
                                    )
                                    for ln in lineas
                                ],
                                spacing=2,
                                tight=True,
                            ),
                        ),
                        ft.Container(height=6),
                        ft.Text(
                            "Muestra este recibo al encargado de la cafetería.",
                            size=11, color=TEXT_GRAY, text_align="center",
                        ),
                    ],
                    spacing=6,
                    tight=True,
                    scroll=ft.ScrollMode.AUTO,
                ),
            ),
            content_padding=ft.padding.symmetric(horizontal=20, vertical=16),
            actions=[
                ft.ElevatedButton(
                    "Cerrar",
                    bgcolor=UTB_BLUE, color=WHITE,
                    on_click=lambda e: page.close_dialog(),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    def badge_texto() -> str:
        n = estado.cantidad_carrito()
        return str(n) if n > 0 else ""

    metodo_seleccionado = [METODOS_PAGO[0]]

    def abrir_dialogo_pago(e):
        if not estado.carrito:
            mostrar_snack("El carrito está vacío.", DANGER)
            return

        radios = ft.RadioGroup(
            content=ft.Column(
                [ft.Radio(value=m, label=m) for m in METODOS_PAGO],
                spacing=4,
            ),
            value=metodo_seleccionado[0],
            on_change=lambda e: metodo_seleccionado.__setitem__(0, e.control.value),
        )

        resumen_items = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(f"{it['cantidad']}× {it['producto']['nombre']}", size=12, color=TEXT_GRAY, expand=True),
                        ft.Text(fmt_precio(it["producto"]["precio"] * it["cantidad"]), size=12, color=TEXT_DARK, weight="w600"),
                    ]
                )
                for it in estado.carrito
            ],
            spacing=4,
        )

        # Efectivo no necesita input: el monto es el total de la orden
        dato_extra = ft.TextField(
            label="Últimos 4 dígitos",
            hint_text="Ej: 1234",
            keyboard_type=ft.KeyboardType.NUMBER,
            border_color=UTB_BLUE,
            focused_border_color=UTB_BLUE2,
            text_size=13,
            visible=False,  # oculto por defecto (Efectivo seleccionado)
        )

        def on_metodo_change(e):
            metodo_seleccionado.__setitem__(0, e.control.value)
            m = e.control.value
            if m == "Efectivo":
                dato_extra.visible = False
            elif m == "Tarjeta":
                dato_extra.label = "Últimos 4 dígitos"
                dato_extra.hint_text = "Ej: 1234"
                dato_extra.keyboard_type = ft.KeyboardType.NUMBER
                dato_extra.visible = True
            else:  # PSE
                dato_extra.label = "Banco / plataforma"
                dato_extra.hint_text = "Ej: Bancolombia"
                dato_extra.keyboard_type = ft.KeyboardType.TEXT
                dato_extra.visible = True
            dato_extra.update()

        radios.on_change = on_metodo_change

        def confirmar(e):
            page.close_dialog()
            metodo = metodo_seleccionado[0]
            # Para efectivo el dato es el total exacto (pago exacto en kiosko)
            dato = str(estado.total()) if metodo == "Efectivo" else dato_extra.value.strip()
            exito, recibo_txt = estado.confirmar_pedido(metodo, dato)
            actualizar_todo()
            if exito:
                navegar_a(2)
                mostrar_dialogo_recibo(recibo_txt)
            else:
                mostrar_snack(f"Error: {recibo_txt}", DANGER)

        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmar pedido", weight="bold", color=TEXT_DARK),
            content=ft.Column(
                [
                    resumen_items,
                    ft.Divider(color=DIVIDER),
                    ft.Row(
                        [
                            ft.Text("Total", size=14, weight="bold", color=TEXT_DARK),
                            ft.Text(fmt_precio(estado.total()), size=16, weight="bold", color=UTB_BLUE),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Container(height=8),
                    ft.Text("Método de pago", size=13, weight="w600", color=TEXT_DARK),
                    radios,
                    ft.Container(height=4),
                    dato_extra,
                ],
                spacing=6,
                tight=True,
                width=300,
            ),
            content_padding=ft.padding.symmetric(horizontal=20, vertical=16),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: page.close_dialog()),
                ft.ElevatedButton(
                    "Confirmar",
                    bgcolor=UTB_BLUE, color=WHITE,
                    on_click=confirmar,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    #  VISTAS
    def vista_menu():
        prods = estado.productos_filtrados()

        filas_grid = []
        for i in range(0, len(prods), 2):
            par = prods[i:i+2]
            celdas = [
                ft.Container(
                    content=tarjeta_producto(p, on_agregar=agregar_producto, disponible=estado.disponible(p)),
                    col={"xs": 6},
                )
                for p in par
            ]
            if len(par) == 1:
                celdas.append(ft.Container(col={"xs": 6}))
            filas_grid.append(ft.ResponsiveRow(celdas, spacing=12))

        return ft.ListView(
            expand=True,
            controls=[
                ft.Container(
                    padding=ft.padding.only(left=20, right=20, top=16, bottom=4),
                    content=ft.Text("Kioscos", size=16, weight="bold", color=TEXT_DARK),
                ),
                ft.Container(
                    padding=ft.padding.only(left=20, right=20, bottom=10),
                    content=ft.Row(
                        [
                            tarjeta_restaurante(
                                r["img"], r["nombre"],
                                r["nombre"] == estado.kiosco_activo,
                                lambda e, r=r: cambiar_kiosco(r["nombre"]),
                            )
                            for r in KIOSCOS
                        ],
                        scroll=ft.ScrollMode.AUTO,
                        spacing=12,
                    ),
                ),
                ft.Divider(height=1, color=DIVIDER),

                ft.Container(
                    padding=ft.padding.only(left=20, right=20, bottom=8),
                    content=ft.Text("Nuestros Menús", size=16, weight="bold", color=TEXT_DARK),
                ),
                ft.Container(
                    padding=ft.padding.symmetric(horizontal=16),
                    content=ft.Column(filas_grid, spacing=12, tight=True),
                ),
                ft.Container(height=20),
            ],
            spacing=0,
            padding=0,
        )

    def vista_carrito():
        if not estado.carrito:
            return ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                content=ft.Column(
                    [
                        ft.Icon(ft.icons.SHOPPING_CART_OUTLINED, size=72, color=TEXT_LIGHT),
                        ft.Container(height=8),
                        ft.Text("Tu carrito está vacío", size=18, weight="bold", color=TEXT_DARK),
                        ft.Text("Agrega productos desde el menú", size=13, color=TEXT_GRAY),
                        ft.Container(height=16),
                        ft.ElevatedButton(
                            "Ver menú",
                            bgcolor=UTB_BLUE, color=WHITE,
                            on_click=lambda e: navegar_a(0),
                        ),
                    ],
                    horizontal_alignment="center",
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            )

        items_col = ft.ListView(
            expand=True,
            controls=[
                ft.Container(
                    padding=ft.padding.symmetric(horizontal=16, vertical=5),
                    content=fila_carrito(it, on_mas=agregar_producto, on_menos=quitar_uno, on_eliminar=eliminar_producto),
                )
                for it in estado.carrito
            ],
            spacing=0,
            padding=ft.padding.only(top=12, bottom=8),
        )

        resumen = ft.Container(
            bgcolor=CARD_BG,
            border_radius=ft.border_radius.only(top_left=24, top_right=24),
            padding=ft.padding.symmetric(horizontal=20, vertical=20),
            shadow=ft.BoxShadow(
                blur_radius=20, color=ft.colors.with_opacity(0.1, "black"),
                offset=ft.Offset(0, -4),
            ),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Subtotal", size=13, color=TEXT_GRAY),
                            ft.Text(fmt_precio(estado.total()), size=13, color=TEXT_DARK),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(
                        [
                            ft.Text("Domicilio", size=13, color=TEXT_GRAY),
                            ft.Text("Gratis", size=13, color=SUCCESS, weight="w600"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Divider(color=DIVIDER),
                    ft.Row(
                        [
                            ft.Text("Total", size=16, weight="bold", color=TEXT_DARK),
                            ft.Text(fmt_precio(estado.total()), size=18, weight="bold", color=UTB_BLUE),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Container(height=8),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.SHOPPING_CART_CHECKOUT_ROUNDED, color=WHITE, size=18),
                                ft.Text("Confirmar pedido", color=WHITE, weight="bold", size=15),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=8,
                        ),
                        bgcolor=UTB_BLUE,
                        border_radius=14,
                        padding=ft.padding.symmetric(vertical=14),
                        on_click=abrir_dialogo_pago,
                        ink=True,
                        shadow=ft.BoxShadow(
                            blur_radius=12, color=ft.colors.with_opacity(0.35, UTB_BLUE),
                            offset=ft.Offset(0, 4),
                        ),
                    ),
                ],
                spacing=10,
            ),
        )

        return ft.Column(
            [items_col, resumen],
            expand=True,
            spacing=0,
        )

    def vista_pedidos():
        if not estado.historial:
            return ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                content=ft.Column(
                    [
                        ft.Icon(ft.icons.RECEIPT_LONG_OUTLINED, size=72, color=TEXT_LIGHT),
                        ft.Container(height=8),
                        ft.Text("Sin pedidos aún", size=18, weight="bold", color=TEXT_DARK),
                        ft.Text("Tus pedidos aparecerán aquí", size=13, color=TEXT_GRAY),
                    ],
                    horizontal_alignment="center",
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            )

        return ft.ListView(
            expand=True,
            controls=[
                ft.Container(
                    padding=ft.padding.symmetric(horizontal=16, vertical=5),
                    content=fila_historial(p, len(estado.historial) - i),
                )
                for i, p in enumerate(reversed(estado.historial))
            ],
            spacing=0,
            padding=ft.padding.symmetric(vertical=12),
        )

    def vista_ajustes():
        AJUSTES_INFO = {
            "Notificaciones": (
                ft.icons.NOTIFICATIONS_OUTLINED,
                "Las notificaciones te avisarán cuando tu pedido esté listo para recoger en la cafetería.",
            ),
            "Historial": (
                ft.icons.HISTORY_ROUNDED,
                lambda: f"Llevas {len(estado.historial)} pedido(s) realizados en esta sesión.",
            ),
            "Metodos de pago": (
                ft.icons.PAYMENT_ROUNDED,
                "Puedes pagar con Efectivo, Tarjeta débito/crédito o PSE al confirmar tu pedido.",
            ),
            "Ayuda y soporte": (
                ft.icons.HELP_OUTLINE_ROUNDED,
                "Para soporte técnico o reclamos dirígete a la Oficina de Bienestar Universitario UTB, bloque A piso 2.",
            ),
            "Acerca de": (
                ft.icons.INFO_OUTLINE_ROUNDED,
                "Sistema de Auto-Pedidos UTB Cafetería\nVersión 1.0 — Proyecto POO 2025\nDesarrollado con Python + Flet.",
            ),
        }

        def abrir_info_ajuste(titulo: str):
            info = AJUSTES_INFO.get(titulo)
            if not info:
                return
            _, cuerpo = info
            texto = cuerpo() if callable(cuerpo) else cuerpo
            dlg = ft.AlertDialog(
                modal=True,
                title=ft.Row([
                    ft.Icon(info[0], color=UTB_BLUE, size=20),
                    ft.Container(width=8),
                    ft.Text(titulo, weight="bold", color=TEXT_DARK, size=15),
                ]),
                content=ft.Text(texto, size=13, color=TEXT_GRAY),
                content_padding=ft.padding.symmetric(horizontal=24, vertical=16),
                actions=[
                    ft.TextButton("Cerrar", on_click=lambda e: page.close_dialog()),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            page.dialog = dlg
            dlg.open = True
            page.update()

        def fila_ajuste(icon, titulo, subtitulo, color=TEXT_DARK):
            return ft.Container(
                bgcolor=CARD_BG,
                border_radius=14,
                padding=ft.padding.symmetric(horizontal=16, vertical=14),
                shadow=sombra_suave(),
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Icon(icon, color=color, size=22),
                            bgcolor=ft.colors.with_opacity(0.1, color),
                            border_radius=10,
                            width=40, height=40,
                            alignment=ft.alignment.center,
                        ),
                        ft.Column(
                            [
                                ft.Text(titulo, size=13, weight="w600", color=TEXT_DARK),
                                ft.Text(subtitulo, size=11, color=TEXT_GRAY),
                            ],
                            spacing=1,
                            expand=True,
                        ),
                        ft.Icon(ft.icons.CHEVRON_RIGHT_ROUNDED, color=TEXT_LIGHT, size=20),
                    ],
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ink=True,
                on_click=lambda e, t=titulo: abrir_info_ajuste(t),
            )

        card_perfil = ft.Container(
            bgcolor=CARD_BG,
            border_radius=18,
            padding=20,
            shadow=sombra(),
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(ft.icons.PERSON_ROUNDED, color=WHITE, size=32),
                        bgcolor=UTB_BLUE,
                        border_radius=30,
                        width=60, height=60,
                        alignment=ft.alignment.center,
                    ),
                    ft.Column(
                        [
                            ft.Text(estado.usuario_actual.nombre if estado.usuario_actual else "—", size=15, weight="bold", color=TEXT_DARK),
                            ft.Text(estado.usuario_actual.email if estado.usuario_actual else "—", size=12, color=TEXT_GRAY),
                            ft.Container(
                                content=ft.Text(estado.usuario_actual.codigo if estado.usuario_actual and hasattr(estado.usuario_actual, "codigo") else "—", size=10, color=UTB_BLUE, weight="w600"),
                                bgcolor=TAG_BG, border_radius=6,
                                padding=ft.padding.symmetric(horizontal=8, vertical=3),
                            ),
                        ],
                        spacing=3,
                    ),
                ],
                spacing=14,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

        return ft.ListView(
            expand=True,
            controls=[
                ft.Container(height=12),
                ft.Container(padding=ft.padding.symmetric(horizontal=16), content=card_perfil),
                ft.Container(height=4),
                ft.Container(padding=ft.padding.symmetric(horizontal=16), content=fila_ajuste(ft.icons.NOTIFICATIONS_OUTLINED, "Notificaciones", "Alertas de pedidos", UTB_BLUE)),
                ft.Container(padding=ft.padding.symmetric(horizontal=16), content=fila_ajuste(ft.icons.HISTORY_ROUNDED, "Historial", f"{len(estado.historial)} pedidos realizados", SUCCESS)),
                ft.Container(padding=ft.padding.symmetric(horizontal=16), content=fila_ajuste(ft.icons.PAYMENT_ROUNDED, "Metodos de pago", "Efectivo, Tarjeta, PSE", ACCENT)),
                ft.Container(padding=ft.padding.symmetric(horizontal=16), content=fila_ajuste(ft.icons.HELP_OUTLINE_ROUNDED, "Ayuda y soporte", "Centro de ayuda UTB", TEXT_GRAY)),
                ft.Container(padding=ft.padding.symmetric(horizontal=16), content=fila_ajuste(ft.icons.INFO_OUTLINE_ROUNDED, "Acerca de", "v1.0 - POO 2025", TEXT_GRAY)),
                ft.Container(height=20),
            ],
            spacing=10,
            padding=0,
        )

    #  LÓGICA DE NAVEGACIÓN Y ESTADO
    TITULOS = ["Menú", "Carrito", "Mis Pedidos", "Ajustes"]
    titulo_ref = ft.Ref[ft.Text]()

    def construir_vista(idx: int) -> ft.Control:
        if idx == 0:
            return vista_menu()
        elif idx == 1:
            return vista_carrito()
        elif idx == 2:
            return vista_pedidos()
        else:
            return vista_ajustes()

    def actualizar_todo():
        # Reconstruye vista activa y badge
        nav = nav_ref.current
        idx = nav.selected_index if nav and nav.selected_index is not None else 0
        if cuerpo_ref.current is not None:
            cuerpo_ref.current.controls = [construir_vista(idx)]
        if badge_ref.current is not None:
            badge_ref.current.value = badge_texto()
            badge_ref.current.visible = estado.cantidad_carrito() > 0
        page.update()

    def on_theme_change(e):
        is_dark = page.platform_brightness == ft.Brightness.DARK
        set_theme(is_dark)
        page.theme_mode = ft.ThemeMode.DARK if is_dark else ft.ThemeMode.LIGHT
        page.bgcolor = BG
        actualizar_todo()

    page.on_platform_brightness_change = on_theme_change

    def navegar_a(idx: int):
        nav_ref.current.selected_index = idx
        titulo_ref.current.value = TITULOS[idx]
        cuerpo_ref.current.controls = [construir_vista(idx)]
        badge_ref.current.value = badge_texto()
        badge_ref.current.visible = estado.cantidad_carrito() > 0
        page.update()

    def on_nav_change(e):
        idx = e.control.selected_index
        titulo_ref.current.value = TITULOS[idx]
        cuerpo_ref.current.controls = [construir_vista(idx)]
        page.update()

    def agregar_producto(producto: dict):
        exito = estado.agregar(producto)
        if exito:
            actualizar_todo()
            mostrar_snack(f"✓  {producto['nombre']} agregado", SUCCESS)
        else:
            mostrar_snack(f"⚠ {producto['nombre']} está agotado", DANGER)

    def quitar_uno(nombre: str):
        estado.quitar_uno(nombre)
        actualizar_todo()

    def eliminar_producto(nombre: str):
        estado.eliminar(nombre)
        actualizar_todo()
        mostrar_snack("Producto eliminado", DANGER)

    def cambiar_kiosco(nombre: str):
        if estado.kiosco_activo == nombre:
            estado.kiosco_activo = None   # segundo click deselecciona → mostrar todos
        else:
            estado.kiosco_activo = nombre
        actualizar_todo()

    #  LAYOUT

    # Header
    header = ft.Container(
        bgcolor=UTB_BLUE,
        padding=ft.padding.only(top=36, left=20, right=20, bottom=18),
        gradient=ft.LinearGradient(
            colors=[UTB_BLUE, UTB_BLUE2],
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
        ),
        content=ft.Row(
            [
                ft.Row(
                    [
                        ft.Image(
                            src="logo_utb.png",
                            width=80,
                            height=32,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        ft.Container(width=10),
                        ft.Column(
                            [
                                ft.Text(
                                    ref=titulo_ref,
                                    value="Menú",
                                    color=WHITE,
                                    size=18,
                                    weight="bold",
                                ),
                                ft.Text(
                                    ref=saludo_ref,
                                    value="",
                                    color=ft.colors.with_opacity(0.75, WHITE),
                                    size=11,
                                ),
                            ],
                            spacing=0,
                            tight=True,
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(expand=True),
                ft.Container(
                    content=ft.Icon(ft.icons.LOGOUT_ROUNDED, color=ft.colors.with_opacity(0.7, WHITE), size=18),
                    on_click=lambda e: cerrar_sesion(),
                    ink=True,
                    border_radius=8,
                    padding=6,
                    tooltip="Cerrar sesión",
                ),
                ft.Container(width=4),
                ft.Stack(
                    [
                        ft.IconButton(
                            icon=ft.icons.SHOPPING_CART_ROUNDED,
                            icon_color=WHITE,
                            icon_size=24,
                            on_click=lambda e: navegar_a(1),
                            padding=0,
                        ),
                        ft.Container(
                            content=ft.Text(
                                ref=badge_ref,
                                value="",
                                size=9,
                                color=WHITE,
                                weight="bold",
                            ),
                            bgcolor=ACCENT,
                            border_radius=10,
                            width=18, height=18,
                            alignment=ft.alignment.center,
                            right=0, top=0,
                            visible=False,
                        ),
                    ],
                    width=44, height=44,
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    # Cuerpo dinámico
    cuerpo = ft.Column(
        ref=cuerpo_ref,
        controls=[],
        expand=True,
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )

    # Navbar
    navbar = ft.NavigationBar(
        ref=nav_ref,
        selected_index=0,
        bgcolor=WHITE,
        indicator_color=TAG_BG,
        shadow_color=ft.colors.with_opacity(0.08, "black"),
        on_change=on_nav_change,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.RESTAURANT_MENU_OUTLINED,
                selected_icon=ft.icons.RESTAURANT_MENU_ROUNDED,
                label="Menú",
            ),
            ft.NavigationDestination(
                icon=ft.icons.SHOPPING_CART_OUTLINED,
                selected_icon=ft.icons.SHOPPING_CART_ROUNDED,
                label="Carrito",
            ),
            ft.NavigationDestination(
                icon=ft.icons.RECEIPT_LONG_OUTLINED,
                selected_icon=ft.icons.RECEIPT_LONG_ROUNDED,
                label="Pedidos",
            ),
            ft.NavigationDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS_ROUNDED,
                label="Ajustes",
            ),
        ],
    )

    # ── VISTA LOGIN ────────────────────────────────────────────────────────
    campo_correo = ft.TextField(
        label="Correo institucional",
        hint_text="usuario@utb.edu.co",
        prefix_icon=ft.icons.EMAIL_OUTLINED,
        border_color=UTB_BLUE,
        focused_border_color=UTB_BLUE2,
        text_size=13,
        keyboard_type=ft.KeyboardType.EMAIL,
        on_submit=lambda e: intentar_login(),
    )
    campo_password = ft.TextField(
        label="Contraseña",
        hint_text="••••••••",
        prefix_icon=ft.icons.LOCK_OUTLINE_ROUNDED,
        border_color=UTB_BLUE,
        focused_border_color=UTB_BLUE2,
        text_size=13,
        password=True,
        can_reveal_password=True,
        on_submit=lambda e: intentar_login(),
    )
    error_label = ft.Text("", color=DANGER, size=12, visible=False)

    def intentar_login():
        correo = campo_correo.value.strip().lower()
        password = campo_password.value

        if correo not in USUARIOS:
            error_label.value = "Correo no registrado."
            error_label.visible = True
            page.update()
            return

        u = USUARIOS[correo]
        if u["password"] != password:
            error_label.value = "Contraseña incorrecta."
            error_label.visible = True
            page.update()
            return

        if not correo.endswith("@utb.edu.co"):
            error_label.value = "Debes usar un correo @utb.edu.co."
            error_label.visible = True
            page.update()
            return

        # Instanciar clase correcta del backend
        if u["rol"] == "admin":
            estado.usuario_actual = Administrador("1", u["nombre"], correo, "1", "mañana")
        else:
            estado.usuario_actual = Estudiante("1", u["nombre"], correo, u["codigo"])

        # Resetear estado limpio para esta sesión
        estado.carrito.clear()
        estado._carrito_backend = CarritoBackend()
        estado.historial.clear()
        estado.kiosco_activo = None

        nombre = estado.usuario_actual.nombre
        page.clean()
        if isinstance(estado.usuario_actual, Administrador):
            page.add(vista_admin())
        else:
            saludo_ref.current.value = f"Hola, {nombre} 👋"
            page.add(
                ft.Column(
                    [header, cuerpo, navbar],
                    expand=True,
                    spacing=0,
                )
            )
            actualizar_todo()
        page.update()

    # ── CERRAR SESIÓN ──────────────────────────────────────────────────────
    def cerrar_sesion():
        estado.usuario_actual = None
        estado.carrito.clear()
        estado._carrito_backend = CarritoBackend()
        estado.historial.clear()
        estado.kiosco_activo = None
        campo_correo.value = ""
        campo_password.value = ""
        error_label.visible = False
        page.clean()
        page.add(vista_login)
        page.update()

    # ── VISTA ADMINISTRADOR ────────────────────────────────────────────────
    def vista_admin():
        def fila_stock(producto: dict) -> ft.Container:
            stock_actual = INVENTARIO.stock.get(producto["obj"], 0)
            cantidad_ref = [10]

            cantidad_txt = ft.Text(str(cantidad_ref[0]), size=14, weight="bold", color=UTB_BLUE, width=30, text_align="center")

            def restar(e):
                if cantidad_ref[0] > 1:
                    cantidad_ref[0] -= 1
                    cantidad_txt.value = str(cantidad_ref[0])
                    cantidad_txt.update()

            def sumar(e):
                cantidad_ref[0] += 1
                cantidad_txt.value = str(cantidad_ref[0])
                cantidad_txt.update()

            def reponer(e):
                INVENTARIO.agregar_stock(producto["obj"], cantidad_ref[0])
                nuevo_stock = INVENTARIO.stock.get(producto["obj"], 0)
                stock_lbl.value = f"Stock: {nuevo_stock}"
                stock_lbl.color = SUCCESS if nuevo_stock > 5 else DANGER
                stock_lbl.update()
                mostrar_snack(f"✓ {producto['nombre']}: +{cantidad_ref[0]} unidades", SUCCESS)

            def descontar(e):
                stock_actual = INVENTARIO.stock.get(producto["obj"], 0)
                if cantidad_ref[0] > stock_actual:
                    mostrar_snack(f"⚠ Solo hay {stock_actual} unidades de {producto['nombre']}", DANGER)
                    return
                INVENTARIO.descontar(producto["obj"], cantidad_ref[0])
                nuevo_stock = INVENTARIO.stock.get(producto["obj"], 0)
                stock_lbl.value = f"Stock: {nuevo_stock}"
                stock_lbl.color = SUCCESS if nuevo_stock > 5 else DANGER
                stock_lbl.update()
                mostrar_snack(f"✓ {producto['nombre']}: -{cantidad_ref[0]} unidades", TEXT_GRAY)

            stock_lbl = ft.Text(
                f"Stock: {stock_actual}",
                size=11,
                color=SUCCESS if stock_actual > 5 else DANGER,
                weight="w600",
            )

            return ft.Container(
                bgcolor=CARD_BG,
                border_radius=12,
                padding=ft.padding.symmetric(horizontal=14, vertical=10),
                shadow=sombra_suave(),
                content=ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text(producto["nombre"], size=13, weight="w600", color=TEXT_DARK),
                                ft.Text(producto["kiosco"], size=10, color=TEXT_GRAY),
                                stock_lbl,
                            ],
                            spacing=2,
                            expand=True,
                            tight=True,
                        ),
                        ft.Container(
                            content=ft.Icon(ft.icons.REMOVE_ROUNDED, size=16, color=UTB_BLUE),
                            width=28, height=28,
                            border_radius=8,
                            bgcolor=TAG_BG,
                            alignment=ft.alignment.center,
                            on_click=restar,
                            ink=True,
                        ),
                        cantidad_txt,
                        ft.Container(
                            content=ft.Icon(ft.icons.ADD_ROUNDED, size=16, color=WHITE),
                            width=28, height=28,
                            border_radius=8,
                            bgcolor=UTB_BLUE,
                            alignment=ft.alignment.center,
                            on_click=sumar,
                            ink=True,
                        ),
                        ft.Container(width=8),
                        ft.Container(
                            content=ft.Text("Reponer", size=11, color=WHITE, weight="w600"),
                            bgcolor=ACCENT,
                            border_radius=8,
                            padding=ft.padding.symmetric(horizontal=10, vertical=6),
                            on_click=reponer,
                            ink=True,
                        ),
                        ft.Container(
                            content=ft.Text("Quitar", size=11, color=WHITE, weight="w600"),
                            bgcolor=DANGER,
                            border_radius=8,
                            padding=ft.padding.symmetric(horizontal=10, vertical=6),
                            on_click=descontar,
                            ink=True,
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=6,
                ),
            )

        # Agrupar por kiosco
        secciones = []
        kioscos_vistos = []
        for p in PRODUCTOS:
            if p["kiosco"] not in kioscos_vistos:
                kioscos_vistos.append(p["kiosco"])

        for kiosco in kioscos_vistos:
            prods_kiosco = [p for p in PRODUCTOS if p["kiosco"] == kiosco]
            secciones.append(
                ft.Container(
                    padding=ft.padding.only(left=16, right=16, top=14, bottom=4),
                    content=ft.Text(kiosco, size=14, weight="bold", color=UTB_BLUE),
                )
            )
            for p in prods_kiosco:
                secciones.append(
                    ft.Container(
                        padding=ft.padding.symmetric(horizontal=12, vertical=3),
                        content=fila_stock(p),
                    )
                )

        secciones.append(ft.Container(height=20))

        return ft.Column(
            [
                ft.Container(
                    bgcolor=UTB_BLUE,
                    padding=ft.padding.only(top=36, left=20, right=20, bottom=18),
                    gradient=ft.LinearGradient(
                        colors=[UTB_BLUE, UTB_BLUE2],
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right,
                    ),
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.ADMIN_PANEL_SETTINGS_ROUNDED, color=WHITE, size=24),
                            ft.Container(width=10),
                            ft.Column(
                                [
                                    ft.Text("Panel Admin", size=18, weight="bold", color=WHITE),
                                    ft.Text(
                                        f"Hola, {estado.usuario_actual.nombre} 👋",
                                        size=11,
                                        color=ft.colors.with_opacity(0.75, WHITE),
                                    ),
                                ],
                                spacing=0, tight=True, expand=True,
                            ),
                            ft.Container(
                                content=ft.Icon(ft.icons.LOGOUT_ROUNDED, color=WHITE, size=20),
                                on_click=lambda e: cerrar_sesion(),
                                ink=True,
                                border_radius=8,
                                padding=6,
                                tooltip="Cerrar sesión",
                            ),
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(
                    padding=ft.padding.only(left=20, right=20, top=14, bottom=6),
                    content=ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text("Pedidos en sesión", size=12, color=TEXT_GRAY),
                                    ft.Text(
                                        f"{len(estado.historial)} pedido(s)  —  ${sum(p['total'] for p in estado.historial):,.0f} pesos",
                                        size=14, weight="bold", color=UTB_BLUE,
                                    ),
                                ],
                                spacing=1, tight=True, expand=True,
                            ),
                        ],
                    ),
                ),
                ft.Divider(height=1, color=DIVIDER),
                ft.Container(
                    padding=ft.padding.only(left=20, top=12, bottom=4),
                    content=ft.Text("Gestión de Inventario", size=15, weight="bold", color=TEXT_DARK),
                ),
                ft.ListView(
                    expand=True,
                    controls=secciones,
                    spacing=0,
                    padding=0,
                ),
            ],
            expand=True,
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        )

    vista_login = ft.Column(
        [
            ft.Container(
                expand=True,
                bgcolor=BG,
                content=ft.Column(
                    [
                        ft.Container(height=60),
                        # Logo / header
                        ft.Container(
                            padding=ft.padding.symmetric(horizontal=32),
                            content=ft.Column(
                                [
                                    ft.Container(
                                        width=80, height=80,
                                        border_radius=20,
                                        bgcolor=UTB_BLUE,
                                        alignment=ft.alignment.center,
                                        content=ft.Icon(ft.icons.RESTAURANT_MENU_ROUNDED, color=WHITE, size=40),
                                        shadow=ft.BoxShadow(blur_radius=20, color=ft.colors.with_opacity(0.3, UTB_BLUE), offset=ft.Offset(0, 8)),
                                    ),
                                    ft.Container(height=20),
                                    ft.Text("UTB Cafetería", size=26, weight="bold", color=UTB_BLUE, text_align="center"),
                                    ft.Text("Sistema de Auto-Pedidos", size=13, color=TEXT_GRAY, text_align="center"),
                                    ft.Container(height=32),
                                    campo_correo,
                                    ft.Container(height=12),
                                    campo_password,
                                    ft.Container(height=6),
                                    error_label,
                                    ft.Container(height=16),
                                    ft.ElevatedButton(
                                        text="Ingresar",
                                        width=400,
                                        height=48,
                                        bgcolor=UTB_BLUE,
                                        color=WHITE,
                                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                                        on_click=lambda e: intentar_login(),
                                    ),
                                    ft.Container(height=16),
                                    ft.Text(
                                        "Acceso exclusivo para estudiantes UTB",
                                        size=11, color=TEXT_LIGHT, text_align="center",
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=0,
                            ),
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
        ],
        expand=True,
        spacing=0,
    )

    page.add(vista_login)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")