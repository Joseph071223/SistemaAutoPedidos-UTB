# UTB Cafetería — Sistema de Auto-Pedidos

Aplicación de escritorio desarrollada con Python y Flet para la gestión de pedidos en la cafetería de la Universidad Tecnológica de Bolívar.

## Descripción

Sistema que permite a los estudiantes realizar pedidos desde los diferentes kioscos de la cafetería (El Asa'o, Punto Fit, Alegría, Antojos), gestionar su carrito de compras y confirmar el pago. Incluye un panel de administrador para gestión de inventario en tiempo real.

## Tecnologías

- Python 3.10+
- Flet 0.22.1 (interfaz gráfica)
- Programación Orientada a Objetos

## Estructura del proyecto

```
SistemaAutoPedidos/
├── Interfaz.py              # Interfaz gráfica principal
├── assets/                  # Imágenes de productos
└── proyecto/
    └── core/
        ├── productos/
        │   ├── productos.py
        │   ├── alimento.py
        │   └── bebida.py
        ├── gestion_pedidos/
        │   ├── carrito.py
        │   ├── orden.py
        │   └── recibo.py
        ├── pagos/
        │   └── pagos.py
        ├── inventario.py
        └── usuarios.py
```

## Instalación

### Windows (PowerShell)
```bash
python -m venv venv
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python Interfaz.py
```

### macOS/Linux
```bash
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python Interfaz.py
```

## Credenciales de prueba

| Correo | Contraseña | Rol |
|--------|------------|-----|
| josmoreno@utb.edu.co | utb2025 | Estudiante |
| emangulo@utb.edu.co | utb1234 | Estudiante |
| admin@utb.edu.co | admin123 | Administrador |

## Funcionalidades

**Estudiante**
- Explorar productos por kiosco (El Asa'o, Punto Fit, Alegría, Antojos)
- Agregar y quitar productos del carrito
- Pagar con Efectivo, Tarjeta o PSE
- Ver historial de pedidos de la sesión
- Recibo detallado al confirmar el pedido

**Administrador**
- Gestión de inventario en tiempo real
- Reponer y descontar stock por producto
- Ver resumen de pedidos y total recaudado en la sesión

## Autores

| Nombre | Código |
|--------|--------|
| Joseph Alexander Moreno Hernandez | T00088514 |
| Emmanuel David Angulo Gonzalez | T00089058 |

Universidad Tecnológica de Bolívar  
Programación Orientada a Objetos — NRC 1955  
2026
