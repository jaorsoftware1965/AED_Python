# ----------------------------------------------------------------------
# Curso de Algoritmos y Estructuras de Datos en Python
# 06-Listas Vinculadas Insertar por Posición
# ----------------------------------------------------------------------

# En esta clase agregaremos el método de insertar por posicion
# Consideraciones
# La posición debe existir
# El Dato que se encuentra en la posición será desplazado a la derecha


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

    # Insertar un elemento en la lista al Final Recursivamente
    def insertarFinalRecursivamente(self, nodo, dato):

        # Verico que exista el nodo
        if (nodo is None):
            # Creamos el Nodo
            nvoNodo = Nodo(dato)

            # Lo ponemos en la cabeza
            self.cabeza = nvoNodo

            # Incremewntamos el contador
            self.nodos = self.nodos + 1
        else:            
            # Verifica si tiene siguiente
            if (nodo.sgte is None):
                # Creo el Nuevo Nodo
                nvoNodo = Nodo(dato)

                # Hacemos que su siguiente apunte al nuevo nodo
                nodo.sgte = nvoNodo

                # Incrementamos el contador de nodos
                self.nodos = self.nodos + 1                            
            else:
                # Llamo recursivamente a la función
                self.insertarFinalRecursivamente(nodo.sgte,dato)            
    
    # Método para insertar por posición
    def insertarPorPosicion(self,dato,posicion):
        # Verificamos que la posición sea válida
        if (posicion <=self.nodos and posicion >0):
        
            # Obtengo el nodo actual
            nodoActual = self.cabeza

            # Obtengo el nodo anterior
            nodoAnterior = nodoActual
            
            # Posicion Actual
            posicionActual = 1

            # Ciclo
            while (nodoActual!=None):            
                
                # Verificamos si estamos en la posición que queremos insertar
                if (posicion == posicionActual):                
                    
                    # Creamos el nodo
                    nodo =  Nodo(dato)

                    # Verificamos si estamos en la posicion 1
                    if (posicion==1):
                    
                        # El sgte del nodo apunta al sgte del head
                        nodo.sgte = self.cabeza

                        # Hacemos que la cabeza apunte al nuevo nodo
                        self.cabeza = nodo
                    
                    else:
                        # El nodo.sgte apunta a donde el sgte del anterior
                        nodo.sgte = nodoAnterior.sgte

                        # El anterior al nodo
                        nodoAnterior.sgte = nodo                    

                    # Mensaje
                    print  ("Se ha insertado el dato ",dato," en la posición ",posicion)

                    # Incrementamos el nodos
                    self.nodos+=1

                    # Salimos del ciclo
                    break
                

                # Incrementamos la posicion actual
                posicionActual+=1
                                
                # Nos movemos al siguiente nodo
                nodoAnterior = nodoActual

                # Incrementamos la posicion
                nodoActual = nodoActual.sgte        
        else:
        
            # Mensaje de Error
            print ("Error InsertarPorPosicion: posicion "+posicion+ " fuera de rango ...")

                    

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

    # Imprimir un elemento en la Lista
    def imprimirRecursivo(self,nodoDesplegar, esElPrimero, nodos=0):
        
        # Imprimimos
        if (esElPrimero):
           print("Lista["+str(nodos)+"]",end="->")

        # Verifico si es None
        if (nodoDesplegar is None):   
           # Imprime null al final
           print('None')    
        else:
           # Se imprime el dato
           print(nodoDesplegar.dato, end='->')

           # Aca esta la recursivida
           self.imprimirRecursivo(nodoDesplegar.sgte,False)


# Creamos una lista
lista = Lista()

# # Insertamos varios elementos
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.insertar(40)
lista.insertar(50)

# Desplegamos la longitud
print("Longitud:",lista.longitud())

# Desplegamos la lista
lista.imprimirRecursivo(lista.cabeza,True,lista.nodos)

#Insertamos en la posición 1
lista.insertarPorPosicion(5,1)

# Desplegamos la lista
lista.imprimirRecursivo(lista.cabeza,True,lista.nodos)

#Insertamos en la posición 6 que es la final
lista.insertarPorPosicion(60,6)

# Desplegamos la lista
lista.imprimirRecursivo(lista.cabeza,True,lista.nodos)

#Insertamos en la posición final que es la 6
lista.insertarPorPosicion("La 3",3)

# Desplegamos la lista
lista.imprimirRecursivo(lista.cabeza,True,lista.nodos)

