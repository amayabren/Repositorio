agenda = { }
def menu():
    print("1. Agregar una persona (apellido, nombre, dni, email y número de teléfono).")
    print("2. Modificar una persona.")
    print("3. Eliminar una persona.")
    print("4. Mostrar agenda.")
    print("5. Salir.")

def opcion():
    op = int(input("Escriba su opción: "))
    return op

def agregar():
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        dni = input("Ingrese el dni: ")
        email = input("Ingrese el email: ")
        telefono = input("Ingrese el número de teléfono: ")
        agenda[dni] = {'nombre': nombre, 'apellido': apellido, 'email': email, 'telefono': telefono}

def modificar():
    dni = input("Ingrese el dni de la persona: ")
    print(agenda[dni])
    cambio = input("Ingrese qué campo desea cambiar: ")
    agenda[dni][f"{cambio}"] = input(f"Ingrese el nuevo {cambio}: ")

def eliminar():
     eliminar = input("Ingrese el dni de la persona que quiere elminar: ")
     print(agenda[eliminar])
     del agenda[eliminar]
     print("Eliminado.")

def mostrar():
     print(agenda)

ciclo = input("Abrir menu de opciones. s/n: ")
while ciclo == "s":
    menu()
    opcion_elegida = opcion()
    if opcion_elegida == 1:
         agregar()
    if opcion_elegida == 2:
         modificar()
    if opcion_elegida == 3:
         eliminar()
    if opcion_elegida == 4:
         mostrar()
    if opcion_elegida == 5:
        break

