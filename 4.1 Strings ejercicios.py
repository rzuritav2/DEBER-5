#Primero
cadena = "si, profe, es cierto... yo me comi la tarea"
#¿Cuál es el resultado?
print(cadena[10])
print(cadena[-1])
print(cadena[0:9])
print(cadena[::3])
#¿Cómo obtener...?
print(cadena[::-1])
print(cadena[4:9])

#Segundo
s = "   hola, ¿cómo estás?"
print(s[::-1])
print(s[len(s)])
print(s.count("o"))
print(s.count("Hola"))
print(s[-4:])
print(s[15:])
print(s.find("o"))
print(s.strip)
x = s.upper()
print(x == s)
print(s[14:].upper())
print(len(s) % 2!=0)
print(s.replace(" ", "*"))
print(s.replace("z", "Z"))

#Algunas preguntas
X = "programar en python"
print(X[-1])
print(X[len(X)-1])

cadena = "hola"
print(cadena.find("2"))
print("a" in "datiles")
print("me gusta programar".find(" "))
print("me gusta programar".count(" "))

nueva = "C" + cadena [1:]
print(nueva)
X = "hoy es dia miercoles"
print(X.replace("i","i"))
print(X.replace("i","i").replace("é","e"))
print(X.count("a")+X.count("e")+X.count("i")+X.count("o")+X.count("u"))
