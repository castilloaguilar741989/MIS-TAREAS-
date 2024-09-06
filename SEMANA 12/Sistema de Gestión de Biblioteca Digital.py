class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor  # Utilizamos tuplas para autor y titulo
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo={self.titulo}, autor={self.autor}, categoria={self.categoria}, isbn={self.isbn})"

class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __repr__(self):
        return f"Usuario(nombre={self.nombre}, user_id={self.user_id})"

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y Libro como valor
        self.usuarios = set()  # Conjunto de IDs de usuarios únicos

    def añadir_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]

    def registrar_usuario(self, usuario):
        if usuario.user_id not in [u.user_id for u in self.usuarios]:
            self.usuarios.add(usuario)
        else:
            raise ValueError("El ID de usuario ya existe.")

    def dar_baja_usuario(self, user_id):
        self.usuarios = {u for u in self.usuarios if u.user_id != user_id}

    def prestar_libro(self, isbn, user_id):
        if isbn in self.libros_disponibles and any(u.user_id == user_id for u in self.usuarios):
            libro = self.libros_disponibles[isbn]
            usuario = next(u for u in self.usuarios if u.user_id == user_id)
            usuario.libros_prestados.append(libro)
            del self.libros_disponibles[isbn]
        else:
            raise ValueError("El libro no está disponible o el usuario no existe.")

    def devolver_libro(self, isbn, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario:
            libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
            if libro:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
            else:
                raise ValueError("El libro no está prestado por el usuario.")
        else:
            raise ValueError("El usuario no existe.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if getattr(libro, criterio, None) == valor:
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario:
            return usuario.libros_prestados
        else:
            raise ValueError("El usuario no existe.")

# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "1234567890")
    libro2 = Libro("Don Quijote", "Miguel de Cervantes", "Novela", "0987654321")

    # Crear usuarios
    usuario1 = Usuario("Juan Pérez", "u001")
    usuario2 = Usuario("Ana García", "u002")

    # Registrar usuarios y añadir libros
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    # Prestar un libro
    biblioteca.prestar_libro("1234567890", "u001")

    # Buscar libros
    print(biblioteca.buscar_libro("titulo", "Don Quijote"))

    # Listar libros prestados
    print(biblioteca.listar_libros_prestados("u001"))

    # Devolver un libro
    biblioteca.devolver_libro("1234567890", "u001")

    # Quitar un libro
    biblioteca.quitar_libro("0987654321")
