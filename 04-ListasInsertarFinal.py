# ----------------------------------------------------------------------
# Curso de Algoritmos y Estructuras de Datos en Python
# 04-Listas Vinculadas Insertar al Final
# ----------------------------------------------------------------------

# En esta clase agregaremos el método de insertar al final
# - insertar.      Inserta un nodo en la cabeza
# - insertarFinal. Inserta un nodo al final
# - longitud.      Obtiene el numero de Elementos de la Lista
# - imprimir.      Imprimir la lista

# Para insertar un nodo al final
# a) Crear el Nuevo nodo
# b) Si la lista está vacía, el elemento se inserta en la cabeza
# c) Si no está la lista vacía, se debe recorrer hasta encontrar el
#    ultimo nodo, el cual su apuntador siguiente esté apuntando a None
# d) Hacer que el ultimo nodo apunte al nuevo nodo


# Graficamente cuando la lista vacía
#    
# cabeza  Insertamos 7   cabeza     Insertamos 5   cabeza
#   |     al final          |       al final         |       
#  None                     7->None                  7->5->
#


# definimos la Clase
class Nodo:

    # Constructor
	def __init__(self, dato):
		
        ## información del nodo
		self.dato = dato

		## apuntador a siguiente
		self.sgte = None


# Definimos la Clase Lista
class Lista:

    # Constructor
    def __init__(self):
		
        # Definimos el apuntador a cabeza
        self.cabeza = None

		# nodos
        self.nodos  = 0


    # Insertar un elemento en la lista
    def insertar(self, dato):
            
        # Creamos un nuevo nodo
        nvoNodo = Nodo(dato)

        # El Nuevo Elemento debe apuntar a donde apunta cabeza
        nvoNodo.sgte = self.cabeza

        # Cabeza apunta al nuevo elemento
        self.cabeza = nvoNodo

        # Incrementamos el Contador de Elementos
        self.nodos = self.nodos + 1

    # Insertar un elemento en la lista al Final
    def insertarFinal(self, dato):
            
        # Creamos un nuevo nodo
        nvoNodo = Nodo(dato)

        # Verifica si la lista está vacía
        if (self.cabeza is None):
            # Hacemos que la cabeza apunte al nuevo nodo
            self.cabeza = nvoNodo
        else:
            # Obtenemos un apuntador temporal con la cabeza
            ptrTmp = self.cabeza

            # Ciclo para buscar el ultimo nodo
            while (not ptrTmp.sgte is None):
                # Se mueve al siguiente
                ptrTmp = ptrTmp.sgte

            # El ultimo nodo apunta al nuevo
            ptrTmp.sgte = nvoNodo

        # Incrementamos el contador de nodos
        self.nodos = self.nodos + 1        

                

    # Método para la longitud
    def longitud(self):

        # Retorna
        return self.nodos


    # Imprimir un elemento en la Lista
    def imprimir(self):

        ## variable temporal para recorrer los nodos
        ptrTmp = self.cabeza

        # Imprimimos lista
        print("Lista["+str(self.nodos)+"]",end="->")

        # Recorrido de la Lista
        while not ptrTmp is None:
            
            # Se imprime el dato
            print(ptrTmp.dato, end='->')

            # Desplazamos al siguiente nodo
            ptrTmp = ptrTmp.sgte

        # Imprime null al final
        print('None')

    

# Creamos una lista
lista = Lista()

# Desplegamos la lista
# lista.imprimir()


# # Insertamos varios elementos
lista.insertarFinal("Al final 1")
lista.insertar(10)
lista.insertar("Hola")
lista.insertar(3.1416)
lista.insertar(True)
lista.insertarFinal("Al final 2")


# Desplegamos la longitud
print("Longitud:",lista.longitud())

# Desplegamos la lista
lista.imprimir()



# class Test:
#     def __del__(self):
#         print("He sido destruido...")

# foo = Test()
# bar = foo
# bar = 5
# del foo # ¿No pasa nada?
# bar = "Hola"

          
