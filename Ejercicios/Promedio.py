#calcular promedio de notas 
#segun el promedio el rendimiento es elevado >8, aceptable entre >=6 y <=8 y bajo >6
suma_notas = 0
cant_notas = 0
notas = []
tiene_nota = "s"
rend = "nada"
while tiene_nota == "s":
    notita = int(input("Escriba su nota: "))
    if notita <= 10 and notita >= 0:
        notas.append(notita)
    else:
        print("Tiene que ser entre 0 y 10.")
    tiene_nota = str(input("Tiene otra nota? s / n: "))

def promedio(x):
    prom = sum(x) / len(x)
    return prom

if promedio(notas) > 8:
        rend = "Elevado"
elif promedio(notas) >= 6 and promedio(notas) <= 8:
        rend = "Aceptable"
else:
        rend = "Bajo"


print(("El promedio es:"), promedio(notas), " y el rendimiento es", rend)
