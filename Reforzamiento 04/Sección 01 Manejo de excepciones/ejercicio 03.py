persona = {
    "nombre": "Xavier",
    "apellido_paterno": "Rodriguez",
    "apellido_materno": "Gonzales",
    "dni": "63325345",
    "edad": 28,
    "correo": "xavier.rodriguez@gmail.com",
    "telefono": "987654321",
    "direccion": "Av. Los Olivos 450",
    "ciudad": "Lima",
    "profesion": "Ingeniero de Software",
    "empresa": "Tech Solutions",
    "salario": 4500.00,
    "estado_civil": "Soltero"
}

def consultar_dato(diccionario, clave):
    try:
        # Intenta acceder a la clave en el diccionario
        valor = diccionario[clave]
        print(f"Clave encontrada -> {clave}: {valor}")
    except KeyError:
        print("Error: La clave ingresada no existe en el diccionario.")

# Realizar al menos 5 consultas (3 válidas, 2 inválidas)
consultas = ["nombre", "edad", "salario", "profesion_inexistente", "telefono_emergencia"]

print("--- PRUEBAS DE CONSULTA EN DICCIONARIO ---")
for c in consultas:
    print(f"\nConsultando clave: '{c}'")
    consultar_dato(persona, c)