#LISTAS
#Primero
numeros = []
print(numeros)
print(type(numeros))

#Segundo
numeros = [1,2,3]
print(numeros)

#Tercero
letras = list()
print(letras)

#Cuarto
letras = list("ABC")
print(letras)

#Quinto
print(list("ZXU"))

#Sexto
for i in range(len(letras)):
    print(letras[i])

#Septimo
i = 0
while i < len(letras):
    print(letras[i])
    i+=1

#Octavo
for elemento in letras:
    print(elemento)

#OPERACIONES CON LISTAS
#Primero
dir(list)
numeros + letras
print(numeros)
print(letras)
numeros+list(range(4,10))

#Segundo
C = numeros+[letras]
print(C)
print(len(C))
print(len(numeros+letras))
print(C[1])
print(type(C[1]))
print(C[3])
print(type(C[3]))
print(C[3:])
print(C[::-1])
print(C[3][1])
print(C[len(C)-1])
print(numeros[2])

#Tercer
print(C.index(2))
print(C[3].index("A"))
print("A" in C)
print("A" in C[3])
print(2 in C)
print(C.append([5,6]))

#TUPLAS
#Primero
dir(tuple)
tupla1 = ( )
print(tupla1)

#Segundo
tupla2 = ("ema")
print(tupla2)
print(type(tupla2))

#Tercero
tuple3 = tuple("ema")
print(tuple3)

#Cuarta
tuple4 = tuple(C)
print(tuple4)

#Quinta
nueva = tuple("abcdefg")
print(nueva)
nueva = ("A",)+nueva[1:]
print(nueva)

#Sexta
A = [1,2,3]
B = (A,)
print(A)
print(B)
print(A.append(4))
