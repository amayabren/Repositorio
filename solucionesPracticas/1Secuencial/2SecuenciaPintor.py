#Un pintor de casas debe hacer un presupuesto para un cliente. Lo 
#que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El
#cliente le indica que necesita conocer el costo de mano de obra para pintar una
#pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro
#cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para
#pintar la pared.

ancho = int(input("Ingrese el ancho de la pared: "))
altura = int(input("Ingrese la altura de la pared: "))
montopormetro = int(input("Ingrese el costo por metro cuandrado: "))

metros = ancho * altura
costo = metros * montopormetro

print(f"El costo será de: ${costo}")