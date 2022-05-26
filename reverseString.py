#devolver el string dado vuelta
def reverseString(palabra):
    newString = ""
    for i in range(len(palabra)-1, -1, -1):#rango desde largo de la palabra hacia atras de uno en uno
        newString += palabra[i] #al nuevo string vamos añadiendo la nueva palabra
    return newString

print(reverseString("paralelepipedo"))
