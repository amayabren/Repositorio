puntos_empatado=1
puntos_ganado=3
semanas_num = int(input("Escriba la cantidad de semanas: "))
count = 0
puntos_total = 0

while count < semanas_num:
    empatado = int(input("Ingrese cuántos partidos empató: "))
    perdido = int(input("Ingrese cuántos partidos perdió: "))
    ganado = int(input("Ingrese cuántos partidos ganó: "))
    puntos_semana = (empatado*puntos_empatado) + (ganado*puntos_ganado)
    puntos_total= puntos_total + puntos_semana  
    count += 1
    if count < semanas_num:
        print("Siguiente semana...")

print(puntos_total)