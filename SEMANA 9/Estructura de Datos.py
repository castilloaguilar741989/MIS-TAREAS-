# Clase Producto representa cada producto en el inventario.
class Producto:
    def __init__(self, ID, nombre, cantidad, precio):
        # Inicializa los atributos de un producto.
        self.ID = ID
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getters para obtener los atributos del producto.
    def get_id(self):
        return self.ID

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos setters para actualizar los atributos del producto.
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Método para representar un producto como una cadena de texto.
    def __str__(self):
        return f"ID: {self.ID}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# Clase Inventario gestiona la lista de productos.
class Inventario:
    def __init__(self):
        # Inicializa la lista de productos y agrega algunos productos iniciales.
        self.productos = []
        self.añadir_producto(Producto("001", "Manzanas", 50, 0.30))
        self.añadir_producto(Producto("002", "Plátanos", 100, 0.25))
        self.añadir_producto(Producto("003", "Naranjas", 80, 0.40))

    # Método para añadir un nuevo producto al inventario.
    def añadir_producto(self, producto):
        # Verifica que el ID del producto sea único antes de añadirlo.
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(f"Error: Ya existe un producto con el ID {producto.get_id()}.")
                return
        self.productos.append(producto)
        print(f"Producto {producto.get_nombre()} añadido exitosamente.")

    # Método para eliminar un producto por su ID.
    def eliminar_producto(self, ID):
        # Busca el producto por ID y lo elimina de la lista.
        for producto in self.productos:
            if producto.get_id() == ID:
                self.productos.remove(producto)
                print(f"Producto con ID {ID} eliminado.")
                return
        print(f"No se encontró ningún producto con el ID {ID}.")

    # Método para actualizar la cantidad o el precio de un producto por su ID.
    def actualizar_producto(self, ID, cantidad=None, precio=None):
        # Busca el producto por ID y actualiza la cantidad y/o precio.
        for producto in self.productos:
            if producto.get_id() == ID:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print(f"Producto con ID {ID} actualizado.")
                return
        print(f"No se encontró ningún producto con el ID {ID}.")

    # Método para buscar productos por su nombre.
    def buscar_producto(self, nombre):
        # Realiza una búsqueda parcial por nombre (case-insensitive).
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print(f"Productos encontrados con el nombre '{nombre}':")
            for producto in resultados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    # Método para mostrar todos los productos en el inventario.
    def mostrar_productos(self):
        # Imprime todos los productos en el inventario.
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("Productos en inventario:")
            for producto in self.productos:
                print(producto)


# Función que define el menú de la interfaz de usuario.
def menu():
    inventario = Inventario()

    while True:
        # Menú de opciones para el usuario.
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto por ID")
        print("4. Buscar productos por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        # Opciones del menú y acciones correspondientes.
        if opcion == "1":
            ID = input("Ingresa el ID del producto: ")
            nombre = input("Ingresa el nombre del producto: ")
            cantidad = int(input("Ingresa la cantidad del producto: "))
            precio = float(input("Ingresa el precio del producto: "))
            producto = Producto(ID, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            ID = input("Ingresa el ID del producto a eliminar: ")
            inventario.eliminar_producto(ID)

        elif opcion == "3":
            ID = input("Ingresa el ID del producto a actualizar: ")
            cantidad = input("Ingresa la nueva cantidad (o presiona Enter para omitir): ")
            precio = input("Ingresa el nuevo precio (o presiona Enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(ID, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingresa el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            # Opción para salir del programa.
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


# Punto de entrada principal del programa.
if __name__ == "__main__":
    # Inicia el menú interactivo.
    menu()
