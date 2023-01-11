#------------------------------------------
#1. Formas mas elemental de una funcion
def mensaje():
    valor = int(input("Ingrese un valor: "))
    return print("Mensaje retornado con valor: ", valor)
mensaje()

#------------------------------------------
#2. función con parametros
def suma(n1,n2):
    return print(n1+n2)
suma(5,3)

#-----------------
def nombre(nom1):
    return print("Hola", nom1)

nombre("jose")

#------------------------------------------
#3. función con parametros
def mensaje(que, numero):
    print("Ingresa", que, "número", numero)

# invocar la función
mensaje("teléfono", 11)
mensaje("precio", 5)
mensaje("número", "número")

#------------------------------------------
#4. función con parametros

def miFuncion(a, b, c):
    print(a, b, c)

miFuncion(1, 2, 3)

#------------------------------------------
#4. función con parametros

def presentar(primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

def presentarUngria(primerNombre, segundoNombre):
    print("Hola, mi nombre es", segundoNombre, primerNombre)

print("Seleccion pais:")
print("1. Para Ungria")
print("2. Para Colombia")
pais = int(input(""))

if pais == 1:
    presentarUngria("Luke", "Skywalker")
    presentarUngria("Jesse", "Quick")
    presentarUngria("Clark", "Kent")

elif pais == 2:
    presentar("Luke", "Skywalker")
    presentar("Jesse", "Quick")
    presentar("Clark", "Kent")

else:
    print("Ha ingresado una opción invalida")

#------------------------------------------
#4. función con parametros / pasar parametros con valores

def presentar (primerNombre, segundoNombre):
    print("Hola, mi nombre es ", primerNombre, segundoNombre)

presentar(segundoNombre="Skywalker", primerNombre="Luke")

#------------------------------------------
#4. función con parametros
def suma(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# Llamarla funcion con argumentos posicionales
suma (1,2,3)

# Llamar la funcion con palabras clave
suma (a = 3, b = 2, c = 4)

#Llamar la funcion con argumentos posicionales y palabras clave
suma(3, c=1, b=3)

#------------------------------------------
#4. función con parametros / valores predeterminados

def presentar(primerNombre, segundoNombre="Smith"):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

# mandar llamar la función aquí (invocarla)
presentar("Edwin")
presentar("Edwin", "Rivera")
presentar(primerNombre="Edwin")

#------------------------------------------
#4. función con parametros

def presentar(primerNombre="Anderson", segundoNombre="Smith"):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar()

#------------------------------------------
#4. función con parametros / None

def strangeFunction(n):
    if(n % 2 == 0):
        return True
print(strangeFunction(2))
print(strangeFunction(1)) 


#------------------------------------------
#4. función con parametros / listas como parametro

def sumaDeLista(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return print(sum)

sumaDeLista([1,2,3,4])


#------------------------------------------
#4. función con parametros

def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))

#------------------------------------------
#4. función con parametros

def isYearLeap(year): #Funcion para determinar si un año es o no biciesto
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                val = True
                return val
            else:
                val = False
                return val
        else:
            val = True
            return val
    else:
        val = False
        return val

testData = [1900, 2000, 2016, 1987] #Años de prueba
testResults = [False, True, True, False] # Resultados de los años de prueba
for i in range(len(testData)):#Este for recorre los arreglos y si el resultado cocincide o no
	yr = testData[i] #Almacena la lista en una nueva variable
	print(yr,"->",end="")
	result = isYearLeap(yr)#llama al funcion y compara
	if result == testResults[i]: #si el resultado de la funcion coincide con la lista o no
		print("OK")
	else:
		print("Error")
        
print(isYearLeap(1987))

#------------------------------------------
#4. función con parametros / usar una funcion en otra funcion

def isYearLeap(year): #Funcion para determinar si un año es o no biciesto
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                val = True
                return val
            else:
                val = False
                return val
        else:
            val = True
            return val
    else:
        val = False
        return val

anno = isYearLeap(1900)
print("Esbiciesto: ",anno)

def daysInMonth(month):
    if anno == True and month == 2:
        days=29
        print("Dias de: ", days)
    else:
        #meses de 30
        if month == 4 or month == 6 or month == 9 or month == 11:
            days = 30
            print("Dias de: ", days)
        #meses de 31
        elif month == 1 or month == 3 or month == 5 or month == 8 or month == 7 or month == 10 or month == 12:
            days = 31
            print("Dias de: ", days)   
        else:
            days=28
            print("Dias de: ", days)

daysInMonth(2)
#------------------------------------------
#4. función con parametros / misma funcion de determinar cuantos dias tiene 1 mes otra forma

def daysInMonth(year, month):
    #validar año bisiesto
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                val = True
            else:
                val = False
        else:
            val = True
    else:
        val = False#fin validar año bisiesto
    #Validar cuantos meses tiene el año / febrero de 28 o 29 si es o no biciesto
    if val == True and month == 2:
        days=29
        print("Dias de: ", days)
    else:
        #meses de 30
        if month == 4 or month == 6 or month == 9 or month == 11:
            days = 30
            print("Dias de: ", days)
        #meses de 31
        elif month == 1 or month == 3 or month == 5 or month == 8 or month == 7 or month == 10 or month == 12:
            days = 31
            print("Dias de: ", days)   
        else:
            days=28
            print("Dias de: ", days)
    return days

#Validar la función
testYears = [1900, 2000, 2016, 1987, 2023]
testMonths = [2, 2, 1, 11, 2]
testResults = [28, 29, 31, 30, 29]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print("El año: ", yr, " y el mes: ",mo, "->", end="")
	result = daysInMonth(yr,mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")


#------------------------------------------
#4. función con parametros laboratorio final

#Tu tarea es escribir y probar una función que toma tres argumentos 
# (un año, un mes y un día del mes) y devuelve el día correspondiente del año, 
# o devuelve None si cualquiera de los argumentos no es válido.
# Debes utilizar las funciones previamente escritas y probadas. Agrega algunos 
# casos de prueba al código. Esta prueba es solo el comienzo.

def isYearLeap(year):#Determinar si un año es o no biciesto
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                val = True
                return val
            else:
                val = False
                return val
        else:
            val = True
            return val
    else:
        val = False
        return val

anno = isYearLeap(1900)#almacenar la función en una variable

def daysInMonth(month):#validar si el mes es de 30,31 ó 28,29 si es biciesto o no
    if anno == True and month == 2:
        days=29
        print("Dias de: ", days)
    else:
        #meses de 30
        if month == 4 or month == 6 or month == 9 or month == 11:
            days = 30
            print("Dias de: ", days)
        #meses de 31
        elif month == 1 or month == 3 or month == 5 or month == 8 or month == 7 or month == 10 or month == 12:
            days = 31
            print("Dias de: ", days)   
        else:
            days=28
            print("Dias de: ", days)
    return days

#def dayOfYear(year, month, day):
#
# pon tu código nuevo aquí
#

#print(dayOfYear(2000, 12, 31))



        



#https://edube.org/learn/programming-essentials-in-python-part-1-spanish/laboratorio-d-iacute-a-del-a-ntilde-o-escribiendo-y-utilizando-tus-propias-funciones




