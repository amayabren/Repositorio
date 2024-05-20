#5.Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el 	
#usuario (input). Luego mostrar los datos de la tupla. Nota: para saber si el número i es par hacer i % 2 == 0

rango = int(input("Ingrese el valor n: "))
lista = [ ]
for i in range(rango):
    if i%2==0:
        lista.append(i)
    i +=1

tupla = tuple(lista)
print(tupla)