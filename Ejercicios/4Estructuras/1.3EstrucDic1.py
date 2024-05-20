"""3. Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento."""
datos = { }

datos["Nombre"] = str(input("Ingrese el nombre: "))
datos["Apellido"] = str(input("Ingrese un apellido: "))
datos["Dni"] = int(input("Ingrese el dni: "))
datos["Email"] = str(input("Ingrese el email: "))
datos["Fecha de nacimeinto"] = int(input("Ingrese la fecha de nacimiento "))

print(datos)