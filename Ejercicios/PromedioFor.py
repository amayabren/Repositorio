rango = int(input("Escriba cuantas notas: "))
notas = []
suma_notas = 0
cant_notas = 0

for i in range(rango):
    notita = int(input("Escriba su nota del 0 al 10: "))
    notas.append(notita)

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
