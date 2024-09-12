# Clase Libro
class Libro:
    def _init_(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla para almacenar título y autor como inmutables
        self.categoria = categoria
        self.isbn = isbn

    def _str_(self):
        return f"'{self.titulo_autor[0]}' de {self.titulo_autor[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario
class Usuario:
    def _init_(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para gestionar libros prestados

    def _str_(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"


# Clase Biblioteca
class Biblioteca:
    def _init_(self):
        self.libros_disponibles = {}  # Diccionario para almacenar libros (ISBN como clave)
        self.usuarios = {}  # Diccionario para almacenar usuarios con el ID como clave
        self.historial_prestamos = {}  # Diccionario para llevar historial de préstamos

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {libro}")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.historial_prestamos[usuario.id_usuario] = []
            print(f"Usuario registrado: {usuario}")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            del self.historial_prestamos[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros_disponibles:
            usuario = self.usuarios[id_usuario]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            self.historial_prestamos[id_usuario].append(libro)
            print(f"Libro prestado: {libro} al usuario {id_usuario}")
        else:
            print(f"Error al prestar el libro con ISBN {isbn} al usuario {id_usuario}.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and id_usuario in self.historial_prestamos:
            usuario = self.usuarios[id_usuario]
            libro = next((lib for lib in usuario.libros_prestados if lib.isbn == isbn), None)
            if libro:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                self.historial_prestamos[id_usuario].remove(libro)
                print(f"Libro devuelto: {libro} por el usuario {id_usuario}")
            else:
                print(f"El usuario no tiene prestado el libro con ISBN {isbn}.")
        else:
            print(f"Error al devolver el libro con ISBN {isbn} por el usuario {id_usuario}.")

    def buscar_libro(self, filtro, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if filtro == "titulo" and valor.lower() in libro.titulo_autor[0].lower():
                resultados.append(libro)
            elif filtro == "autor" and valor.lower() in libro.titulo_autor[1].lower():
                resultados.append(libro)
            elif filtro == "categoria" and valor.lower() == libro.categoria.lower():
                resultados.append(libro)

        if resultados:
            print(f"Resultados de búsqueda ({filtro}='{valor}'): ")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros para el {filtro}='{valor}'.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.historial_prestamos:
            libros = self.historial_prestamos[id_usuario]
            if libros:
                print(f"Libros prestados por el usuario {id_usuario}:")
                for libro in libros:
                    print(libro)
            else:
                print(f"El usuario {id_usuario} no tiene libros prestados.")
        else:
            print(f"No se encontró historial de préstamos para el usuario {id_usuario}.")


# Ejemplo de uso
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "1234567890")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "0987654321")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Carmen", "001")
biblioteca.registrar_usuario(usuario1)

# Prestar libros
biblioteca.prestar_libro("001", "1234567890")

# Listar libros prestados por un usuario
biblioteca.listar_libros_prestados("001")

# Buscar libros por título
biblioteca.buscar_libro("titulo", "principito")

# Devolver libro
biblioteca.devolver_libro("001", "1234567890")

# Listar libros prestados después de la devolución
biblioteca.listar_libros_prestados("001")