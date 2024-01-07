def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador("6.1")

c0 = int(input("Elije un numero entero y positivo: "))
pasos = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    elif c0 % 2 == 1:
        c0 = 3 * c0 + 1
    
    pasos += 1
    print(f'En el paso: {pasos}, c0 = {c0}')

print(f'Para llegar a 1 se han necesitado {pasos} pasos!')

separador("Escenario 1")

hat_list = [1, 2, 3, 4, 5]

numero = int(input("Elije un numero para remplazar el central de la lista: "))
hat_list[len(hat_list)//2] = numero

hat_list.pop()

print("La lista mide:", len(hat_list))
print(hat_list)

separador("6.2")

beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Añade a la lista a Stu Sutcliffe, y Pete Best.")

for _ in range(2):
    miembro = input("Añade a un miembro: ")
    beatles.append(miembro)

if "Stu Sutcliffe" and "Pete Best" in beatles:
    del beatles[beatles.index("Stu Sutcliffe")]
    del beatles[beatles.index("Pete Best")]

beatles.insert(0, "Ringo Starr")

print(beatles)

separador("6.3")

# Ordenamiento burbuja
lista = []
while True:
    value = input("Elije un valor (fin para terminar de elegir): ")
    if value.lower() == 'fin':
        break
    lista.append(int(value))

for i in range(len(lista) - 1):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print("Lista ordenada:", lista)

separador("6.4")

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista_sin_dups = []

for numero in my_list:
    if (numero not in lista_sin_dups):
        lista_sin_dups.append(numero)

print("La lista con elementos únicos:")
print(lista_sin_dups)

separador("6.5")

numeros_de_lote = []

for _ in range(6):
    numero = int(input("Elije un número ganador de la loteria: "))
    numeros_de_lote.append(numero)

numeros_de_lote.sort()
print("Numeros ganadores:", numeros_de_lote)

separador("6.6")

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    nota = float(input(f"Nota de {asignatura}: "))
    if nota < 5.0:
        notas.append(asignatura)

print("Asignaturas que tienes que repetir:")
print(notas)

