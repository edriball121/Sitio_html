
# Condicional IF - ELSE
print("Condicionales IF - ELSE")
valor = 11
if valor == 10:
    print("Este valor es igual a :" + str(valor));
else:
    print("Este valor es distinto de Diez, el valor es: " + str(valor));

# Validar igualdad (==)
print("Validar Operador igual a: (==)")
var = 0
print(var == 0);#True

var2 = 1
print(var2 == 0);#False

# Validar diferente (!=)
print("Validar operador diferente de (!=)")
var3 = 0
print(var3 != 0); #False

var4 = 1
print(var4 != 0); # True

#Validar mayor y menor que
print("Validar mayor y menor que (< ; >)")
n1 = 0
print(n1 > 0); #False

n2 = 2
print(n2 < 3); #True

n = int(input("Ingrese el valor de N "))

print("El valor de N es: " + str(n) + "¿N es mayor que 100? ");
print(n > 100)

print("El valor de N es: " + str(n) + "¿N es menor que 100? ")
print(n < 100)

#Ejemplos practicos
#------------------------------------------------------------
#1

#Valdiar menor, mayor ó igual que
print("Validar menor, mayor o igual que (>= ; <=)")
n3 = 0
print(n3 >= 0); #True

n4 = 1

print(n4 <= 3)

#------------------------------------------------------------
#2
#lee dos números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

#elegir el número más grande
if numero1> numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2

#imprimir el resultado
print("El número más grande es:", nmasGrande)

#--------------------------------------------------------------
#3
#lee tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))

#asumimos temporalmente que el primer número
#es el más grande
#lo verificaremos pronto
nmasGrande = numero1

#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero2 > nmasGrande:
    nmasGrande = numero2

#comprobamos si el tercer número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero3 > nmasGrande:
    nmasGrande = numero3

#imprimir el resultado
print("El número más grande es:", nmasGrande)

#-----------------------------------------------------------------
#4
# lee tres números
numero1 = int(input("Ingresa el primer número:"))
numero2 = int(input("Ingresa el segundo número:"))
numero3 = int(input("Ingresa el tercer número:"))

# verifica cuál de los números es el mayor
# y pásalo a la variable de mayor número

numeroMayor = max(numero1,numero2,numero3)

# imprimir el resultado
print("El número más grande es:", numeroMayor) 

#----------------------------------------------------------------
#5
palabra = input("Ingrese una palabra: ")

if palabra == "Espatifilo":
    print ("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
elif palabra == "espatifilo":
    print ("No, ¡quiero un gran Espatifilo!")
else:
    print ("¡Espatifilo! ¡No " + palabra + " !")

#----------------------------------------------------------------
#6

ingreso=float(input("Ingrese el ingreso anual:"))

if ingreso < 85528:
    impuesto = (0.18 * ingreso) - 556.2
    
    if impuesto <= 0:
        impuesto = 0
else: 
    impuesto = (0.32 * ingreso) - 14839
    if impuesto <= 0:
        impuesto = 0

impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")


#----------------------------------------------------------------
#6

año = int(input("Introduzca un año:"))

if año < 1582:
    print ("No dentro del período del calendario gregoriano")
else:
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                print('Año bisiesto')
            else:
                print('Año común')
        else:
            print('Año bisiesto.')
    else:
        print('Año común')


