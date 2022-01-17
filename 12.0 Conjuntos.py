#Primero
A = set()
print(type(A))

#Segundo
A = [1,2,3]
print(A)

#Tercero
B = [1,2,3,1,2,3,1,2,3]
print(B)

#Cuarto
print(A == B)

#Quinto
numeros = [1,2,3,2,1,3,2,1,3,2,1,2,3]
print(numeros)

#Noveno
C = set(numeros)
print(C)

#Decimo
for n in A:
    print(n)

#OPERACIONES CON CONJUNTOS
#Primer
print(len(A))
print(3 in A)
print(4 in A)
print(4 not in A)

#Segundo
A.discard(9)
print(A.remove(1))
print(B.clear())

#Tercero
B.add(0)
B.add(9)
print(A == B)
print(A == B)
print(A | B)
print(A & B)
print(A < B)
print(A > B)