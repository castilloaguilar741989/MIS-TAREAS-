import json


# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        for producto in resultados:
            print(producto)

    def mostrar_todos_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id_producto: vars(producto) for id_producto, producto in self.productos.items()}, f)

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                self.productos = {id_producto: Producto(**info) for id_producto, info in datos.items()}
        except FileNotFoundError:
            print("El archivo no existe.")


# Función de menú
def menu():
    inventario = Inventario()
    archivo = 'inventario.json'
    inventario.cargar_desde_archivo(archivo)

    while True:
        print("\nMenu:")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Todos los Productos")
        print("6. Guardar y Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id_producto, cantidad=int(cantidad) if cantidad else None,
                                           precio=float(precio) if precio else None)
        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_todos_productos()
        elif opcion == '6':
            inventario.guardar_en_archivo(archivo)
            print("Inventario guardado. Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
