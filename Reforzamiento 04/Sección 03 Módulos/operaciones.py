import random

def generar_lista():
    return [random.randint(0, 100) for _ in range(30)]

def ordenar_lista(lista):
    # Retorna una nueva lista ordenada sin alterar la original
    return sorted(lista)

def obtener_mayor(lista):
    return max(lista)