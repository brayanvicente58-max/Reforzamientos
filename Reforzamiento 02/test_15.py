empresas_originales = ['Google', 'Microsoft', 'Amazon', 'Oracle', 'IBM']

empresas_copia = empresas_originales.copy()

empresa_extra_1 = "Google"
empresa_extra_2 = "Amazon"
empresa_extra_3 = "Meta"

empresas_copia.append(empresa_extra_1)
empresas_copia.append(empresa_extra_2)
empresas_copia.append(empresa_extra_3)

empresas_sin_duplicados = []
for empresa in empresas_copia:
    if empresa not in empresas_sin_duplicados:
        empresas_sin_duplicados.append(empresa)

elementos_eliminados = len(empresas_copia) - len(empresas_sin_duplicados)

print("Lista original:", empresas_originales)
print("Lista con nuevos elementos:", empresas_copia)
print("Lista sin duplicados:", empresas_sin_duplicados)
print("Elementos duplicados eliminados:", elementos_eliminados)