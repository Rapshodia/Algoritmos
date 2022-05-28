#algoritmo fibonacci 

def fibonacci(num) :
    x1 = 0
    x2 = 1
    for n in range(0, num+1):#recorre desde 0 hasta el numero ingresado
        
        if n % 2 == 0:# si el numero que va recorriendo es divisible de 2
            
            print(x1)
            x1 += x2
        else:
            print(x2)
            x2 += x1

fibonacci(12)


