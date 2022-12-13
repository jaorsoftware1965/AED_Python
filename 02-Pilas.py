# ----------------------------------------------------------------------
# Curso de Algoritmos y Estructuras de Datos en Python
# 02-Pilas
# ----------------------------------------------------------------------

# Una Pila es una estructura que almacena datos siguiendo la logica
# LIFO; First In First Out: Último en Entrar; Primero en salir; UEPS
# en Español

# El ejemplo con libros:

#             l3   <- Tope de la Pila
#       l2    l2
#  l1   l1    l1

# Métodos a implementar en la Pila
# - isEmpty. Verifica si la pila está vacía
# - clear  . Limpia la pila
# - push   . Insertar un elemento en el tope de la pila
# - size   . Tamaño de la Pila
# - peek   . Devuelve el dato en la Pila sin sacarlo
# - get    . Obtiene los elementos de la pila como lista
# - print  . Imprimir la Pila

# Definimos la Clas
class Pila:

    # Constructor
    def __init__(self):
        # Se crea una pila vacía
        self.pila = [] # Una lista de Python

    # Limpiar la Pila
    def clear(self):
        # Se limpia la pila
        self.pila.clear()

    # Verifica si está vacía
    def isEmpty(self):
        # Verifica si está vacía
        return self.pila == []

    # Meter un Elemento en la Pila
    def push(self,item):
        # Se mete el elemento
        self.pila.append(item)


    # Se saca el elemento de la Pila
    def pop(self):

        # Dato a devolver
        dato = ""

        #Verifica que no esté vacía
        if (self.isEmpty()):
            # Mensaje
            print("La pila está vacía; no es posible sacar un elemento")
        else:
            # Coloca el dato en la variabñe
            dato = self.pila.pop()

        # Retorna el dato
        return dato

    # Tamaño de la Pila
    def size(self):
        # Se crea una pila vacía
        return (len(self.pila))


    # Obtener el Elemento
    def peek(self):
        # Variable
        dato = ""

        #Verifica que no esté vacía
        if (self.isEmpty()):
            # Mensaje
            print("La pila está vacía; no es posible obtener la Cima")
        else:
            # Coloca el dato en la variabñe
            dato = self.pila[len(self.pila)-1]

    # Metodo para obtener la pila como lista
    def get(self):
        # Devuelve la lista
        return self.pila

    # Imprimir la Pila
    def print(self):
        # Imprime la Pila
        print(self.pila)

# Creamos un objeto de la Pila
p = Pila()

# Insertamos 4 elementos
p.push(10)
p.push(20)
p.push(30)
p.push(40)

# Imprimimos la pila
p.print()

# Creamos otra pila
pInv = Pila()

# Ciclo para obtener los datos originales
while (not p.isEmpty()):
    # Saca de la primer pila y mete en la segunda
    datoSacado = p.pop()
    pInv.push(datoSacado)

# Se imprime la lista invertida
pInv.print()

# Se limpia la pila 
p.clear()

# Variable
palindrome = "CIVIC"

# Ciclo para obtener las letras
for letra in palindrome:
    p.push(letra)

# imprimimos
p.print()

# Obtenemos la lista y la convertimos en cadena
cadena1 = "".join(p.get())

# Imprimimos la pila invertida
pInv.clear()


# Ciclo para obtener los datos originales
while (not p.isEmpty()):
    # Saca de la primer pila y mete en la segunda
    datoSacado = p.pop()
    pInv.push(datoSacado)

# Imprimos la lista invertida
pInv.print()

print()

# Obtenemos la lista y la convertimos en cadena
cadena2 = "".join(pInv.get())

# Verificamos si son iguales
if (cadena1 == cadena2):
   # Mensaje
   print("Si es Palindrome")
else:   
   # Mensaje
   print("No es Palindrome") 




