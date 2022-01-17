#Primero
A = dict()
print(A)

#Segundo
B = {}
print(B)

#Tercero
traducciones = {"hola":"hello","adios":"bye","dia":"day","noche":"night"}
print(traducciones)

#Cuarto
calendario = [("enero",1),("febrero",2),("marzo",3)]
meses = dict(calendario)
print(meses)
print(type(meses))

#Quinto
equipo = {8:["Molina",16,3], 2:["Lucia",14,1], 6:["Karen",15,2], 9:["Sonia",16,1]}
print(equipo)

#Sexto
for clave in traducciones.keys():
    print(clave)

#Septimo
print(traducciones.keys())
for valor in traducciones.values():
    print(valor)

#Octavo
for clave in traducciones.keys():
    print(clave, "==>", valor)

#Noveno
for datos in equipo.values():
    print(datos)
