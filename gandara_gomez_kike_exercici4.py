def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador("4.1")

sueldo = float(input("Introduce el ingreso anual:"))

if sueldo <= 85528:
    impuesto = sueldo * 0.18 - 556.02
else:
    impuesto = 14839.02 + (sueldo - 85528) * 0.32

impuesto = round(max(impuesto, 0))

print("El impuesto es:", impuesto, "Euros")

separador("4.2")

año = int(input("Introduce un año:"))

if año < 1582:
    print("No dentro del período del calendario Gregoriano.")
else:
    if (año % 4 != 0) or (año % 100 == 0 and año % 400 != 0):
        print("Año normal")
    else:
        print("Año bi")

separador("4.3")

secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

user_guess = int(input("Ingresa tu suposición: "))

while user_guess != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    user_guess = int(input("Intenta nuevamente. Ingresa tu suposición: "))

print("¡Bien hecho, muggle! Eres libre ahora.")

separador("4.4")

NumeroPar = int(input("Elije un numero:"))

if (NumeroPar % 2) == 0:
    print("Es par")
else:
    print("Es impar")

separador("4.5")

Edad = int(input("Edad?"))
Ingresos = int(input("Ingresos?"))

if Edad >= 16 and Ingresos >= 1000:
    print("Tiene que tributar")
else:
    print("No tiene que tributar")

separador("4.6")

Sexo = input("H o M?")
Nombre = input("Nombre?")

if Sexo == "H" and Nombre > "N":
    print("B")
elif Sexo == "M" and Nombre < "M":
    print("A")

separador("4.7")

renta_anual = float(input("Ingresa tu renta anual en euros: "))

if renta_anual < 10000:
    tipo_impositivo = 5
elif 10000 <= renta_anual < 20000:
    tipo_impositivo = 15
elif 20000 <= renta_anual < 35000:
    tipo_impositivo = 20
elif 35000 <= renta_anual < 60000:
    tipo_impositivo = 30
else:
    tipo_impositivo = 45

print(f"Tu renta anual es de {renta_anual} euros, y tu tipo impositivo es del {tipo_impositivo}%.")

separador("4.8")

puntuacion = float(input("Ingresa tu puntuación de rendimiento: "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
    cantidad_dinero = 0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    cantidad_dinero = 2400 * puntuacion
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    cantidad_dinero = 2400 * puntuacion
else:
    nivel = "Puntuación no válida"
    cantidad_dinero = 0

if nivel != "Puntuación no válida":
    print(f"Tu nivel de rendimiento es {nivel} y recibirás {cantidad_dinero} euros.")
else:
    print("La puntuación ingresada no es válida.")

separador("4.9")

edad = int(input("Pon tu edad: "))

if edad < 4:
    precio_entrada = 0
elif 4 <= edad <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10

print(f"El precio de la entrada para una persona de {edad} años es de {precio_entrada} euros.")

separador("4.10")

opcion = input("¿Quieres una pizza vegetariana? (Sí/No): ").lower()

if opcion == "sí":
    print("Ingredientes vegetarianos disponibles:")
    print("1. Pimiento")
    print("2. Tofu")
else:
    print("Ingredientes no vegetarianos disponibles:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")

numero_ingrediente = int(input("Elige un ingrediente (ingresa el número): "))

if opcion == "sí":
    es_vegetariana = True
    ingredientes = ["Mozzarella", "Tomate"]
    if numero_ingrediente == 1:
        ingredientes.append("Pimiento")
    elif numero_ingrediente == 2:
        ingredientes.append("Tofu")
else:
    es_vegetariana = False
    ingredientes = ["Mozzarella", "Tomate"]
    if numero_ingrediente == 1:
        ingredientes.append("Peperoni")
    elif numero_ingrediente == 2:
        ingredientes.append("Jamón")
    elif numero_ingrediente == 3:
        ingredientes.append("Salmón")

print("\nTu pizza:")
print("Tipo: Vegetariana" if es_vegetariana else "Tipo: No Vegetariana")
print("Ingredientes:", ", ".join(ingredientes))

separador("4.11")

def determinar_clase_ip(ip):
    octetos = ip.split('.')

    primer_octeto = int(octetos[0])

    if 1 <= primer_octeto <= 126:
        clase = 'A'
    elif 128 <= primer_octeto <= 191:
        clase = 'B'
    elif 192 <= primer_octeto <= 223:
        clase = 'C'
    elif 224 <= primer_octeto <= 239:
        clase = 'D'
    elif 240 <= primer_octeto <= 255:
        clase = 'E'
    else:
        clase = 'No válida'

    return clase

def determinar_tipo_ip(clase, ip):
    if clase == 'A' and ip.startswith('10.'):
        tipo = 'Privada'
    elif clase == 'B' and ip.startswith('172.') and (16 <= int(ip.split('.')[1]) <= 31):
        tipo = 'Privada'
    elif clase == 'C' and ip.startswith('192.168.'):
        tipo = 'Privada'
    else:
        tipo = 'Pública'

    return tipo

ip = input("Ingrese la dirección IP: ")

clase = determinar_clase_ip(ip)

tipo = determinar_tipo_ip(clase, ip)

print(f"La dirección IP {ip} pertenece a la clase {clase} y es de tipo {tipo}.")
