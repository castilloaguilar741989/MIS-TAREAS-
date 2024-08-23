import os

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as f:
                    for linea in f:
                        try:
                            nombre, cantidad = linea.strip().split(',')
                            self.productos[nombre] = int(cantidad)
                        except ValueError:
                            print(f"Formato de línea incorrecto: {linea.strip()}")
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error al leer el archivo: {e}")
        else:
            self.crear_archivo_vacio()

    def crear_archivo_vacio(self):
        """Crea un archivo vacío si no existe uno."""
        try:
            with open(self.archivo, 'w') as f:
                pass  # Solo se necesita crear el archivo vacío
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al crear el archivo: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo."""
        try:
            with open(self.archivo, 'w') as f:
                for nombre, cantidad in self.productos.items():
                    f.write(f"{nombre},{cantidad}\n")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al escribir en el archivo: {e}")

    def agregar_producto(self, nombre, cantidad):
        """Agrega un producto o actualiza la cantidad si ya existe."""
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        self.guardar_inventario()
        print(f"Producto '{nombre}' agregado/actualizado exitosamente.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            print(f"El producto '{nombre}' no se encuentra en el inventario.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for nombre, cantidad in self.productos.items():
                print(f"{nombre}: {cantidad}")

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\nGestión de Inventario")
        print("1. Agregar/Actualizar Producto")
        print("2. Eliminar Producto")
        print("3. Mostrar Inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                inventario.agregar_producto(nombre, cantidad)
            except ValueError:
                print("Por favor, ingrese una cantidad válida.")
        elif opcion == '2':
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == '3':
            inventario.mostrar_inventario()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
