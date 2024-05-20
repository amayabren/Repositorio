"""5. Un profesor de matemática necesita generar la tabla de multiplicar de un número 
entero comprendido entre 1 y 10. Por ejemplo para el 3 debería aparecer como salida:
3x1=3
3x2=6
3x3=9
…. y así hasta 10"""

num = int(input("Ingrese el num entre 1 y 10: "))

for i in range(11):
    if i != 0:
        print(f"{num}x{i}={i*num}")

