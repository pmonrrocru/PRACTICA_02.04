sexo = input("Introduce tu sexo mujer/hombre: ")
nombre = input("introduce tu nombre: ")

if sexo == "mujer":
    if nombre[0].upper() < "M":
        print("Estas en el grupo: Gryffindor")
    else:
        print("Estas en el grupo: Slytherin")
else:
    if sexo == "hombre":
        if nombre[0].upper() > "N":
            print("Tu grupo es: Gryffindor")
        else:
            print("Tu grupo es: Slytherin")


