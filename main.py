from core.menu import Menu
from core.usuarios import Administrador, Estudiante
from core.productos.alimento import Alimento
from core.productos.bebida import Bebida
from core.gestion_pedidos.carrito import Carrito
from core.gestion_pedidos.orden import Orden
from core.gestion_pedidos.recibo import Recibo
from core.pagos.pagos import Pago_efectivo
from core.inventario import Inventario


def main():
    admin = Administrador("A01", "testadmin", "testadmin@utb.edu.co", "senior", "mañana")
    estudiante = Estudiante("E01", "Emmanuel", "emangulo@utb.edu.co", "T00089058")

    menu_utb = Menu("Antojos")

    ecmo = Alimento("Snack", "Empanada de carne molida", 5000, 250)
    jugo = Bebida("Jugo de mango", 3200, 600)

    print(admin.gestionar_menu("agregar", "Antojos", ecmo))
    print(admin.gestionar_menu("agregar", "Antojos", jugo))
    print(admin.gestionar_menu("ver", "Antojos"))

    inventario = Inventario()
    inventario.agregar_stock(ecmo, 10)
    inventario.agregar_stock(jugo, 8)

    carrito = Carrito()
    carrito.agregar_producto(ecmo)
    carrito.agregar_producto(jugo)
    carrito.info_carrito()

    orden = Orden(carrito)
    print(orden.generar_pedido())

    pago = Pago_efectivo(orden.total, 20000)
    print(orden.asignar_pago(pago))
    print(orden.procesar_pago())

    recibo = Recibo(pago)
    print(recibo.generar_recibo())

    estudiante.historial.append(recibo.generar_recibo())
    print("\nHistorial del estudiante:")
    print(estudiante.ver_historial())


if __name__ == "__main__":
    main()