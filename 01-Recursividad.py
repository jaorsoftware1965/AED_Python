# ----------------------------------------------------------------------
# Curso de Algoritmos y Estructuras de Datos en Python
# 01-Recursividad
# ----------------------------------------------------------------------

# La Recursividad es la capacidad de una función de llamarse a si misma
# Puede haber mas de una llamada recursiva dentro de la función
# Cada vez que se llama a una función recursivamente, la actual queda
# pendiente.
# Debe haber por lo menos un punto o línea de código en donde la función
# finalice, y se resuelvan todas las itereaciones pendientes.

# El factorial de un numero es el resultado de multiplicar este numero
# por sus menores; hasta el 1.
# El factorial de 0 es 1
# El factorial de 1 es 1

# !0 = 1
# !1 = 1                
# !2 = 2 x 1              !2 = 2 * !1
# !3 = 3 x 2 x 1 = 6      !3 = 3 * !2


# Función Factorial
def fnFactorial(numero):
    """Función Recursiva del Factorial de un Número"""

    # Mensaje
    print("Calculando el Factorial de:", numero)

    # Verificamos que sea 0
    if (numero == 0):
        # Acá termina la función
        print("El Factorial de: 0 es: 1")

        # Retornamos 1
        return 1

    else:
        # Obtiene el resultado llamando a la función recursivamente
        resultado = numero * fnFactorial(numero - 1)    

        # Mensaje
        print("El Factorial de:",numero, "es:",resultado)

        # Devuelve el resultado
        return resultado

# Prueba la función
fnFactorial(5)