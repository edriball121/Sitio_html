#---------------------------------------------------------------------------
#1 Asignar nuevo valor a elemento de la lista
numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numeros) # imprimiendo contenido de la lista original.
numeros[0]=111
print ("Nuevo contenido de la lista: " , numeros)

#---------------------------------------------------------------------------
#2 copiar el valor de una posición en otra

numeros[1] = numeros[4]

#---------------------------------------------------------------------------
#3 mostrar contenido / longitud de la lista

numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo el contenido de la lista original

numeros [0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior

numeros [1] = numeros [4] # copiando el valor del quinto elemento al segundo
print("Contenido de la lista anterior:", numeros) # imprimiendo contenido de la lista anterior

print("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista


#---------------------------------------------------------------------------
#4 eliminar elementos de una lista
numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo contenido de la lista original

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior

numeros[1] = numeros[4] # copiando el valor del quinto elemento al segundo
print("Contenido de la lista anterior:", numeros) # imprimiendo contenido de la lista anterior

print ("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista anterior

###

del numeros[1] # eliminando el segundo elemento de la lista
print("Longitud de la nueva lista:", len(numeros)) # imprimiendo nueva longitud de la lista
print("\nNuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual

del numeros[1]
print(len(numeros))
print(numeros) 



#---------------------------------------------------------------------------
#5 indices negativos

numeros = [111, 7, 2, 1]
print(numeros[-1])
print(numeros[-2])


#---------------------------------------------------------------------------
#6 ejercicio practico

listaSombrero = [1, 2, 3, 4, 5] # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# para reemplazar el número de en medio con un número entero ingresado por el usuario.

listaSombrero[2] = int(input("Ingrese un numero entero "))

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.

del listaSombrero[4]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.

print ("La longitus es: ",len(listaSombrero))

print(listaSombrero)

#---------------------------------------------------------------------------
#7 agregar elementos a una lista Append/insert
numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)

###

numeros.append(4)

print(len(numeros))
print(numeros)

###

numeros.insert(0,222)
print(len(numeros))
print(numeros)

#
numeros.insert(1,333)
print(len(numeros))
print(numeros)

#---------------------------------------------------------------------------
miLista = [] # creando una lista vacía
miLista2 = []
for i in range (5):
    miLista.append (i + 1)

print(miLista)
#
for i in range(5):
    miLista2.insert(0, i + 1)

print(miLista2)


#-------------------------------------------------
#20. Ejercicio lista
miLista = [10, 1, 8, 3, 5]
suma = 0

for i in range(len(miLista)):
    suma += miLista[i]

print("El resultado de la suma es: ", suma)

#-------------------------------------------------
#21. Ejercicio lista
miLista = [10, 1, 8, 3, 5]
suma = 0

for i in miLista:
    suma += i

print(suma)

#-------------------------------------------------
#22. cambiar valores de variables entre si
var1=1
var2=2
var1, var2 = var2, var1  
print("Variable 1: ", var1)  
print("Variable 2: ", var2)

#-------------------------------------------------
#23. cambiar valores de los subindices de una lista

miLista = [10, 1, 8, 3, 5]

miLista [0], miLista [4] = miLista [4], miLista [0]
miLista [1], miLista [3] = miLista [3], miLista [1]

print(miLista) 


#-------------------------------------------------
#24. Ejercicio practico de listas los Beatles

# paso 1 / Crear una lista vacia llamada beatles
beatles = []
print("Paso 1:", beatles)

# paso 2 / emplear el metodo append para agregar a los miembros de la banda
beatles.append("Jhon Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3 / emplear ciclo for para agregar mas miembros
for i in range(2):
    beatles.append(input("Ingrese un nuevo miembro a la banda: "))
print("Paso 3:", beatles)

# etapa 4
del(beatles[3])
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fabulosos tamaño de la banda ", len(beatles), " miembros")


#-------------------------------------------------
#25. ordenar lista de forma ascendente

miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista)

#-------------------------------------------------
#26. ordenar lista de forma ascendente interactiva
miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = int(input("Introduce un elemento de la lista: "))
    miLista.append(val)

while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)

#-------------------------------------------------
#27. Copiar parte del contenido de una lista

# Copiando toda la lista
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)

# Copiando parte de la lista
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:4]
print(nuevaLista)

#-------------------------------------------------
#27. in / not validar si un elemento existe o no en la lista

miLista = [0, 3, 12, 8, 2]

print(5 in miLista)
print(5 not in miLista)
print(12 in miLista)

#-------------------------------------------------
#28. Elemento mayor de una lista

miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista[0]

for i in range(1, len(miLista)):
   if miLista [i]> mayor:
        mayor = miLista[i]

print(mayor)


#-------------------------------------------------
#28. Encontrar elemento en una lista

miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5
Encontrado = False

for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar
    if Encontrado:
        break

if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

#-------------------------------------------------
#28. Encontrar elemento en una lista

sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0

for numeros in seleccionados:
    if numeros in sorteados:
        aciertos += 1

print(aciertos)

#-------------------------------------------------
#29. ejemplo practico listas

#mostrar solo los numeros que no esten repetidos
miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("Lista original: ", miLista)
otraLista = [] #crear nueva lista vacia

[otraLista.append(nuevaLista)

for nuevaLista in miLista
    if nuevaLista not in otraLista]

print(otraLista)

#otro metodo
unique_sweets = list(set(miLista))
print("Con metodo set: ", unique_sweets)

#-------------------------------------------------
#30. Listas bidimensionales (Matrices)
# EJEMPLO ajedrez

EMPTY = "-"
TORRE = "TORRE"
PEON = "PEON"
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)

tablero[0][0] = TORRE
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE
tablero[1][0] = PEON

print(tablero)

#-------------------------------------------------
#31. Listas bidimensionales (Matrices)

temps = [[0.0 for h in range (24)] for d in range (31)]
suma = 0.0

for day in temps:
    suma += day[11]

promedio= suma / 31

print("Temperatura promedio al mediodía:", promedio)
mas_alta = -100.0

for day in temps:
    for temp in day:
        if temp > mas_alta:
            mas_alta = temp

print("La temperatura más alta fue:", mas_alta)

hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

#-------------------------------------------------
#31. Listas tridimensionales (Matrices)

#3 edificios con 15 pisos y 20 habitaciones en cada piso
habitaciones =[[[False for r in range(20)] for f in range(15)] for t in range(3)]

habitaciones[1][9][13] = True #reservar cuarto
habitaciones[0][4][1] = False  #liberar reservación
print(habitaciones)

#validar habitaciones disponibles
vacante = 0

for numeroHabitacion in range(20):
    if not habitaciones[1][14][numeroHabitacion]:
        vacante += 1
print(vacante)



#https://edube.org/learn/programming-essentials-in-python-part-1-spanish/operaciones-en-listas-in-not-in