#Un pintor de casas debe hacer un presupuesto para un cliente. Lo 
#que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El
#cliente le indica que necesita conocer el costo de mano de obra para pintar una
#pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro
#cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para
#pintar la pared.

metros = int(input("Ingrese los metros: "))
montopormetro = int(input("Ingrese el costo por metro cuandrado: "))

def total(metros, montopormetro):
    costo = metros * montopormetro
    print(costo)

print("El costo será de: ")
total(metros, montopormetro)
