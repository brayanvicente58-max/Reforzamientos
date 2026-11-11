invitados = ['Luis', 'Ana', 'Raúl', 'Pedro', 'Miguel', 'Katherine', 'Fiorella']

impares = []
pares = []

for nombre in invitados:
    if len(nombre) % 2 != 0:
        impares.append(nombre)
    else:
        pares.append(nombre)

lista_reorganizada = impares + pares

print("Lista original:", invitados)
print("Nombres con longitud impar:", impares)
print("Nombres con longitud par:", pares)
print("Lista reorganizada:", lista_reorganizada)