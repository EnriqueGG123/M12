def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador("8.1")

f = open("texto-n.txt", "w")
f.write(input("Elije un numero de 1-10:"))
f.close()

