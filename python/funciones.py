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

def dayOfYear(year, month, day):
    #validar que la data ingresada sea valida
    #validar año bisiesto
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                val = True
                print(val)
            else:
                val = False
                print(val)
        else:
            val = True
            print(val)
    else:
        val = False#fin validar año bisiesto
        print(val)
    #Validar cuantos dias tiene el mes / febrero de 28 o 29 si es o no biciesto
    if val == True and month == 2:
        days=29
        print("Dias de: ", days)
    else:
        #meses de 30
        if month == 4 or month == 6 or month == 9 or month == 11:
            days = 30
            print("Dias de: ", days)
        #meses de 31
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            days = 31
            print("Dias de: ", days)   
        else:
            days=28
            print("Dias de: ", days)
    #Validar total de dias
    cantDias = [31,28,31,30,31,30,31,31,30,31,30,31] #definr lista con la cantidad de dias por mes
    if days == 29 or val == True: #definir dia para mes biciesto
        del(cantDias[1])
        cantDias.insert(1, 29)

    for i in range(month-1):
        totalDias += cantDias[i]
        
    totalDias += day
    print(totalDias)
    return totalDias

print("Total de dias: ", dayOfYear(2024, 3, 32))

#------------------------------------------
#4. función con parametros laboratorio final /es o no numero primo

def isPrime(num):
    primo = ""
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
        else:
            primo = True
            break

    return primo

print(isPrime(11))

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()


#------------------------------------------
#4. función con parametros laboratorio final / convertir gasolina

#El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. 
# Por ejemplo, en Europa, se muestra como la cantidad de combustible consumido por cada 100 kilómetros.
#En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.
#Tu tarea es escribir un par de funciones que conviertan l/100km a mpg(milas por galón), y viceversa.

#Las funciones:
#Se llaman l100kmampg y mpgal100km respectivamente.
#Toman un argumento (el valor correspondiente a sus nombres).
#Complementa el código en el editor.
#Ejecuta tu código y verifica si tu salida es la misma que la nuestra.
#Aquí hay información para ayudarte:
#1 milla = 1609.344 metros.
#1 galón = 3.785411784 litros.
#salida
#60.31143162393162
#31.36194444444444
#23.52145833333333
#3.9007393587617467
#7.490910297239916
#10.009131205673757


def l100kmtompg(liters):
    galon = liters*3.785411784
    return galon
def mpgtol100km(miles):
    distancia = miles*1609.344
    return distancia


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))

#------------------------------------------
#4. función con variables globales    
def miFuncion():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)

var = 1
miFuncion()
print(var)

#------------------------------------------
#4. función asignar valores a variables y/o listas fuera de la función   
def miFuncion(miLista1):
    print(miLista1)
    del miLista1[0]

miLista2 = [2, 3]
miFuncion(miLista2)
print(miLista2)

#------------------------------------------
#4. función IMC

def piespulgam(pies, pulgadas = 0.0):
    return pies * 0.3048 + pulgadas * 0.0254


def lbsakg(lb):
    return lb * 0.45359237


def imc(peso, altura):
    #el \ significa que el codigo continua en la proxima linea
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    
    return peso / altura ** 2


print(imc(peso = lbsakg(176), altura = piespulgam(5, 7)))


#------------------------------------------
#4. función triangulo


def esUnTriangulo (a, b, c):
    return a + b > c and b + c > a and c + a > b

print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))

def esUnTrianguloRectangulo(a, b, c):
    if not esUnTriangulo  (a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

print(esUnTrianguloRectangulo(5, 3, 4))
print(esUnTrianguloRectangulo(1, 3, 4))



#------------------------------------------
#4. función triangulo 2da parte

def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def campoTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return None
    return heron(a, b, c)

print(campoTriangulo(1., 1., 2. ** .5))


#------------------------------------------
#4. función factoriales
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    producto = 1
    for i in range(2, n + 1):
        producto *= i
    return producto

for n in range(1, 6): # probando
    print(n, factorialFun(n))


#------------------------------------------
#4. función fibonasi
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # probando
    print(n, "->", fib(n))

#------------------------------------------
#4. función fibonasi 2do metodo

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)

#------------------------------------------
#4. función recursividad
# Implementación recursiva de la función factorial
def factorial(n):
    if n == 1:    # la condición de terminación
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4)) # 4 * 3 * 2 * 1 = 24

#https://edube.org/learn/programming-essentials-in-python-part-1-spanish/laboratorio-d-iacute-a-del-a-ntilde-o-escribiendo-y-utilizando-tus-propias-funciones




