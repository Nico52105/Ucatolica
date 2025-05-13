class Biblioteca:
    def __init__(self):
        self.libros = []
        self.lectores = []
        self.empleados = []

    def menu_principal(self):
        while True:
            print("\n--- SISTEMA DE BIBLIOTECA ---")
            print("1. Gestión de Libros")
            print("2. Gestión de Lectores")
            print("3. Gestión de Empleados")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.gestion_libros()
            elif opcion == "2":
                self.gestion_lectores()
            elif opcion == "3":
                self.gestion_empleados()
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def gestion_libros(self):
        while True:
            print("\n--- GESTIÓN DE LIBROS ---")
            print("1. Agregar Libro")
            print("2. Consultar Libros")
            print("3. Actualizar Libro")
            print("4. Eliminar Libro")
            print("5. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_libro()
            elif opcion == "2":
                self.consultar_libros()
            elif opcion == "3":
                self.actualizar_libro()
            elif opcion == "4":
                self.eliminar_libro()
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def agregar_libro(self):
        print("\n--- AGREGAR LIBRO ---")
        id_libro = input("ID del Libro: ")
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        anio = input("Año: ")
        cantidad = int(input("Cantidad: "))

        libro = {
            "id": id_libro,
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "anio": anio,
            "cantidad": cantidad
        }
        self.libros.append(libro)
        print("Libro agregado exitosamente.")

    def consultar_libros(self):
        print("\n--- CONSULTAR LIBROS ---")
        if not self.libros:
            print("No hay libros registrados.")
        else:
            for libro in self.libros:
                print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}, Año: {libro['anio']}, Cantidad: {libro['cantidad']}")

    def actualizar_libro(self):
        print("\n--- ACTUALIZAR LIBRO ---")
        id_libro = input("Ingrese el ID del libro a actualizar: ")
        for libro in self.libros:
            if libro["id"] == id_libro:
                print("Libro encontrado. Ingrese los nuevos datos:")
                libro["titulo"] = input("Nuevo Título: ")
                libro["autor"] = input("Nuevo Autor: ")
                libro["genero"] = input("Nuevo Género: ")
                libro["anio"] = input("Nuevo Año: ")
                libro["cantidad"] = int(input("Nueva Cantidad: "))
                print("Libro actualizado exitosamente.")
                return
        print("Libro no encontrado.")

    def eliminar_libro(self):
        print("\n--- ELIMINAR LIBRO ---")
        id_libro = input("Ingrese el ID del libro a eliminar: ")
        for libro in self.libros:
            if libro["id"] == id_libro:
                self.libros.remove(libro)
                print("Libro eliminado exitosamente.")
                return
        print("Libro no encontrado.")

    def gestion_lectores(self):
        while True:
            print("\n--- GESTIÓN DE LECTORES ---")
            print("1. Agregar Lector")
            print("2. Consultar Lectores")
            print("3. Eliminar Lector")
            print("4. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_lector()
            elif opcion == "2":
                self.consultar_lectores()
            elif opcion == "3":
                self.eliminar_lector()
            elif opcion == "4":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def agregar_lector(self):
        print("\n--- AGREGAR LECTOR ---")
        id_lector = input("ID del Lector: ")
        nombre = input("Nombre: ")
        libros_prestados = int(input("Libros Prestados: "))
        multas = int(input("Número de Multas: "))
        deuda = float(input("Deuda Acumulada: "))

        lector = {
            "id": id_lector,
            "nombre": nombre,
            "libros_prestados": libros_prestados,
            "multas": multas,
            "deuda": deuda
        }
        self.lectores.append(lector)
        print("Lector agregado exitosamente.")

    def consultar_lectores(self):
        print("\n--- CONSULTAR LECTORES ---")
        if not self.lectores:
            print("No hay lectores registrados.")
        else:
            for lector in self.lectores:
                print(f"ID: {lector['id']}, Nombre: {lector['nombre']}, Libros Prestados: {lector['libros_prestados']}, Multas: {lector['multas']}, Deuda: {lector['deuda']}")

    def eliminar_lector(self):
        print("\n--- ELIMINAR LECTOR ---")
        id_lector = input("Ingrese el ID del lector a eliminar: ")
        for lector in self.lectores:
            if lector["id"] == id_lector:
                self.lectores.remove(lector)
                print("Lector eliminado exitosamente.")
                return
        print("Lector no encontrado.")

    def gestion_empleados(self):
        while True:
            print("\n--- GESTIÓN DE EMPLEADOS ---")
            print("1. Agregar Empleado")
            print("2. Consultar Empleados")
            print("3. Eliminar Empleado")
            print("4. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_empleado()
            elif opcion == "2":
                self.consultar_empleados()
            elif opcion == "3":
                self.eliminar_empleado()
            elif opcion == "4":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def agregar_empleado(self):
        print("\n--- AGREGAR EMPLEADO ---")
        id_empleado = input("ID del Empleado: ")
        nombre = input("Nombre: ")
        cargo = input("Cargo: ")
        turno = input("Turno: ")

        empleado = {
            "id": id_empleado,
            "nombre": nombre,
            "cargo": cargo,
            "turno": turno
        }
        self.empleados.append(empleado)
        print("Empleado agregado exitosamente.")

    def consultar_empleados(self):
        print("\n--- CONSULTAR EMPLEADOS ---")
        if not self.empleados:
            print("No hay empleados registrados.")
        else:
            for empleado in self.empleados:
                print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Cargo: {empleado['cargo']}, Turno: {empleado['turno']}")

    def eliminar_empleado(self):
        print("\n--- ELIMINAR EMPLEADO ---")
        id_empleado = input("Ingrese el ID del empleado a eliminar: ")
        for empleado in self.empleados:
            if empleado["id"] == id_empleado:
                self.empleados.remove(empleado)
                print("Empleado eliminado exitosamente.")
                return
        print("Empleado no encontrado.")


if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.menu_principal()