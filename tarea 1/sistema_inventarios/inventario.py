from producto import Producto


class Inventario:
    """
    Clase que gestiona una lista de productos.
    """

    def __init__(self):
        self.__productos = []

    def __existe_id(self, id_producto):
        for p in self.__productos:
            if p.get_id() == id_producto:
                return True
        return False

    def anadir_producto(self, producto):
        if self.__existe_id(producto.get_id()):
            return False
        self.__productos.append(producto)
        return True

    def eliminar_por_id(self, id_producto):
        for i, p in enumerate(self.__productos):
            if p.get_id() == id_producto:
                del self.__productos[i]
                return True
        return False

    def actualizar_por_id(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.__productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                return True
        return False

    def buscar_por_nombre(self, texto):
        texto = texto.lower()
        resultados = []
        for p in self.__productos:
            if texto in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def obtener_todos(self):
        return list(self.__productos)
