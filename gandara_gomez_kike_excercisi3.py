def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

separador("3.1")

Nombre = input('Como te llamas?')

print('Hola', Nombre + "!")

separador("3.2")

Juan = 3
María = 5
Adan = 6

print(Juan, ",", María, ",", Adan)

total_manzanas = Juan + María + Adan

print(total_manzanas)

manzanas_perdidas = 4

manzanas_finales = total_manzanas - manzanas_perdidas

print(manzanas_finales)

separador("3.3")

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.60934
kilometers_to_miles = kilometers * 0.621371

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

separador("3.4")

x =  1 # codifica aquí tus datos de prueba
x = float(x)
# escribe tu código aquí

X3 = ((x * 3)**3)
X2 = ((x * 2)**2) 

y = (X3 - X2 + (x * 3) - 1)

print("y =", y)

separador("3.5")

Horas_Trabajadas = int(input('Cuantas horas has trabajado?'))
Por_Hora = int(input('Cuanto cobras la hora?'))

print(Por_Hora * Horas_Trabajadas)

separador("3.6")

n = int(input('Elije el numero: '))
suma = (n * (n + 1)) // 2

print(suma)

separador("3.7")

Peso = int(input('Cuanto pesas?'))

# La estatura debe tener un formato de metros.centimetros
Estatura = float(input('Cuanto mides?'))

IMC = Peso / (Estatura ** 2)

print(IMC)

separador("3.8")

cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
tasa_interes_anual = float(input("Ingrese la tasa de interés anual (%): "))
num_años = int(input("Ingrese el número de años de la inversión: "))

tasa_interes_decimal = tasa_interes_anual / 100 
capital_obtenido = cantidad_invertir * (1 + tasa_interes_decimal)**num_años

print(f"El capital obtenido en la inversión después de {num_años} años es: {capital_obtenido:.2f}")

separador("3.9")

byte1 = int(input("Ingrese el primer byte de la dirección IP: "))
byte2 = int(input("Ingrese el segundo byte de la dirección IP: "))
byte3 = int(input("Ingrese el tercer byte de la dirección IP: "))
byte4 = int(input("Ingrese el cuarto byte de la dirección IP: "))

direccion_ip = f"{byte1}.{byte2}.{byte3}.{byte4}"

print(f"La dirección IP es: {direccion_ip}")

separador("3.10")

hora = int(input("Hora de inicio (0-23): "))
minutos = int(input("Minuto de inicio (0-59): "))
duracion = int(input("Duración del evento (minutos): "))
dia = int(input("Día (1-30): "))
dia_orig = dia

minutos_totales = (hora * 60 + minutos + duracion) % (24 * 60)  # Se hace % para las horas despues de las 00:00
hora_final = minutos_totales // 60
minutos_finales = minutos_totales % 60

if hora == 23 and (minutos + duracion >= 60):
    dia += 1

if dia > 30:
    dia = 1

if (((duracion / 60) / 60) // 1 - 1) >= 1:
    dia += int(((duracion / 60) / 60) // 1 - 1)

print(f"El evento comenzando el día {dia_orig} a las {hora:02d}:{minutos:02d} y durando {duracion} minutos, terminará el día {dia} a las {hora_final:02d}:{minutos_finales:02d}.")