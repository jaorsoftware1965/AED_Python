# ----------------------------------------------------------------------
# Curso de Algoritmos y Estructuras de Datos en Python
# 07-Listas Vinculadas Eliminar
# ----------------------------------------------------------------------

# En esta clase agregaremos el método de eliminar
# Para eliminar un dato hay que considerar


# a) Si es el primero, tenemos que hacer que la cabeza
# apunte al siguiente del nodo a eliminar

# Cabeza
#    |
#   10->20->30

# Si queremos eliminar el 10, cabeza debe apuntar al 20


# b) En caso de que no sea el primero, el anterior a
# el; debe apuntar al siguiente del que se elimina

# Cabeza
#    |
#   10->20->30-->None

# Si queremos elimina el 20, el anterior; que es el 10
# debe apuntar al siguiente del 20; es decir al 30


# Eliminar el nodo en cada caso


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

        # Mensaje
        print ("Se ha creado la lista simple")


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

        # Mensaje
        print("El dato ",dato, "fue insertado en la Cabeza de la Lista ...")

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
            print ("Error InsertarPorPosicion: posicion ",posicion, " fuera de rango ...")

                    

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

    # Método para eliminar
    def eliminar(self,dato):
    
        # Obtenemos el apuntador temporal
        nodoActual = self.cabeza

        # Declaramos un apuntador a anterior
        nodoAnterior = None

        # Variable de posicion
        posicion = 1

        # Variable para controlar el borrado
        fueBorrado = False

        # Verificamos que haya elementos
        if (self.cabeza!=None):        
            
            # Ciclo para recorrer cada elemento
            while (nodoActual!=None):            
            
                # Verifica si es el dato
                if (nodoActual.dato == dato):                
            
                    # Verificamos si está en la cabeza
                    if (nodoActual == self.cabeza):                    
            
                        # El head apunta al siguiente
                        self.cabeza = nodoActual.sgte

                        # Mensaje
                        print ("El dato ",dato," fué eliminado en la cabeza en posicion ",posicion)                        
                    
                    else:
                        
                        # El anterior apunta al sgte del que se elimina
                        nodoAnterior.sgte = nodoActual.sgte

                        # Mensaje
                        print ("El dato ", dato," fué eliminado en la posición:" , posicion)                        
                                           
                    # Actualiza variable de Borrado
                    fueBorrado = True

                    # Eliminamos el sgte del nodo actual
                    del nodoActual           

                    # Decrementamos el contador de nodos
                    self.nodos-=1

                    #Sale del Ciclo
                    break
                
                # Guarda el nodo actual como anterior
                nodoAnterior = nodoActual

                # Se mueve al siguiente
                nodoActual = nodoActual.sgte

                # Incrementa posicion
                posicion+=1
            
            # Verifica si lo encontré         
            if (not fueBorrado):
            
                # No lo encontró
                print("El dato:",dato," no fué encontrado en la lista ..." )

                # Actualiza posición
                posicion = -1     
                        
        else:
        
            # NO hay elementos en la lista
            print("No hay elementos en la lista ...")

            # Actualiza posición
            posicion = 0
        

        # Retorna la posición
        return posicion

    

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
lista.imprimir()

# ELiminamos el primero
lista.eliminar(55)
lista.eliminar(50)

# Desplegamos la lista
lista.imprimir()

# ELiminamos el ultimo
lista.eliminar(10)

# Desplegamos la lista
lista.imprimir()


# ELiminamos en medio
lista.eliminar(30)

# Desplegamos la lista
lista.imprimir()

# ELiminamos los restanes
lista.eliminar(20)

# Desplegamos la lista
lista.imprimir()

lista.eliminar(40)

# Desplegamos la lista
lista.imprimir()

