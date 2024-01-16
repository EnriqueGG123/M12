import os.path

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador("8.1")

def generarTablaMul(numero):
    resultado = ""

    for i in range(10):
        mul = int(numero) * i + 1
        resultado = resultado + '{numero1} x {i1} = {mul1}'.format(numero1 = numero, i1 = i + 1, mul1 = mul) + "\n"

    return resultado


def guardarTabla(numero):
    f = open("texto-" + numero + ".txt", "w")
    f.write(generarTablaMul(numero))
    f.close()

guardarTabla(input("Elije un numero de 1-10:"))

separador("8.2")

def existeTabla(numarchivo):
    if (os.path.isfile("texto-" + numarchivo + ".txt")):
        archivo = open("texto-" + numarchivo + ".txt", "r")
        print(archivo.read())
        archivo.close()
    else:
        print("No existe el archivo!")

existeTabla(input("Elije un numero de 1-10:"))

separador("8.3")

n1, m1 = input("Elije un numero de 1-10:"), int(input("Elije otro numero de 1-10:"))

def darLineaTabla(n, m):
    if (os.path.isfile("texto-" + n + ".txt")):
        with open("texto-" + n + ".txt", "r") as fp:
            x = fp.readlines()[m - 1]
            print(x)
    else:
        print("No existe el archivo!")

darLineaTabla(n1, m1)

separador("8.4")

print("\n\n\n\n\n\nNO FUNCIONA EL LINK!\n\n\n\n\n\n")

separador("8.5")

import os

def crear_listin():
    if not os.path.exists('listin.txt'):
        with open('listin.txt', 'w'):
            pass

def consultar_telefono(nombre):
    with open('listin.txt', 'r') as file:
        for line in file:
            current_nombre, telefono = line.strip().split(',')
            if current_nombre == nombre:
                return telefono
    return f'No hay el teléfono para {nombre}'

def agregar_cliente(nombre, telefono):
    with open('listin.txt', 'a') as file:
        file.write(f'{nombre},{telefono}\n')
    print(f'Añadido el telefono de {nombre}')

def eliminar_cliente(nombre):
    with open('listin.txt', 'r') as file:
        lines = file.readlines()

    with open('listin.txt',  'w') as file:
        for line in lines:
            current_nombre, _ = line.strip().split(',')
            if current_nombre != nombre:
                file.write(line)
    print(f'Se ha eliminado el telefono de {nombre}')

# Ejemplo de uso
crear_listin()

while True:
    print("\n1. Consultar telefono")
    print("2. Añadir un cliente")
    print("3. Eliminar un cliente")
    print("4. Salir")

    opcion = input("Selecciona una opcion (1/2/3/4): ")

    if opcion == '1':
        nombre = input("Nombre del cliente: ")
        print(consultar_telefono(nombre))
    elif opcion == '2':
        nombre = input("Nombre del nuevo cliente: ")
        telefono = input("Teléfono del nuevo cliente: ")
        agregar_cliente(nombre, telefono)
    elif opcion == '3':
        nombre = input("Nombre del cliente a eliminar: ")
        eliminar_cliente(nombre)
    elif opcion == '4':
        break
    else:
        print("Opcion no vvlida. Intentalo de nuevo.")

separador("8.6")

import re

def pedir_credenciales():
    while True:
        usuario = input("Nombre del usuario (mínimo 6 caracteres): ")
        if len(usuario) >= 6:
            break
        else:
            print("Nombre ded usuario debe tener al menos 6 caracteres.")

    while True:
        contrasena = input("Mete la contraseña (minimo 8 caracteres, al menos una mayuscula y una minuscula): ")
        if len(contrasena) >= 8 and re.search("[a-z]", contrasena) and re.search("[A-Z]", contrasena):
            break
        else:
            print("La contraseña debe tener al menos 8 caracteres una mayuscula y una minuscula.")

    return usuario, contrasena

def registrarse():
    usuario, contrasena = pedir_credenciales()
    with open("users.txt", "a") as file:
        file.write(f"{usuario},{contrasena}\n")
    print("Usuario registrado y guardado en el registro")

def login():
    usuario, contrasena = pedir_credenciales()
    with open("users.txt", "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(',')
            if usuario == stored_user and contrasena == stored_pass:
                print("Has iniciado sesion")
                return
    print("Usuario o contraseña incorrectos")

def menu():
    while True:
        print("\Menu:")
        print("1. Registrar")
        print("2. Iniciar sesion maquina")
        print("3. Enga hasta luego")

        opcion = input("Seleccione una de estas :) (1, 2, 3): ")

        if opcion == "1":
            registrarse()
        elif opcion == "2":
            login()
        elif opcion == "3":
            print("Deu")
            break
        else:
            print("?")

menu()