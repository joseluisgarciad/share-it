import os.path as path
import os


def existe_fichero(nombre):
    if path.exists(os.getcwd() + "\\" + nombre.replace(" ", "").lower() + ".user"):
        return True
    else:
        return False


def leer_fichero_datos(nombre):
    # with open(nombre.replace(" ", "").lower() + ".user") as f:
    f = open(nombre.replace(" ", "").lower() + ".user", "r")
    edad = 0
    est_m = 0.0
    est_cm = 0.0
    namigos = 0
    amigos = []
    genero = ""
    correo = ""
    tlf = ""
    pais = ""
    ciudad = ""

    for linea in f:
        if linea[0:2] == "01":
            nombre = linea[3:-1]
        if linea[0:2] == "02":
            edad = linea[3:-1]
        if linea[0:2] == "03":
            est_m = linea[3:-1]
        if linea[0:2] == "04":
            est_cm = linea[3:-1]
        if linea[0:2] == "05":
            namigos = linea[3:-1]
        if linea[0:2] == "06":
            amigos = linea[3:-1].split()
        if linea[0:2] == "07":
            genero = linea[3:-1]
        if linea[0:2] == "08":
            correo = linea[3:-1]
        if linea[0:2] == "09":
            tlf = linea[3:-1]
        if linea[0:2] == "10":
            pais = linea[3:-1]
        if linea[0:2] == "11":
            ciudad = linea[3:-1]

    f.close()

    return nombre, edad, est_m, est_cm, namigos, amigos, genero, correo, tlf, pais, ciudad


def grabar_fichero_datos(nombre, edad, estatura_m, estatura_cm, num_amigos, amigos: list, genero, correo_electronico,
                         telefono, pais_residencia, ciudad):
    with open(nombre.replace(" ", "").lower() + ".user", 'w') as f:
        f.write("01 " + nombre + "\n")
        f.write("02 " + str(edad) + "\n")
        f.write("03 " + str(estatura_m) + "\n")
        f.write("04 " + str(estatura_cm) + "\n")
        f.write("05 " + str(num_amigos) + "\n")
        f.write("06 " + (" ".join(amigos)) + "\n")
        f.write("07 " + genero + "\n")
        f.write("08 " + correo_electronico + "\n")
        f.write("09 " + telefono + "\n")
        f.write("10 " + pais_residencia + "\n")
        f.write("11 " + ciudad + "\n")

    f.close()

#    for linea in f:
#        g.write(linea)
#    g.close()
#    f.close()
