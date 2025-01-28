#recursividad
#1. caso base: es la condición que detiene la recursividad, sin un caso base, 
# la función se estaría llamando a si misma indefinidamente.
#2. caso recursivo: es la llamada a la función dentro de la misma función.

#El factorial de un número n es el producto de todos los números enteros
#desde 1 hasta n positivos

# 5! = 5*4*3*2*1 = 120
# Solucion iterativa= (sin recursividad) 

def factorial_iteraivo(n):
    resultado=1
    for a in range (1,n+1):
        resultado*=a #resultado=resultado*i
        print(resultado)
    #print(f"El factorial de {n} es {resultado}")
factorial_iteraivo(5)

# Solucion recursiva= (sin recursividad) 

def factorial_recursivo(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_recursivo(n-1)
print(factorial_recursivo(5))
                                    
    