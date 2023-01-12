#-------------------Ciclo WHILE--------------------------------------
contador = 0
while contador < 20:
    contador += 1
    print("ciclo nro: " + str(contador))

#---------------------------------------------------------
#1
# Almacenaremos el número más grande actual aquí
numeroMayor = -999999999

# Ingresa el primer valor
numero = int(input ("Introduzca un número o escriba -1 para detener:"))

# Si el número no es igual a -1, continuaremos
while numero != -1:
    # ¿Es el número más grande que el número más grande?
    if numero > numeroMayor:
        # Sí si, actualiza el mayor númeroNúmero
        numeroMayor = numero
    # Ingresa el siguiente número
    numero = int (input("Introduce un número o escribe -1 para detener:"))

# Imprimir el número más grande
print("El número más grande es:", numeroMayor)

#---------------------------------------------------------
#2

# programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares
# programa termina cuando se ingresa cero

numerosImpares = 0
numerosPares = 0

# lee el primer número
numero = int (input ("Introduce un número o escriba 0 para detener:"))

# 0 termina la ejecución
while numero != 0:
    # verificar si el número es impar
    if numero % 2 == 1:
        # aumentar el contador de números impares
        numerosImpares += 1
    else:
        # aumentar el contador de números pares
        numerosPares += 1
    # lee el siguiente número
    numero = int (input ("Introduce un número o escriba 0 para detener:"))

# imprimir resultados
print("Números impares: ", numerosImpares)
print("Números pares: ", numerosPares)


#---------------------------------------------------------
#3

contador = 5
while contador != 0:
    print("Dentro del ciclo: ", contador)
    contador -= 1
print("Fuera del ciclo", contador)

#---------------------------------------------------------
#4



numeroSecreto = 777
numeroAdivinado = 0
print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
while numeroSecreto != numeroAdivinado:
    numeroAdivinado = int(input("Ingrese el número secreto"))
    
    if numeroSecreto == numeroAdivinado:
        print("¡Bien hecho, muggle! Eres libre ahora")
    
    if numeroSecreto != numeroAdivinado:
        print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")


#-------------------Ciclo FOR------------------------------------
#4 
#Range() define longitud del for iniciando en 0 hasta 99
# al Range se le puede agregar un 2do parametro el cual define desde hasta donde se ejecutara el for
# Range (2, 8) la salida sera: 2,3,4,5,6,7
# Range puede tener un tercer parametro el cual define la longitud de cada giro
# Range(1, 12, 3) Salida: 1,4,7,10
for i in range (100): 
    print("Ciclo Nro: " + str(i))
    pass

#---------------------------------------------------------------------------
#5

pow = 1
for exp in range(16):
    print ("2 a la potencia de", exp, "es", pow)
    pow * 2 

#---------------------------------------------------------------------------
#6
import time

for i in range(1,6):
    print(i, " Mississippi")
    time.sleep(1)

print("¡Listos o no, ahi voy!")

#---------------------------------------------------------------------------
#7

# break - ejemplo

print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

#---------------------------------------------------------------------------
#7

# continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

#---------------------------------------------------------------------------
#8
numeroMayor = -99999999
contador = 0

while True:
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))
    if numero == -1:
        break
    contador = 1
    if numero > numeroMayor:
        numeroMayor = numero

if contador != 0:
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número") 

#---------------------------------------------------------------------------
#9

numeroMayor = -99999999
contador = 0

numero = int (input("Ingresa un número o escribe -1 para finalizar el programa:"))

while numero != -1:
    if numero == -1:
        continue
    contador = 1

    if numero > numeroMayor:
        numeroMayor = numero
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))

if contador:
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número") 

#---------------------------------------------------------------------------
#9

while True:
    condicion = input ("Ingresa una palabra clave para salir del ciclo: ")
    if condicion == "chupacabra":
        print("Has dejado el ciclo con exito!")
        break


#---------------------------------------------------------------------------
#9

userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

for letra in userWord:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    else:
        print(letra)

#---------------------------------------------------------------------------
#10
       
i = 5
while i < 5:
    print (i)
    i += 1
else:
    print("else:", i)

#---------------------------------------------------------------------------
#11

for i in range(5):
    print(i)
else:
    print("else:", i)


