# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial (n-1)
    
print (factorial(6))

