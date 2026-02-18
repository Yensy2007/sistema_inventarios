from producto import Producto
from inventario import Inventario


def leer_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(" Error: ingresa un número entero válido.")


def leer_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(" Error: ingresa un número válido (ej: 10.50).")


def mostrar_menu():
    print("\n===== SISTEMA DE GESTIÓN DE INVENTARIOS =====")
    print("1) Añadir producto")
    print("2) Eliminar producto por ID")
    print("3) Actualizar producto")
    print("4) Buscar producto por nombre")
    print("5) Mostrar todos los productos")
    print("0) Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            print("\n--- Añadir producto ---")
            id_p = input("ID (único): ").strip()
            nombre = input("Nombre: ").strip()
            cantidad = leer_int("Cantidad: ")
            precio = leer_float("Precio: ")

            producto = Producto(id_p, nombre, cantidad, precio)
            if inventario.anadir_producto(producto):
                print(" Producto añadido correctamente.")
            else:
                print(" Error: el ID ya existe.")

        elif opcion == "2":
            print("\n--- Eliminar producto ---")
            id_p = input("ID a eliminar: ").strip()
            if inventario.eliminar_por_id(id_p):
                print(" Producto eliminado.")
            else:
                print(" Producto no encontrado.")

        elif opcion == "3":
            print("\n--- Actualizar producto ---")
            id_p = input("ID a actualizar: ").strip()
            cantidad = leer_int("Nueva cantidad: ")
            precio = leer_float("Nuevo precio: ")
            if inventario.actualizar_por_id(id_p, cantidad, precio):
                print(" Producto actualizado.")
            else:
                print(" Producto no encontrado.")

        elif opcion == "4":
            print("\n--- Buscar producto ---")
            texto = input("Texto a buscar: ").strip()
            resultados = inventario.buscar_por_nombre(texto)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print(" No se encontraron productos.")

        elif opcion == "5":
            print("\n--- Inventario completo ---")
            productos = inventario.obtener_todos()
            if not productos:
                print(" Inventario vacío.")
            else:
                for p in productos:
                    print(p)

        elif opcion == "0":
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción inválida.")


if __name__ == "__main__":
    main()
