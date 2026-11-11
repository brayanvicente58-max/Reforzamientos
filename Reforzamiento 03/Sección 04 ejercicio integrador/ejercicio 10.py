class Agenda:
    # Estructura interna: Lista de diccionarios
    def __init__(self):
        self.contactos = []

    # Método para agregar contacto (validando DNI único)
    def agregar_contacto(self, nombre: str, telefono: str, email: str, dni: str) -> bool:
        for c in self.contactos:
            if c["dni"] == dni:
                print(f"[ERROR] El DNI {dni} ya pertenece a otro contacto ({c['nombre']}).")
                return False

        nuevo_contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "email": email,
            "dni": dni
        }
        self.contactos.append(nuevo_contacto)
        print(f"Contacto '{nombre}' agregado exitosamente.")
        return True

    # Método para mostrar todos los contactos registrados
    def mostrar_contactos(self):
        print("\n--- LISTA DE CONTACTOS EN LA AGENDA ---")
        if not self.contactos:
            print("La agenda está vacía.")
            return

        for idx, c in enumerate(self.contactos, 1):
            print(f"{idx}. {c['nombre']} | Tel: {c['telefono']} | Email: {c['email']} | DNI: {c['dni']}")

    # Método para buscar por DNI
    def buscar_por_dni(self, dni: str):
        print(f"\nBuscando DNI: {dni}...")
        for c in self.contactos:
            if c["dni"] == dni:
                print(f"[ENCONTRADO] Nombre: {c['nombre']} | Teléfono: {c['telefono']} | Email: {c['email']}")
                return c
        print(f"[NO ENCONTRADO] No existe ningún contacto con el DNI {dni}.")
        return None


# Pruebas solicitadas
mi_agenda = Agenda()

# Agregar al menos 3 contactos
mi_agenda.agregar_contacto("Andrea Torres", "987654321", "andrea@email.com", "71234567")
mi_agenda.agregar_contacto("Bruno Díaz", "912345678", "bruno@email.com", "78901234")
mi_agenda.agregar_contacto("Carla Ríos", "955544332", "carla@email.com", "74567890")

# Intentar duplicar DNI
mi_agenda.agregar_contacto("Clon", "000000000", "clon@email.com", "71234567")

# Mostrar agenda completa
mi_agenda.mostrar_contactos()

# Dos búsquedas: una existente y una inexistente
mi_agenda.buscar_por_dni("78901234")  # Existente
mi_agenda.buscar_por_dni("99999999")  # Inexistente