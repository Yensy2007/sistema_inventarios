# producto.py
# Clase Producto

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Para guardar en archivo
    def to_linea(self):
        return f"{self.__id},{self.__nombre},{self.__cantidad},{self.__precio}\n"

    # Mostrar bonito
    def __str__(self):
        return f"ID: {self.__id} | {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio}"
