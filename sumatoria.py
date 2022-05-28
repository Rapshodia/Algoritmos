# dado un numero regresar la sumatoria de todos sus digitos

def sumatoria(numero):
    total = 0
    while numero != 0:
        ultimoDigito = numero % 10
        total += ultimoDigito
        numero = numero // 10
    return total

numero = int(input("Escribe un numero"))
print(sumatoria(numero))