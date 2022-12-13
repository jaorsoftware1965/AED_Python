# --------------------------------------------------------
# Curso de Algoritmos y Estructuras de Datos en JavaScript
# 14 Listas Doblemente Enlazadas
# --------------------------------------------------------

# Una lista doblemente enlazada es una lista en donde cada
# nodo tiene un apuntador al siguiente nodo y un apuntador
# al anterior nodo

# Adicionalmente, aparte de tener el apuntador head, tiene 
# un apuntador adicional que apunta a la cola de la lista
# es decir al último elemento


#        head                     tail
#         |                        |
#  None <-10--> <--20-->....    <--50--> None

# Los elementos entran por la cabeza, tal y como en la lista
# simple

#          head y tail
#               |
#       None<-- 10 ->None

# Cabeza.prev -> 20
# nodo.sgte   -> 10
# Cabeza      -> 20

#            head
#             |
#      None<--20--> <--10-->None

# Titulo de la Clase
print("AED en JavaScript con NodeJs")
print("14 Listas Doblemente Enlazadas")
print("")

# Clase para el Nodo
class Nodo:

    # El constructor
    def __init__(self,dato):
    
        # Las 3 propiedades del Nodo
        self.dato = dato
        self.sgte = None
        self.prev = None
    


# Definimos la Clase para la Lista Doble
class listaDoble:

    # constructor
    def __init__(self):
    
        # Definimos un arreglo vacío para la lista
        print("Se ha creado una lista Doblemente enlazada ...")

        # Establecemos que el head y el tail apunta a None
        self.cabeza   = None
        self.cola     = None

        # Para el longitud de la lista
        self.longitud = 0        
    

    # Método para insertar en la lista doble
    def insertar(self,dato):
    
        # Creamos un dato con el nodo
        nodo = Nodo(dato)

        # Verificamos si es el primer elemento
        if (self.cabeza == None):
        
            # Cabeza y cola apuntan al primer elemento
            self.cabeza = nodo
            self.cola   = nodo

            # Mensaje
            print("Se ha insertado el dato:",dato," como primero en la lista")
        
        else:
        
            # hacemos que el nodo->prev al que apunta cabeza
            # debe apuntar al nvo nodo
            self.cabeza.prev = nodo

            # Hacemos que el nuevo nodo su siguiente apunte a donde
            # está apuntado la cabeza
            nodo.sgte = self.cabeza

            # Cabeza apunta al nodo
            self.cabeza = nodo

            # Mensaje
            print("Se ha insertado en la cabeza el dato: ",dato)
        

        # Incrementamos longitud
        self.longitud+=1       
    

    # Método para imprimir la lista doble
    def imprimir(self):
    
        # Declara una variable de salida
        salida=""

        # Verifico que hay elementos en la lista
        if (self.longitud > 0):
        
            # Obtiene la referencia a la cabeza
            nodoActual = self.cabeza

            # actualiza la salida
            salida += "["+str(self.longitud)+"] = "

            # Inicializa el contador
            contador = 1

            # Ciclo para recorrer la lista
            while (nodoActual!=None):
            
                # Verifica si está en el ultimo dato
                if (contador < self.longitud):
                
                    salida += str(nodoActual.dato)+","
                
                else:
                
                    salida += str(nodoActual.dato)+""
                

                # Incrementa el contador
                contador+=1

                # Se mueve al siguiente nodo
                nodoActual = nodoActual.sgte
            
            # Deslpliega la salida
            print(salida)
        
        else:
        
            # Mensaje
            print("La lista no tiene elementos ...")
                        
    

    # Método para imprimir la lista doble
    def imprimirReverso(self):
    
        # Declara una variable de salida
        salida=""

        # Verifico que hay elementos en la lista
        if (self.longitud > 0):
        
            # Obtiene la referencia a la cola
            nodoActual = self.cola

            # actualiza la salida
            salida += "["+str(self.longitud)+"] = "

            # Inicializa el contador
            contador = 1

            # Ciclo para recorrer la lista
            while (nodoActual!=None):
            
                # Verifica si está en el ultimo dato
                if (contador < self.longitud):
                
                    salida += str(nodoActual.dato)+","
                
                else:
                
                    salida += str(nodoActual.dato)+""
                

                # Incrementa el contador
                contador+=1

                # Se mueve al previo nodo
                nodoActual = nodoActual.prev
            
            # Deslpliega la salida
            print(salida)
        
        else:
        
            # Mensaje
            print("La lista no tiene elementos ...")
                        
    


# Creamos una lista simple
oListaSimple = listaDoble()

# Insertamos varios elementos
oListaSimple.insertar(10)

# Imprimimos los datos de la lista
oListaSimple.imprimir()

oListaSimple.insertar("Rocky Balboa")
oListaSimple.insertar(True)

# Imprimimos los datos de la lista
oListaSimple.imprimir()
oListaSimple.imprimirReverso()

# Insertamos 2 elementos
oListaSimple.insertar("Rambo")
oListaSimple.insertar(3.1416)


# Imprimimos los datos de la lista
oListaSimple.imprimir()
oListaSimple.imprimirReverso()