def palindromo(palabra):
    inicio = 0
    final = len(palabra)-1 # largo de la palabra

    while inicio < len(palabra)/2:
        if palabra[inicio] != palabra[final]:
            return False
        inicio += 1
        final -= 1
    return True

print(palindromo("seres"))