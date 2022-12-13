# ----------------------------------------------------------------------
# Curso de Algoritmos y Estructuras de Datos en Python
# 12-Listas Ordenamiento Burbuja Bubble Sort
# ----------------------------------------------------------------------


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
            while (True):            
                
                # Verificamos si estamos en la posición que queremos insertar
                if (posicion == posicionActual):                
                    
                    # Creamos el nodo
                    nodoNuevo =  Nodo(dato)

                    # Verificamos si estamos en la posicion 1
                    if (posicion==1):
                    
                        # El sgte del nodo apunta al sgte del cabeza
                        nodoNuevo.sgte = self.cabeza

                        # Hacemos que la cabeza apunte al nuevo nodo
                        self.cabeza = nodoNuevo
                    
                    else:

                        # El nodo.sgte apunta a donde el sgte del anterior
                        nodoNuevo.sgte = nodoAnterior.sgte

                        # El anterior al nodo
                        nodoAnterior.sgte = nodoNuevo                    

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

    # Insertar con Orden Ascendente Descendente
    def insertarConOrd(self,dato,ascendente):
        # Verifica que haya elementos en la lista
        if (self.nodos==0):
            # Inserta normal
            self.insertar(dato)
        else:
            # Verifica si es ascendente la inserción
            if (ascendente):
                # Inserta Ascendente
                posDato = self.buscarMayor(dato)
            else:
                #Inserta Descendente
                posDato = self.buscarMenor(dato)     

            # Verifica si encontró dato
            if (posDato[0]>0):    
               # Inserta el dato en la posición obtenida
               self.insertarPorPosicion(dato,posDato[0])    

            else:
               # Inserta al final
               self.insertarFinal(dato)


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

        # Imprime None al final
        print('None')

    # Imprimir un elemento en la Lista
    def imprimirRecursivo(self,nodoDesplegar, esElPrimero, nodos=0):
        
        # Imprimimos
        if (esElPrimero):
           print("Lista["+str(nodos)+"]",end="->")

        # Verifico si es None
        if (nodoDesplegar is None):   
           # Imprime None al final
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
            
                        # El cabeza apunta al siguiente
                        self.cabeza = nodoActual.sgte
                    
                    else:
                        
                        # El anterior apunta al sgte del que se elimina
                        nodoAnterior.sgte = nodoActual.sgte

                                           
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

    # Método para eliminar por posición
    def eliminarPorPosicion(self,posicion):
    
        # Obtenemos el apuntador temporal
        nodoActual = self.cabeza

        # Declaramos un apuntador a anterior
        nodoAnterior = None

        # Variable de posicion
        posicionActual = 1

        # Valor a retornar
        resultado = None
        

        # Verificamos que haya elementos
        if (self.cabeza!=None):
        
            # Verificamos que la posición esté en el rango
            if (posicion<=self.nodos):
            
                # Ciclo para recorrer cada elemento
                while (nodoActual!=None):
                
                    # Verifica si es la posición deseada
                    if (posicion == posicionActual):
                    
                        # Verificamos si está en la cabeza
                        if (nodoActual == self.cabeza):
                        
                            # El cabeza apunta al siguiente
                            self.cabeza = nodoActual.sgte
                        
                        else:
                        
                            # El anterior apunta al sgte del que se elimina
                            nodoAnterior.sgte = nodoActual.sgte
                        
                        # Coloca el Resultado
                        resultado = nodoActual.dato

                        # Eliminamos el sgte del nodo actual
                        del nodoActual

                        # Decrementamos el nodos
                        self.nodos-=1

                        # Sale del Ciclo
                        break
                    
                    # Guarda el nodo actual como anterior
                    nodoAnterior = nodoActual

                    # Se mueve al siguiente
                    nodoActual = nodoActual.sgte

                    # Incrementa posicion
                    posicionActual+=1
                
            
            else:
            
                # Mensaje
                print("La posición:",posicion," esta fuera de rango ...")
            
        
        else:        
            # NO hay elementos en la lista
            print("No hay elementos en la lista ...")        

        # Retorna la posición
        return resultado

    # Buscar un dato
    def buscar(self,dato):
    
        # Variable para la posición
        posicion = 1

        # Obtiene la referencia del cabeza
        nodoActual = self.cabeza


        # Ciclo para recorrer los elementos
        while (nodoActual!= None):
        

            # Verifica que sea el dato buscado
            if (dato == nodoActual.dato):
            
                # sale del ciclo
                break
            
            else:
            
                # Se mueve al siguiente dato
                nodoActual = nodoActual.sgte

                # Incrementa el contador de posición
                posicion+=1
                        
        
        #  Verifica el apuntador temporal para saber si lo encontró
        if (nodoActual==None):
        
            # No lo encontró
            print("El dato:",dato," no fué encontrado en la lista ..." )

            # Coloca la posición en -1
            posicion = -1
        

        # Devuelve la posición
        return posicion
    

    # Buscar por posicion
    def buscarPorPosicion(self,posicion):
    
        # Variable para resultado
        resultado = None

        # Validamos la posicion
        if (posicion <= self.nodos and posicion > 0):
        
            # Variable para la posicion
            posicionActual = 1

            # Obtiene la referencia al cabeza
            nodoActual = self.cabeza

            # Ciclo para recorrer los elementos
            while (nodoActual!=None):
            
                # Verifica si está en la posición actual
                if (posicion == posicionActual):
                
                    # Coloca el dato en resultado
                    resultado = nodoActual.dato

                    # Sale del ciclo
                    break
                
                # Se mueve al siguiente nodo
                nodoActual = nodoActual.sgte

                # Incrementa la posicion
                posicionActual+=1
                    
        else:
        
            # Mensaje
            print("Error buscarPorPosicion. posición fuera de rango ...")
        

        # Retorna el resultado
        return resultado

    

    # Método para buscar el Mayor y retornar su posición
    def buscarMayor(self,dato):
    
        # Variables
        posicionActual = 1
        datoEncontrado = None

        # Obtiene la referencia del cabeza
        nodoActual = self.cabeza

        # Valida que haya elementos
        if (self.nodos > 0):
        
            # Ciclo para recorrer los elementos
            while (nodoActual!=None):
            
                # Verifica que sea mayor
                if (nodoActual.dato > dato):
                
                    # Valor encontrado
                    datoEncontrado = nodoActual.dato

                    # Rompe el ciclo
                    break
                
                # Se mueve al siguiente nodo
                nodoActual = nodoActual.sgte

                # Incrementa la posicion actual
                posicionActual+=1
            

            # Verifica que lo haya encontrado
            if (not datoEncontrado):
            
                # Indica que no encontró
                posicionActual = 0

                # Mensaje
                print("No se encontró un elemento mayor que:",dato)
            
        
        else:
        
            # Mensaje
            print("La lista está vacía ...")
        

        # Creamos la lista para los resultados
        resultado = []

        # Se agrega la posición actual y el dato encontrado
        resultado.append(posicionActual)
        resultado.append(datoEncontrado)

        # retorna el resultado
        return resultado
    

    # Método para buscar el Menor y retornar su posición
    def buscarMenor(self,dato):
    
        # Variables
        posicionActual = 1
        datoEncontrado = None

        # Obtiene la referencia del cabeza
        nodoActual = self.cabeza

        # Valida que haya elementos
        if (self.nodos > 0):
        
            # Ciclo para recorrer los elementos
            while (nodoActual!=None):
            
                # Verifica que sea menor
                if (nodoActual.dato < dato):
                
                    # Valor encontrado
                    datoEncontrado = nodoActual.dato

                    # Rompe el ciclo
                    break
                
                # Se mueve al siguiente nodo
                nodoActual = nodoActual.sgte

                # Incrementa la posicion actual
                posicionActual+=1
            

            # Verifica que lo haya encontrado
            if (not datoEncontrado):
            
                # Indica que no encontró
                posicionActual = 0

                # Mensaje
                print("No se encontró un elemento menor que:",dato)
            
        
        else:
        
            # Mensaje
            print("La lista está vacía ...")
        

        # Creamos la lista para los resultados
        resultado = []

        # Se agrega la posición actual y el dato encontrado
        resultado.append(posicionActual)
        resultado.append(datoEncontrado)

        # retorna el resultado
        return resultado

    # Invertir una lista
    def invertir(self):

        # Vector para los datos
        datosEnLista=[]

        # Verifica que haya datos en la lista
        if (self.nodos > 0):

            # Ciclo mientras haya nodos en la lista
            while (self.nodos > 0):
                # Eliminamos de la posición 1 y obtenemos el dato
                datoEliminado = self.eliminarPorPosicion(1)

                # Agregamos el dato a la lista
                datosEnLista.append(datoEliminado)

            # Ciclo para agrega a la lista ya invertido
            for contador in range(0,len(datosEnLista)):
                
                # Agrega
                self.insertar(datosEnLista[contador])

            # Mensaje
            print("La lista ha sido invertida ...")

        else:
            # Mensaje
            print("No hay elementos en la lista para invertir ...")   

    # Colocar en Posición
    def colocarEnPosicion(self,dato,posicion):
    
        # Validamos posicion
        if (posicion <= self.nodos and posicion > 0):
        
            # Variable para la posición actual
            posicionActual = 1

            # Referencia al nodo actual
            nodoActual = self.cabeza

            # Ciclo para recorrer los elementos
            while (nodoActual!=None):            
                # Verifica
                if (posicion == posicionActual):
                
                    # coloca el dato
                    nodoActual.dato = dato

                    # Sale del ciclo
                    break
                

                # Se mueve al siguiente dato
                nodoActual = nodoActual.sgte

                # Incrementa la posicion actual
                posicionActual+=1
            
        
        else:
        
            # Mensaje
            print("Error colocarPosicion. La posición ",posicion, " no es válida ...")
        
    

    # Metodo de ordenamiento burbuja ascendente/descendente
    def ordenarPorBurbuja(self,ascendente):
    
        # Ciclo para el primer indice
        for index1 in range(1,self.nodos):            
        
            # Ciclo para el segundo indice
            for index2 in range(index1+1,self.nodos+1):                
            
                # Obtenemos el dato a comparar izquierdo
                datoIzquierdo = self.buscarPorPosicion(index1)

                # Obtenemos el dato a comparar derecho
                datoDerecho   = self.buscarPorPosicion(index2)

                # Verificamos tipo ordenamiento
                if (ascendente):
                    # Comparamos
                    if (datoIzquierdo > datoDerecho):
                                            
                        # Se hace la permuta
                        self.colocarEnPosicion(datoDerecho,index1)
                        self.colocarEnPosicion(datoIzquierdo,index2)            
                    
                else:
                    # Comparamos
                    if (datoIzquierdo < datoDerecho):                    
                        # Se hace la permuta
                        self.colocarEnPosicion(datoDerecho,index1)
                        self.colocarEnPosicion(datoIzquierdo,index2)            

# Creamos lista
lista = Lista()


# lista de datos para el test
lstNumeros = [100,2,20,22,13,45,67,89,22,34]

# Ciclo
for contador in range(0,10):
    
    # Insertamos
    lista.insertar(lstNumeros[contador])

    
# Desplegamos la longitud
lista.imprimir()

# Ordenamos por Burbuja
lista.ordenarPorBurbuja(True)

# Imprimos de nuevo
lista.imprimir()

# Ordenamos por Burbuja
lista.ordenarPorBurbuja(False)

# Imprimos de nuevo
lista.imprimir()
