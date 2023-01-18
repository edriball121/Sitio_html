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

#------------------------------------------
#diccionarios
#------------------------------------------



dict = {
    "gato" : "chat", 
    "perro" : "chien", 
    "caballo" : "cheval"
    }
numerosTelefono = {
    'jefe' : 5551234567, 
    'Suzy' : 22657854310}
diccionarioVacio = {}

print(dict)
print(numerosTelefono)
print(diccionarioVacio)

print(dict['gato'])
print(numerosTelefono['Suzy'])

#------------------------------------------
#diccionarios in/not in

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'leon', 'caballo']

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "no está en el diccionario")


#------------------------------------------
#diccionarios / recorrer el diccionario
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dict.keys():
    print(key, "->", dict[key])

#------------------------------------------
#diccionarios / ordenar el diccionario
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in sorted(dict.keys()):
    print(key, "->", dict[key])

#------------------------------------------
#diccionarios / uso de items()
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for spanish, french in dict.items():
    print(spanish, "->", french)


#------------------------------------------
#diccionarios / uso de values()

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for french in dict.values():
    print(french)

#------------------------------------------
#diccionarios / editar
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict['gato'] = 'minou'
print(dict)

#------------------------------------------
#diccionarios / agregar

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict['cisne'] = 'cygne'
print(dict)
#diccionarios / agregar metodo update()
dict.update({"Lobo" : "Pet"})

#------------------------------------------
#diccionarios / eliminar

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

del dict['perro']
print(dict)
#diccionarios / elimina el ultimo elemento del diccionario
dict.popitem()
print(dict)

#------------------------------------------
#diccionarios y tupla
grupo = {}

while True:
    nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    calif = int(input("Ingresa la calificación del alumno (0-10): "))
    
    if nombre in grupo:
        grupo[nombre] += (calif,)
    else:
        grupo[nombre] = (calif,)
        
for nombre in sorted(grupo.keys()):
    sum = 0
    contador = 0
    for calif in grupo[nombre]:
        sum += calif
        contador += 1
    print(nombre, ":", sum / contador)

#------------------------------------------
#Varios ejemplos de tuplas


# Ejemplo 1
t1 = (1, 2, 3)
for elem in t1:
    print(elem)

# Ejemplo 2
t2 = (1, 2, 3, 4)
print(5 in t2)
print(5 not in t2)

# Ejemplo 3
t3 = (1, 2, 3, 5)
print(len(t3))

# Ejemplo 4
t4 = t1 + t2
t5 = t3 * 2

print(t4)
print(t5)

miTup = tuple((1, 2, "cadena"))
print(miTup)

lst = [2, 4, 6]
print(lst)    # salida: [2, 4, 6]
print(type(lst))    # salida: <class 'list'>
tup = tuple(lst)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # salida: <class 'tuple'>


tup = 1, 2, 3, 
lst = list(tup)
print(type(lst))    # outputs: <class 'list'>

#------------------------------------------
#Varios ejemplos de diccionarios

polEspDict = {
    "kwiat" : "flor",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

elemento1 = polEspDict["gleba"]    # ejemplo 1
print(elemento1)    # salida: tierra

elemento2 = polEspDict.get("woda")
print(elemento2)    # salida: agua


#------------------------------------------

polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

polEspDict["zamek"] = "cerradura"
item = polEspDict["zamek"]    # salida: cerradura 

#------------------------------------------
miDirectorioTelefonico = {}    # un diccionario vacio

miDirectorioTelefonico ["Adan"] = 3456783958    # crear o añadir un par clave-valor
print(miDirectorioTelefonico)    # salida: {'Adan': 3456783958}

del miDirectorioTelefonico ["Adan"]
print(miDirectorioTelefonico)    # salida: {}
#------------------------------------------
polEspDict = {"kwiat" : "flor"}

polEspDict = update({"gleba" : "tierra"})
print(polEspDict)    # salida: {'kwiat' : 'flor', 'gleba' : 'tierra'}

polEspDict.popitem()
print(polEspDict)    # outputs: {'kwiat' : 'flor'}
#------------------------------------------
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

for item in polEspDict:
    print(item)    # salida: zamek
                   #          woda
                   #          gleba
#------------------------------------------
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

for clave, valor in polEspDict.items():
    print("Pol/Esp ->", clave, ":", valor)
#------------------------------------------
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

if "zamek" in polEspDict:
    print("SI")
else:
    print("NO")
#------------------------------------------
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

print(len(polEspDict))    # salida: 3
del polEspDict["zamek"]    # elimina un elemento
print(len(polEspDict))    # salida: 2

polEspDict.clear()   # elimina todos los elementos
print(len(polEspDict))    # salida: 0

del polEspDict    # elimina el diccionario
#------------------------------------------
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

copyDict = polEspDict.copy()
#------------------------------------------