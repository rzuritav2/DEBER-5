#Primero
total=0
for i in range(101):
    total=total+i
print("Sumatoria:", total)

#Segundo
numero=int(input("Número:"))
f=1
if numero!=0:
    for i in range(1,numero+1):
        f=f*i
print("Factorial:", f)

#Tercer
n1=0
n2=1
print(n1)
print(n2)
for i in range(8):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3

#Cuarto
sumaNegativos=0
sumaPositivos=0
cantidadPositivos=0
for i in range(6):
    nro=int(input("Número: "))
    if nro>0:
        cantidadPositivos+=1
        sumaPositivos+=nro
    else:
        sumaNegativos+=nro
print("Sumatoria de los negativos: ", sumaNegativos)
if cantidadPositivos!=0:
    print("Promedio de los positivos: ",sumaPositivos/cantidadPositivos)
else:
    print("No se ingresaron números positivos")