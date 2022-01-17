#Primer ejercicio
N = input("Tú nombre: ")
print("Ahora estas en la matrix, ", N)

#Segundo ejercicio
costo = float(input("Costo de la cena: $"))
servicio = costo*0.062
propina = costo*0.1
print("Costo total de la comida: $",costo+servicio+propina)

#Tercer ejercicio
dia = int(input("Dia tu nacimiento: "))
mes = int(input("Mes tu nacimiento: "))
año = int(input("Año tu nacimiento: "))
print(dia,"/",mes,"/", año)

#Cuarto ejercicio
fecha = int(input("Ingrese una fecha en formato ddmmaaaa: "))
año = fecha % 10000
dia= fecha // 1000000
mes= (fecha // 10000) % 100
print(dia,"/",mes,"/", año)

#Quinto ejercicio
fecha = int(input("Ingrese una fecha en formato ddmmaaaa: "))
dia = fecha [:2]
mes= fecha [2:4]
año= fecha [4:]
print(dia,"/",mes,"/", año)

#Sexto ejercicio
capacidad = float(input("Capacidad del tanque: "))
kmlx = float(input("Rendimiento (Km totales a recorrer: "))
recorrido = float(input("Km totales ha recorrer: "))
kmxtanque = capacidad * kmlx
print("Seran necesarios", recorrido/kmxtanque, "tanques.")



