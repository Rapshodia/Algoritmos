#Funcion que recibe una palabra como string
#La funcion debe retornar un diccionario con la cantidad de letras

def cuentaLetras(palabra):
    dicc = {}
    for l in palabra:
        if l in dicc:
            dicc[l] += 1
        else:
            dicc[l] = 1
    return dicc

print(cuentaLetras("hola como estas"))