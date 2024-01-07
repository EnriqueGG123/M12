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

