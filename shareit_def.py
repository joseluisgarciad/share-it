import os

def bienvenida_usuario(usuario):
    print()
    print("Muy bien,", usuario, ". Entonces podemos crear un perfil con estos datos.")
    print("--------------------------------------------------")


def agradecimiento_usuario():
    print("--------------------------------------------------")
    print("Gracias por la información. Esperamos que disfrutes con Mi Red")
    print()


def mostrar_perfil(nombre,
                   edad,
                   estatura_m,
                   estatura_cm,
                   num_amigos,
                   amigos,
                   genero,
                   correo_electronico,
                   telefono,
                   pais_residencia,
                   ciudad):
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "años")
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
    print("Amigos:  ", num_amigos, ": ", ",".join(amigos)) #num_amigos, " - ", amigos)
    print("Genero:  ", genero)
    print("Correo:  ", correo_electronico)
    print("Telefono:", telefono)
    print("Pais:    ", pais_residencia)
    print("Ciudad   ", ciudad)
    print("--------------------------------------------------")


def actualizar_perfil():
    edad = actualizacion_anno()
    (estatura_m, estatura_cm) = actualizacion_estatura()
    num_amigos = actualizacion_amigos()
    amigos = actualizacion_lista_amigos(num_amigos)
    genero = actualizar_genero()
    correo = actualizar_correo()
    telefono = actualizar_telefono()
    pais = actualizar_pais()
    ciudad = actualizar_ciudad()


    return edad, estatura_m, estatura_cm, num_amigos, amigos, genero, correo, telefono, pais, ciudad


def mostrar_muro(muro:list):
    print("(=========== ", len(muro), " mensajes ===========)")
    for linea in muro:
        print(linea)


def publicar_mensaje(nombre, amigos, estado, muro: list):
    muro.append(estado)
    for amigo in amigos:
        archivo = open(amigo.replace(" ", "").replace(",", "").lower() + ".user", "a")
        archivo.write("12 Origen:" + nombre + " : " + estado + "\n")
        archivo.close()

def mostar_mensaje_publico(nombre, mensaje):
    print()
    print("--------------------------------------------------")
    print(nombre, "dice:", mensaje)
    print("--------------------------------------------------")


def mensaje_bienvenida(nombre):
    print()
    print("Hola ", nombre, ", bienvenido a Mi Red")
    print()


def mostrar_mensaje_amigos(nombre, amigos: list, mensaje):
    textoamigos = ""
    i = 0
    while i < len(amigos):
        textoamigos += amigos[i]
        textoamigos += ", "
        i += 1

    print()
    print("--------------------------------------------------")
    print(nombre, "dice:", textoamigos, " ", mensaje)
    print("--------------------------------------------------")


def actualizacion_lista_amigos(num_amigos):
    i = 0
    amigos = []

    print("Ingresa los nombres de tu amigos o amigas: (introduce 0 cuando termines) -> ")
    for i in range(num_amigos):
        nombre_amigo = input()
        if nombre_amigo == "0":
            break
        else:
            amigos.append(nombre_amigo)

    return amigos


def borrarpantalla():  # Definimos la función estableciendo el nombre que queramos
    if os.name == "posix" or os.name == "mac":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def mostrar_logo():
    print("Bienvenido a ... ")
    print("""
         ___          ___          ___          ___          ___                          ___     
        /\  \        /\__\        /\  \        /\  \        /\  \                  ___   /\  \    
       /::\  \      /:/  /       /::\  \      /::\  \      /::\  \                /\  \  \:\  \   
      /:/\ \  \    /:/__/       /:/\:\  \    /:/\:\  \    /:/\:\  \               \:\  \  \:\  \  
     _\:\~\ \  \  /::\  \ ___  /::\~\:\  \  /::\~\:\  \  /::\~\:\  \              /::\__\ /::\  \ 
    /\ \:\ \ \__\/:/\:\  /\__\/:/\:\ \:\__\/:/\:\ \:\__\/:/\:\ \:\__\          __/:/\/__//:/\:\__\_
    \:\ \:\ \/__/\/__\:\/:/  /\/__\:\/:/  /\/_|::\/:/  /\:\~\:\ \/__/         /\/:/  /  /:/  \/__/
     \:\ \:\__\       \::/  /      \::/  /    |:|::/  /  \:\ \:\__\           \::/__/  /:/  /     
      \:\/:/  /       /:/  /       /:/  /     |:|\/__/    \:\ \/__/            \:\__\  \/__/      
       \::/  /       /:/  /       /:/  /      |:|  |       \:\__\               \/__/             
        \/__/        \/__/        \/__/        \|__|        \/__/                             

    """)


# Primera interacción. Solicitamos al usuario que ingrese su nombre,
# y lo guardamos en una variable de tipo str
def actualizacion_nombre():
    nombre = input("Introduce el nombre del perfil. ")
    return (nombre)


# Segunda interacción. Solicitamos el ingreso del año, y utilizamos este
# dato para estimar la edad de la persona. ¿Por qué decimos que solo estamos "estimando" su edad?
# ¿Qué ocurre si eliminamos la conversión a tipo de dato 'int' de la siguiente línea?
def actualizacion_anno():
    agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    edad = 2017 - agno - 1
    return edad


# Tercera interacción. Solicitamos la estatura, medida en metros.
# Utilizamos la conversión a 'int', y una expresión para convertir esto
# a una medida en metros y centímetros
def actualizacion_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    estatura_m = int(estatura)
    estatura_cm = int((estatura - estatura_m) * 100)
    return estatura_m, estatura_cm


# Cuarta interacción. Consultamos cuántos amigos tiene el usuario.
def actualizacion_amigos():
    num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))
    return num_amigos


def actualizar_genero():
    genero = str(input("Genero:"))
    return genero


def actualizar_correo():
    correo_electronico = str(input("Correo electronico:"))
    return correo_electronico


def actualizar_telefono():
    telefono = str(input("Numero de telefono:"))
    return telefono


def actualizar_pais():
    pais_residencia = str(input("Pais de Residencia:"))
    return pais_residencia


def actualizar_ciudad():
    ciudad = str(input("Ciudad:"))
    return ciudad
