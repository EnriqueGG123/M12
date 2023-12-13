def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

separador("5.1")

import time

def Acabado(index):
    if (index + 1 == 5):
        print("¡Listos o no, ahí voy!")
    
for i in range(5):
    print(i + 1, "Mississippi")
    Acabado(i)

separador("5.2")

secreta = input("Cual es la palabra secreta: ")

while True:
    if secreta == "":
        continue
    elif secreta == "chupacabra":
        break

separador("5.3")

palabra = input("Ingresa una palabra: ")
palabra = palabra.upper()

for letra in palabra:
    if letra in ['A', 'E', 'I', 'O', 'U']:
        continue

    print(letra)

separador("5.4")

palabra = input("Ingresa una palabra: ")
palabra = palabra.upper()
nueva_palabra = ""

for letra in palabra:
    if letra in ['A', 'E', 'I', 'O', 'U']:
        continue

    nueva_palabra = nueva_palabra + letra

print(nueva_palabra)

separador("5.5")

invertido = float(input("Ingresa la cantidad a invertir: "))
interes = float(input("Ingresa la tasa de interés anual (en porcentaje): "))
num_años = int(input("Ingresa el número de años de la inversión: "))

decimal = interes / 100

for año in range(1, num_años + 1):
    capital_obtenido = invertido * (1 + decimal) ** año
    print(f"Año {año}: Capital obtenido = {capital_obtenido:.2f}")



separador("5.6")

altura_de_piramide = int(input("Alutra de la piramide de asteriscos: "))

for i in range(altura_de_piramide + 1):
    print('*' * i)

for i in range(altura_de_piramide + 1):
    for j in range(i * 2 - 1, 0, -2):
        print(j, end=' ')
    print()

separador("5.7")

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingresa un número entero: "))

if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")


separador("5.8")

palabra = input("Ingresa una palabra: ")

for letra in palabra[::-1]:
    print(letra)

separador("5.9")

frase = input("Ingresa una frase: ")
letra = input("Ingresa una letra: ")

contador = 0
for caracter in frase:
    if caracter == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces en la frase.")


separador("5.10")

bloques = int(input("Ingresa el número de bloques: "))

bloques_total = 0
altura = 0

while bloques_total <= bloques:
    altura += 1
    bloques_total += altura

if bloques_total > bloques:
    altura -= 1

print("La altura de la pirámide es:", altura)
