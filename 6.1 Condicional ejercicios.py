class Condicionales:

#Primer ejercicio
    def valorAbsoluto(self):
        numero = int(input("Ingrese un numero: "))
        if numero < 0:
            numero = numero+-1
            print("El valor absoluto es ",numero)

#Segundo ejercicio
    def coincidencia(self):
        nombre1=input("Un nombre: ")
        nombre2=input("Otro nombre: ")
        indice_final_nombre1 = len(nombre1)-1
        indice_final_nombre2 = len(nombre2)-1
        if nombre1[0]==nombre2[0] or nombre1[indice_final_nombre1]==nombre2[indice_final_nombre2]:
            print("Coincidencia")
        else:
            print("No hay coincidencia")

#Tercer ejercicio
    def candidato(self):
        candidato=input("Candidato elegido: ")
        if candidato.upper()=="A":
            print("Usted ha votado por el partido rojo")
        elif candidato.upper()=="B":
            print("Usted ha votado por el partido azul")
        elif candidato.upper()=="C":
            print("Usted ha votado por el partido verde")
        else:
            print("Opcion erronea")

#Cuarto ejercicio
    def letra(self):
        letra = input("Letra: ")
        if len(letra)!=1:
            print("Debe ser solo una letra")
        else:
            if letra in "aeiou":
                print("Es vocal")

#Quinto ejercicio
    def bisiesto(self):
        año = int(input("Año: "))
        if año % 4 != 0:
            print("No es bisiesto")
        else:
            print("No es bisiesto")

cond = Condicionales()
cond.candidato()