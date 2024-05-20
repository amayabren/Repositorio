#Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que 
#el valor de lo que ingresa sea “fin”

nombre = str(input("Escriba el nombre: "))

while nombre != "fin":
    print(nombre)
    nombre = str(input("Escriba el nombre: "))