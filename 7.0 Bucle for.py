for x in range(10):
    print(x)

for x in range(100,200):
    print(x)

for x in range(5,20,3):
    print(x)

n=int(input("Número: "))
for x in range(n, n*2):
    print(x)

c=int(input("Cantidad de números: "))
total=0
for variable in range(c):
    numero=int(input("Número: "))
    total+=numero
print("Total de la suma:", total)

frase=input("Frase: ")
print("Vocales en la frase:")
for x in "aeiou":
    if x in frase:
        print(x)

frase=input("Frase: ")
cantidad=0
for x in frase:
    if x in "aeiou":
        cantidad+=1
print("Cantidad de vocales:", cantidad)


