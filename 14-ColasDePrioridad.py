# --------------------------------------------------------
# Curso de Algoritmos y Estructuras de Datos en JavaScript
# 14 Colas de Prioridad
# --------------------------------------------------------

# Cola de Prioridad
# Es aquella en donde cada nodo tiene un valor que determina
# su prioridad y en base a ello, el elemento es colocado en
# la fila

# Por ejemplo; en los servicios de salud, se le da prioridad
# a los niños y ancianos; y aunque haya una fila, se les
# atiende primero

# Para eso agregaremos una propiedad de prioridad al nodo

# Diseñaremos los siguientes métodos
# enqueue            . El que ya teníamos pero modificado
# enqueueMaxPriority . Insertar siempre en el frente
# enqueuePriority    . Insertar con una prioridad determinada


# Titulo de la Clase
print("AED en JavaScript con NodeJs")
print("13 Colas de Prioridad")
print("")


# Clase para el Nodo
class Node:

    # El constructor
    def __init__(self,data,priority=0):
    
        # Las 2 propiedades del Nodo
        self.data     = data
        self.priority = priority
        self.next     = None        
    


# Definimos la Clase para la Fila de Prioridad
class QueuePriority:

    # constructor
    def __init__(self,maxElementos):
    
        # Definimos un arreglo vacío para la lista
        print("Se ha creado una Fila de Prioridad para "+str(maxElementos))

        # Establecemos el front y rear
        self.front = None
        self.rear  = None
        self.max   = maxElementos

        # Para el tamaño de la fila
        self.size = 0
    

    # Método para verificar si está llena
    def isFull(self):
    
        # retorna si está lleno              
        return self.size==self.max
    

    # Método para verificar si está vacía
    def isEmpty(self):
    
        # retorna si está vacía
        return self.size==0
    

    # Tamaño
    def getSize(self):
    
        # Mensaje
        print("Size:"+str(self.size))

        # Retorna el tamaño
        return self.size
    

    
    # Método para obtener el frente
    def getFront(self):
    
        # Variable para resultado
        resultado = None

        # Verifica que no esté vacía
        if ( not self.isEmpty()):
        
            # Mensaje
            print("Front:",self.front.data , " Prioridad:", self.front.priority)

            # Coloca el resultado
            resultado = self.front
        
        else:
        
            # Mensaje
            print("La Fila está vacía, no hay frente ...")
        

        # Devuelve el resultado
        return resultado
    


    # Método para obtener el final
    def getRear(self):
    
        # Variable para resultado
        resultado = None

        # Verifica que no esté vacía
        if (not self.isEmpty()):
        
            # Mensaje
            print("Rear:",self.rear.data, " Prioridad:" , self.rear.priority)
            
            # Retorna el dato
            resultado = self.rear
        
        else:
        
            # Mensaje
            print("La Fila está vacía, no hay frente ... \n")
            
        # Devuelve el resultado
        return resultado
    
    

    # Método para encolar
    def enqueue(self,data):
    
        # Verificamos que no esté llena
        if (not self.isFull()):
        
            # Creamos un nodo con el datoy prioridad
            nodo = Node(data)        

            # Verificamos si es el primer elemento
            if (self.front==None):
            
                # El Frente y el Final son el mismo
                self.front = nodo
                self.rear  = nodo
            
            else:
            
                # Al nodo le asignamos una prioridad menor al de la cola
                nodo.priority = self.rear.priority - 1

                # El siguiente donde apunta rear, apunta ahora al nuevo nodo
                self.rear.next = nodo

                # rear apunta al nuevo nodo
                self.rear = nodo
            
            # Incrementamos el contador
            self.size+=1
        
        else:
        
            # Mensaje
            print("La Fila está llena; no es posible insertar mas elementos ...\n")
        
        
    

    # Método para encolar con Maxima Prioridad
    def enqueueMaxPriority(self,data):
    
        # Verificamos que no esté llena
        if (not self.isFull()):
        
            # Creamos un dato con el nodo
            nodo = Node(data, 0)        

            # Verificamos si es el primer elemento
            if (self.front==None):
            
                # El Frente y el Final son el mismo
                self.front = nodo
                self.rear  = nodo
            
            else:
            
                # Se coloca la prioridad mas 1 del frente
                nodo.priority = self.front.priority + 1

                # El nodo.next apunta al front
                nodo.next = self.front

                # Se coloca en el frente el nuevo nodo
                self.front = nodo
            
            # Incrementamos el contador
            self.size+=1
        
        else:
        
            # Mensaje
            print("La Fila está llena; no es posible insertar mas elementos ...")
        
        
    

    # Método para encolar con prioridad
    def enqueuePriority(self,data,priority):
    
        # Verificamos que no esté llena
        if (not self.isFull()):
        
            # Creamos un dato con el nodo
            nodo = Node(data, priority)        

            # Verificamos si es el primer elemento
            if (self.front==None):
            
                # El Frente y el Final son el mismo
                self.front = nodo
                self.rear  = nodo
            
            else:
            
                # Verifico que la prioridad del nodo a insertar sea menor que el que está al final
                if (priority < self.rear.priority):
                
                    # Inserta al final
                    self.rear.next = nodo

                    # El rear apunta al nuevo nodo
                    self.rear = nodo
                
                else:
                
                    # Busca el nodo que tenga menor prioridad que el que se inserta
                    #         6               6 -> 5                
                    # 9 -> 8 -> 5   ---> 9 -> 8 -> 5    ---> 9 -> 8 -> 6 -> 5

                    # Obtengo el apuntador
                    tmp         = self.front
                    tmpAnterior = tmp

                    # Ciclo para buscar un nodo con menor prioridad prioridad
                    while (tmp!=None):
                    
                        if (priority > tmp.priority):
                        
                            # Ya lo encontró; obligatoriamente lo tiene que encontrar
                            break
                        
                        # actualiza anterior
                        tmpAnterior = tmp

                        # Se mueve al siguiente
                        tmp = tmp.next
                    

                    # Verifica que no sea el primero, porque entonces no hay anterior
                    if (tmp == self.front):
                    
                        # Insertamos al frente
                        nodo.next = self.front

                        # Mueve el front
                        self.front = nodo
                    
                    else:
                    
                        # El nuevo nodo debe apuntar a donde anterior
                        nodo.next = tmpAnterior.next

                        # HAcemos que el anterior apunte al nuevo
                        tmpAnterior.next = nodo
                                        
                                
            

            # Incrementamos el contador
            self.size+=1
        
        else:
        
            # Mensaje
            print("La Fila está llena; no es posible insertar mas elementos ...\n")
        
    
    # Método para desencolar
    def dequeue(self):
    
        # resultado
        resultado = None

        # Verifica que haya elementos
        if (not self.isEmpty()):
        
            # Obtenemos el dato a eliminar
            resultado = self.front
                
            # Verifica si hay un solo elemento
            if (self.front == self.rear):
                            
                # Sed elimina el único y se Colocan los 2 apuntadores en None
                del (self.front)
                del (self.rear)
            
            else:
            
                # temporal
                tmp = self.front

                # Se elimina el del frente
                self.front = self.front.next

                # Elimina la referencia en temporal
                del (tmp.next)
            

            # Mensaje
            print("Se ha eliminado el dato:",resultado.data, " Prioridad:",resultado.priority)

            # Decremetamos el contador
            self.size-=1
        
        else:
        
            print("La Fila está vacía ...\n")
            

        # retornamos
        return resultado
    

    
    # Imprimir la Fila
    def print(self):
    
        # Declara una variable de salida
        salida = ""

        # Verifico que hay elementos en la Fila
        if (not self.isEmpty()):
        
            # Obtiene la referencia al front
            nodoActual = self.front

            # actualiza la salida
            salida += "Queue["+str(self.size)+"] = "

            # Inicializa el contador
            contador = 1

            # Ciclo para recorrer la lista
            while (nodoActual!=None):
            
                # Verifica si está en el ultimo dato
                if (contador < self.size):
                
                    salida += "["+nodoActual.data+"|"+str(nodoActual.priority)+"],"
                
                else:
                
                    salida += "["+nodoActual.data+"|"+str(nodoActual.priority)+"]"
                

                # Incrementa el contador
                contador+=1

                # Se mueve al siguiente nodo
                nodoActual = nodoActual.next
            
            # Deslpliega la salida
            print(salida)
        
        else:
        
            # Mensaje
            print("La Fila no tiene elementos ...\n")
        


# Creamos una Fila de Prioridad
oFila = QueuePriority(10)

# Encolamos datos
oFila.enqueue("Test.txt")

# Imprime la lista ascendente
oFila.print()

# Obtener el Frente
oFila.getFront()

# Obtener el Final
oFila.getRear()

# Obtener el tamaño de la fila
oFila.getSize()


# Encolamos datos
oFila.enqueue("Archivo.dat")
oFila.enqueue("Documento.pdf")
oFila.enqueue("Foto.jpg")
oFila.enqueue("Imagen.png")


# Imprime 
oFila.print()

# Obtener el Frente
oFila.getFront()

# Obtener el Final
oFila.getRear()

# Obtener el tamaño de la fila
oFila.getSize()

# Deja una linea
print("")

# Insertar con Máxima Prioridad
oFila.enqueueMaxPriority("Importante.pdf")

# Imprime 
oFila.print()

# Obtener el Frente
oFila.getFront()

# Obtener el Final
oFila.getRear()

# Obtener el tamaño de la fila
oFila.getSize()

# Deja una linea
print("")

# Insertamos con prioridad
oFila.enqueuePriority("InsertaPrioridad1.txt",1)

# Imprime 
oFila.print()

# Obtener el Frente
oFila.getFront()

# Obtener el Final
oFila.getRear()

# Obtener el tamaño de la fila
oFila.getSize()

# Deja una linea
print("")

# Insertamos con prioridad
oFila.enqueuePriority("InsertaPrioridad2.txt",2)

# Imprime 
oFila.print()

# Obtener el Frente
oFila.getFront()

# Obtener el Final
oFila.getRear()

# Obtener el tamaño de la fila
oFila.getSize()

# Deja una linea
print("")

# Insertamos con prioridad
oFila.enqueuePriority("InsertaPrioridad-10.txt",-10)

# Imprime 
oFila.print()

# Obtener el Frente
oFila.getFront()

# Obtener el Final
oFila.getRear()

# Obtener el tamaño de la fila
oFila.getSize()

# Deja una linea
print("")


