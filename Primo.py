def numeroPrimo(num):
    for x in range(2, num):
        if(num % 2 ==0): #si el numero ingresado al dividirlo por 2 el resto es 0 significaque es divisible por si mismo por uno y por 2 eso returna false
            return False
        else:
            return True

print(numeroPrimo(7))