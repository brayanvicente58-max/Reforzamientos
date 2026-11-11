from validaciones import validar_usuario

pruebas = ["abc1234", "carlos_99", "usuarioexitosomuy", "admin", "devPython2026"]

print("--- VALIDACIÓN DE USUARIOS ---")
for u in pruebas:
    resultado = validar_usuario(u)
    print(f"Usuario: '{u}' -> Resultado: {resultado}")