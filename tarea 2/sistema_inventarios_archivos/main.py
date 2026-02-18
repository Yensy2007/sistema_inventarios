# main.py
# Menú interactivo para gestionar el inventario

from inventario import Inventario
from producto import Producto


def menu():
    inventario = Inventario("inventario.txt")

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto (cantidad o precio)")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
                print(" Guardado en inventario.txt correctamente.")
            except ValueError:
                print(" Error: Cantidad debe ser entero y precio debe ser número.")

        elif opcion == "2":
            id_producto = input("Ingrese el ID a eliminar: ")
            inventario.eliminar_producto(id_producto)
            print(" Cambios guardados en inventario.txt.")

        elif opcion == "3":
            id_producto = input("Ingrese el ID a actualizar: ")

            print("¿Qué deseas actualizar?")
            print("1. Cantidad")
            print("2. Precio")
            sub_opcion = input("Opción: ")

            try:
                if sub_opcion == "1":
                    nueva_cantidad = int(input("Nueva cantidad: "))
                    inventario.actualizar_producto(id_producto, cantidad=nueva_cantidad)
                    print(" Cambios guardados en inventario.txt.")

                elif sub_opcion == "2":
                    nuevo_precio = float(input("Nuevo precio: "))
                    inventario.actualizar_producto(id_producto, precio=nuevo_precio)
                    print(" Cambios guardados en inventario.txt.")

                else:
                    print(" Opción inválida.")
            except ValueError:
                print(" Error: Ingresa valores numéricos válidos.")

        elif opcion == "4":
            nombre = input("Ingrese nombre o parte del nombre: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
