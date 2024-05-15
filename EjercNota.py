#Un estudiante está cursando 5 materias, tiene la nota de cada 
#materia y quiere saber cuál es su promedio."

nota1 = int(input("Escriba la primera nota: "))
nota2 = int(input("Escriba la segunda nota: "))
nota3 = int(input("Escriba la tercera nota: "))
nota4 = int(input("Escriba la cuarta nota: "))
nota5 = int(input("Escriba la quinta nota: "))


lista = []

lista.append(nota1)
lista.append(nota2)
lista.append(nota3)
lista.append(nota4)
lista.append(nota5)


def promedio(x):
    promedio_lista = sum(x) / len(x)
    return promedio_lista 


print(promedio(lista))
