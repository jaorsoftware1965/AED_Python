# ----------------------------------------------------------------------
# Curso de Algoritmos y Estructuras de Datos en Python
# 14-Colas
# ----------------------------------------------------------------------

# Cola
# Una Cola o Fila, es una secuencia de datos las cuales siguen una lógica de
# operación llamada FIFO: First In First Out. Primero en entrar es el primero
# en salir; en español PEPS

# Para comprender mas fácilmente es como una fila para comprar algo.
# La primera persona que se forma en la fila es la primera en ser atendida.
# Primera persona en ENTRAR a la Cola es la primera en SALIR.

# Llegan; Juan, Pedro y María
# Ventanilla: Juan, Pedro, Maria
# frente: Juan
# cola  : Maria

# Se despacha a juan
# Ventanilla: Pedro, Maria

# El Nodo en una fila, sigue teniendo la misma estructura que hemos visto
# en las Pilas y en las Listas: data y next

# Para manejar una Fila optimamente, se necesitan 2 apuntadores:
# a)front. El frente de la Fila, por donde se da el servicio
# b)rear . La cola   de la Fila

# En las filas, se considera que esta puede encontrarse llena, por lo tanto
# debe de haber una constante que determine cuantos elementos puede haber
# en la Fila

# Los métodos tradicionales que se implementan en una fila son:
# enqueue . Inserta un elemento  en la cola
# dequeue . Eliminar un elemento de la cola
# isFull  . Verificar si está llena
# isEmpty . Verificar si está vacía
# imprimir. Imprimir los elementos de la Fila

# getFront. Obtener el que está al frente (peek)
# getRear . Obtener el que está al final
# getSize . Obtener el tamaño de la fila

# Cuando insertamos en una fila, la circunstancia especial es cuando insertamos
# el primer elemento, para lo cual, el front y el rear, apuntan a este primer
# elemento

# Cuando eliminamos en una fila, la circunstancia especial es cuando eliminamos
# el único elemento, ya que tenemos que hacer que el front y el rear se liberen


# Clase para el Nodo
class Node:

    # El constructor
    def __init__(self,data):
    
        # Las 2 propiedades del Nodo
        self.data = data
        self.next = None
    


# Definimos la Clase para la Fila
class Queue:

    # constructor
    def __init__(self,maxElementos):
    
        # Definimos un arreglo vacío para la lista
        print("Se ha creado una Fila para ",maxElementos,"\n")

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
        print("Size:",self.size)

        # Retorna el tamaño
        return self.size
    

    
    # Método para obtener el frente
    def getFront(self):
    
        # Verifica que no esté vacía
        if (not self.isEmpty()):
        
            # Mensaje
            print("Front:",self.front.data)

            # Retorna el dato
            return self.front.data
        
        else:
        
            # Mensaje
            print("La Fila está vacía, no hay frente ...\n")
        
    

    # Método para obtener el final
    def getRear(self):
    
        # Verifica que no esté vacía
        if (not self.isEmpty()):
        
            # Mensaje
            print("Rear:",self.rear.data)
            
            # Retorna el dato
            return self.rear.data
        
        else:
        
            # Mensaje
            print("La Fila está vacía, no hay cola ...\n")
    
    # Método para encolar
    def enqueue(self,data):
    
        # Verificamos que no esté llena
        if (not self.isFull()):
        
            # Creamos un dato con el nodo
            nodo = Node(data)        

            # Verificamos si es el primer elemento
            if (self.front==None):
            
                # El Frente y el Final son el mismo
                self.front = nodo
                self.rear  = nodo
            
            else:
            
                # El siguiente donde apunta rear, apunta ahora al nuevo nodo
                self.rear.next = nodo

                # rear apunta al nuevo nodo
                self.rear = nodo
            
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
            resultado = self.front.data
                
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
            print("Se ha eliminado el dato:",resultado,"\n")

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
            while (nodoActual != None):
            
                # Verifica si está en el ultimo dato
                if (contador < self.size):
                
                    salida += nodoActual.data+","
                
                else:
                
                    salida += nodoActual.data+""
                

                # Incrementa el contador
                contador+=1

                # Se mueve al siguiente nodo
                nodoActual = nodoActual.next
            
            # Deslpliega la salida
            print(salida,"\n")
        
        else:
        
            # Mensaje
            print("La Fila no tiene elementos ...\n")
        

# Creamos una Fila
oFila = Queue(10)

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

# Eliminamos 2 elementos de la fila
oFila.dequeue()
oFila.dequeue()

# Imprime 
oFila.print()

# Obtener el Frente
oFila.getFront()

# Obtener el Final
oFila.getRear()

# Obtener el tamaño de la fila
oFila.getSize()

oFila.dequeue()
oFila.dequeue()

# Imprime 
oFila.print()

# Obtener el Frente
oFila.getFront()

# Obtener el Final
oFila.getRear()

# Obtener el tamaño de la fila
oFila.getSize()


oFila.dequeue()
oFila.dequeue()

# Imprime 
oFila.print()

# Obtener el Frente
oFila.getFront()

# Obtener el Final
oFila.getRear()

# Obtener el tamaño de la fila
oFila.getSize()