#En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas (las notas van de 0 a 10) de los alumnos de un curso. 
#Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8), aceptable (el promedio está comprendido entre 6 y 8) o bajo (promedio 
#es inferior a 6). Desarrollar un algoritmo que resuelva este problema. Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen.

cant = int(input("Ingrese cuántos estudiantes rindieron: "))
suma = 0

for i in range(cant):
    nota = int(input("Ingrese nota: "))
    while nota > 10 or nota < 0:
        nota = int(input("La nota debe ser entre 0 y 10. Vuelva a ingresar la nota: "))
    suma += nota

def prom():
    promedio = suma / cant
    return promedio

def rend(promedio):
    if promedio > 8:
        return "Elevado"
    elif promedio >= 6:
        return "Acpetable"
    else:
        return "Bajo"

promedio = prom()
print(f"EL promedio es: {promedio}")
rendimiento = rend(promedio)
print(f"El rendimiento es: {rendimiento}")

