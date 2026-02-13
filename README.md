# Sistema de Gestión de Inventarios (POO)

Este proyecto implementa un sistema simple de inventarios para una tienda usando Programación Orientada a Objetos (POO).

## Funcionalidades
- Añadir producto (validando que el ID sea único)
- Eliminar producto por ID
- Actualizar cantidad y/o precio por ID
- Buscar producto(s) por nombre (coincidencias parciales)
- Mostrar todos los productos

## Estructura del proyecto
- `producto.py`: Clase `Producto` con atributos (id, nombre, cantidad, precio) y getters/setters.
- `inventario.py`: Clase `Inventario` que gestiona la lista de productos y las operaciones.
- `main.py`: Menú interactivo en consola para usar el sistema.

## Ejecución
1. Abrir el proyecto en PyCharm
2. Ejecutar `main.py`
