#1. Condicional parcial (solo el if) con expresión lógica simple
num = int(input("Ingrese un número: "))
if num < 10:
    print("Es menor a diez.")

#2. Condicional completo (if - else) con expresión lógica simple
num = int(input("Ingrese otro número: "))
if num < 10:
    print("Es menor a diez.")
else:
    print ("Es mayor a diez")

#3. Condicional parcial (solo el if) con expresión lógica compuesta (and)
num = int(input("Ingrese otro número: "))
if num > 5 and num < 10:
    print("El número está entre 5 y 10")

#4. Condicional completo (if - else) con expresión lógica compuesta (or)
num = int(input("Ingrese otro número: "))
if num == 7 or num == 8:
    print("El número es 7 u 8.")
else:
    print("El número no es 7 ni 8.")