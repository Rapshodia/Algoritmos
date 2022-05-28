#Funcion regresa cuantas veces se encuentra la palabra en la frase

def encuentraPalabra(arreglo, palabra):
    cont = 0
    for p in arreglo:
        if p == palabra:
            cont += 1
    return cont

arreglo = ["hola", "como", "estas", "me", "gusta", "programar", "tambien", "me", "gusta", "jugar"]
print(encuentraPalabra(arreglo, "me"))