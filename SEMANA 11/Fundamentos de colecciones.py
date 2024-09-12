import pickle

class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __repr__(self):
        return f"Producto(ID={self.producto_id}, nombre='{self.nombre}', cantidad={self.cantidad}, precio={self.precio:.2f})"

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario con ID como clave y Producto como valor

    def añadir_producto(self, producto):
        if producto.producto_id not in self.productos:
            self.productos[producto.producto_id] = producto
        else:
            raise ValueError("El producto con este ID ya existe.")

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            del self.productos[producto_id]
        else:
            raise ValueError("El producto con este ID no existe.")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if cantidad is not None:
                producto.actualizar_cantidad(cantidad)
            if precio is not None:
                producto.actualizar_precio(precio)
        else:
            raise ValueError("El producto con este ID no existe.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if producto.nombre.lower() == nombre.lower()]
        return resultados

    def mostrar_todos_los_productos(self):
        return list(self.productos.values())

    def guardar_inventario(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'rb') as f:
                self.productos = pickle.load(f)
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará un nuevo inventario.")

# Inicialización del inventario con productos de ejemplo
def inicializar_inventario(inventario):
    productos_ejemplo = [
        Producto("001", "Laptop", 10, 999.99),
        Producto("002", "Teclado", 25, 49.99),
        Producto("003", "Ratón", 30, 29.99),
        Producto("004", "Monitor", 15, 199.99),
        Producto("005", "Impresora", 8, 149.99)
    ]
    for producto in productos_ejemplo:
        inventario.añadir_producto(producto)

# Interfaz de usuario
def menu():
    inventario = Inventario()
    inventario.cargar_inventario('inventario.pkl')

    # Inicializar con productos de ejemplo
    inicializar_inventario(inventario)

    while True:
        print("\nMenu:")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Selecciona una opción (1-7): ")

        if opcion == '1':
            producto_id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(producto_id, nombre, cantidad, precio)
            try:
                inventario.añadir_producto(producto)
                print("Producto añadido con éxito.")
            except ValueError as e:
                print(e)

        elif opcion == '2':
            producto_id = input("ID del producto a eliminar: ")
            try:
                inventario.eliminar_producto(producto_id)
                print("Producto eliminado con éxito.")
            except ValueError as e:
                print(e)

        elif opcion == '3':
            producto_id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no actualizar): ")
            precio = input("Nuevo precio (dejar en blanco para no actualizar): ")
            try:
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(producto_id, cantidad, precio)
                print("Producto actualizado con éxito.")
            except ValueError as e:
                print(e)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            productos = inventario.buscar_producto_por_nombre(nombre)
            if productos:
                print("Productos encontrados:")
                for producto in productos:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            productos = inventario.mostrar_todos_los_productos()
            if productos:
                print("Lista de todos los productos:")
                for producto in productos:
                    print(producto)
            else:
                print("No hay productos en el inventario.")

        elif opcion == '6':
            inventario.guardar_inventario('inventario.pkl')
            print("Inventario guardado con éxito.")

        elif opcion == '7':
            inventario.guardar_inventario('inventario.pkl')
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, elige entre 1 y 7.")

if __name__ == "__main__":
    menu()
