# ----------------------------------------------------------------------
# Curso de Algoritmos y Estructuras de Datos en Python
# 03-Listas Vinculadas
# ----------------------------------------------------------------------

# En Python, a la estructura Lista, se le agrega el adjetivo vinculada para
# poder diferenciarla del objeto Lista del Lenguaje.

# Una Lista Vinculada es una Estructura Lineal, que almacena objetos llamados
# Nodos, los cuales contienen información y por lo menos un puntero que lo
# enlaza hacia otro nodo

# Los Nodos son creados dinámicamente en tiempo de ejecución y por lo tanto
# al ser un manejo de memoria dinámica, la información no se encuentra en
# memoria contigua.

# Las Listas pueden enlazarse con un solo apuntador, para lo cual son llamadas
# listas simples. Este apuntador enlaza con el siguiente nodo.

# Existen Listas llamadas dobles, las cuales contienen un apuntador hacia el
# siguiente nodo; y otro apuntador al nodo anterior.

# En estas primeras clases estudiaremos las Listas con un solo apuntador; el
# siguiente.

# Al primer nodo de la Lista se le conoce como cabeza.

# La Lista debe de contener un apuntador llamado Header o Cabeza el cual
# siempre apunta al primer nodo de la lista.

# Cada vez que se inserta un NUEVO NODO a la lista, este se inserta en la 
# cabeza

# En esta clase veremos los métodos
# - insertar. Inserta un nodo en la cabeza
# - longitud. Obtiene el numero de nodos de la Lista
# - imprimir. Imprimir la lista

# Para insertar un elemento se sigue lo siguiente.
# a) Se crea el Nuevo Nodo
# b) El Nuevo Nodo apunta al nodo al que apunta cabeza
# c) Cabeza apunta al nuevo nodo


# Graficamente cuando la lista vacía
#    
# cabeza  Insertamos 7   cabeza    Insertamos 5   cabeza
#   |                       |                        |       
#  None                     7->None                  5->7->None
#

# Definimos la Clase Nodo
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
        self.cabeza    = None

		# nodos
        self.nodos     = 0


    # Insertar un elemento en la lista
    def insertar(self, dato):
            
        # Creamos un nuevo nodo
        nvoNodo = Nodo(dato)

        # El Nuevo Elemento debe apuntar a donde apunta cabeza
        nvoNodo.sgte = self.cabeza

        # Cabeza apunta al nuevo elemento
        self.cabeza = nvoNodo

        # Incrementamos el Contador de Nodos
        self.nodos = self.nodos + 1

    # Método para la longitud
    def longitud(self):

        # Retorna
        return self.nodos


    # Imprimir  la Lista
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
lista.imprimir()


# Insertamos varios elementos
lista.insertar(10)
lista.insertar("Hola")
lista.insertar(3.1416)
lista.insertar(True)

# Desplegamos la longitud
print("Longitud:",lista.longitud())

# Desplegamos la lista
lista.imprimir()

x = 10
y = x  # Si estoy creando un nuevo objeto INT

print(x)
print(y)
print()

x = 9
print(x)
print(y)
print()

x = Nodo(10)
y = x # NO Estoy creando un nuevo objeto NODO, lo apunto

print(x.dato)
print(y.dato)

x.dato = 9
print(x.dato)
print(y.dato)





