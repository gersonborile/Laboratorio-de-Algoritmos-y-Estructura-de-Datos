#ejercicio 1

def devolver_distintos(a,b,c):
    suma= a+b+c

    if suma>15:
        return max(a,b,c)
    elif suma<10:
        return min(a,b,c)
    else:
        if (a > b and a < c) or (a < b and a > c):
            return a
        elif (b > a and b < c) or (b < a and b > c):
            return b
        else:
            return c

#ejercicio 2

def funcion(palabra):
   
    letras = set(palabra)
   
    letras_ordenadas = sorted(letras)
    return letras_ordenadas



#ejercicio 3

def funcion(*args):
    for i in range(1, len(args)):
        if args[i] == 0 and args[i - 1] == 0:
            return True
    return False


#ejercicio 4 

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(num):
    cantidad_primos = 0
    for i in range(num + 1):
        if es_primo(i):
            print(i)  
            cantidad_primos += 1
    return cantidad_primos

