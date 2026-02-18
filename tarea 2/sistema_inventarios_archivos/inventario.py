# inventario.py
# Clase que gestiona la lista de productos y el archivo de inventario

from producto import Producto


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # ==========================
    # MANEJO DE ARCHIVOS
    # ==========================

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo de texto"""
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        producto = Producto(
                            datos[0],
                            datos[1],
                            int(datos[2]),
                            float(datos[3])
                        )
                        self.productos.append(producto)
        except FileNotFoundError:
            # Si el archivo no existe, se crea automáticamente
            open(self.archivo, "w").close()
        except PermissionError:
            print(" Error: No tienes permisos para acceder al archivo.")

    def guardar_en_archivo(self):
        """Guarda todos los productos en el archivo"""
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(producto.to_linea())
        except PermissionError:
            print(" Error: No se pudo escribir en el archivo.")

    # ==========================
    # OPERACIONES DEL INVENTARIO
    # ==========================

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" Error: El ID ya existe.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print(" Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print(" Producto eliminado.")
                return
        print(" Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_en_archivo()
                print(" Producto actualizado.")
                return
        print(" Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.productos
            if nombre.lower() in p.get_nombre().lower()
        ]

        if encontrados:
            for p in encontrados:
                print(f"{p.get_id()} | {p.get_nombre()} | {p.get_cantidad()} | ${p.get_precio()}")
        else:
            print(" No se encontraron productos.")

    def mostrar_productos(self):
        if not self.productos:
            print(" Inventario vacío.")
            return

        print("\nID | Nombre | Cantidad | Precio")
        print("-" * 35)
        for p in self.productos:
            print(f"{p.get_id()} | {p.get_nombre()} | {p.get_cantidad()} | ${p.get_precio()}")
