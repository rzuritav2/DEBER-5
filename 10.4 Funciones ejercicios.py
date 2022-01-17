#Primero
def DNIvalido(dni):
    cantidad=0
    while dni!=0:
        cantidad=cantidad+1
        dni=dni//10
    return cantidad==7 or cantidad==8

#Segundo
def lenUltimaPalabra(cadena):
    longitud = len(cadena)
    if longitud==0:
        return 0
    cantidad=0
    for i in range(longitud):
        if cadena[i]!=' ':
            cantidad=cantidad+1
        else:
            if cadena[i]==" " and i<(longitud-1) and cadena[i+1]!=' ':
                cantidad=0
    return cantidad

#Tercero
def primerosTresDigitos(numero):
    while numero >= 1000:
        numero = numero / 10
    return int(numero)

def obtenerIdentificador(nombre, dni):
    nombre=nombre.strip()
    i=nombre[0:nombre.find(" ")]
    i=i+str(lenUltimaPalabra(nombre))
    i=i+str(primerosTresDigitos(dni))
    return i

#programa principal
nombre=input("Nombre del socio: ")
while nombre!="":
    dni=int(input("DNI del socio: "))
    while not(DNIvalido(dni)):
        print("Número inválido.")
        dni=int(input("DNI del socio: "))
    identificador = obtenerIdentificador(nombre,dni)
    print("El identificador del socio es: ",identificador)
    nombre=input("Nombre del socio: ")
