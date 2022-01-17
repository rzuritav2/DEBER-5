#Primero
def primo(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

numero=int(input("Número: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")

#Segundo
def frecuencia(numero,digito):
    cantidad=0
    while numero!=0:
        ultDigito=numero%10
        if ultDigito==digito:
            cantidad+=1
        numero=numero//10
    return cantidad

num=int(input("Número: "))
un_digito=int(input("Dígito: "))
print("Frecuencia del dígito en el número:",frecuencia(num,un_digito))

#Tercero
def factorial():
    cantidad=0
    n=int(input("Número: "))
    while n!=-1:
        f=1
        if n!=0:
            for i in range(1,n+1):
                f=f*i
        print("Factorial:", f)
        cantidad+=1
        n=int(input("Número (-1 para cortar): "))
    return cantidad

#Cuarto
def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

cantidad=0
mayor=-1
numero=int(input("Número positivo: "))
while numero>=0:
    suma=sumaDigitos(numero)
    if suma > mayor:
            mayor=suma
            n_mayorsuma=numero
    if suma < 10:
        cantidad+=1
    numero=int(input("Número positivo: "))
print("Sumatoria de dígitos de",n_mayorsuma,":",mayor)
print("Cantidad con sumatoria menor a 10:",cantidad)
