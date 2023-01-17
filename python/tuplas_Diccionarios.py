#------------------------------------------
#tipos de secuencia /mutabilidad
#una secuencia es un tipo de dato que puede ser escaneado por el bucle for
tupla1 = (1, 2, 4, 8)
tupla2 = 1., .5, .25, .125

print(tupla1)
print(tupla2)

#------------------------------------------
#Tuplas ejemplos
miTupla = (1, 10, 100, 1000)

print(miTupla[0])
print(miTupla[-1])
print(miTupla[1:])
print(miTupla[:-2])

for elem in miTupla:
    print(elem)

#------------------------------------------
#Tuplas ejemplos 2

miTupla = (1, 10, 100)

t1 = miTupla + (1000, 10000)
t2 = miTupla * 3

print(len(t2))
print(t1)
print(t2)
print(10 in miTupla)
print(-10 not in miTupla)

#------------------------------------------
#Tuplas ejemplos 2
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)