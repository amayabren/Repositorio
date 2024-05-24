"""4. En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos 
(nombre, apellido, dni, email, fecha de nacimiento)"""  
familia = { }
for i in range(4):
    print(f"Datos de la persona {i+1}.")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = input("Ingrese el dni: ")
    email = input("Ingrese el email: ")
    fecha = input("Ingrese la fecha de nacimiento: ")
    familia[nombre] = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Dni": dni,
        "Email":email,
        "Fecha de nacimiento":fecha
    }

print(familia)