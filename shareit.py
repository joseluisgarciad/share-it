# Hola, para empezar con nuestro proyecto de red social, vamos a utilizar
# las herramientas que conocemos para ejecutar algunas acciones.
#
# Primero, mostraremos un mensaje en pantalla dando la bienvenida al usuario
# y escribiendo el nombre de la red.

# A continuación preguntaremos algunos datos al usuario para poder construir su perfil,
# y guardaremos esta información en variables.

# Finalmente, escribiremos en pantalla todos los datos que hemos recolectado, y permitiremos
# al usuario escribir un mensaje de estado.

# Te invito a examinar el código, leer los comentarios y comprender los tipos de datos
# que estamos utilizando en cada caso.


# Para conocer un poco más del usuario, vamos a preguntarle algunos datos.
# Por ejemplo, su año de nacimiento, y aprovecharemos este dato descubrir la edad del usuario.
# ¿Cómo lo haremos?, usaremos una variable para guardar el resultado del cálculo de
# la edad del usuario. Este es un dato de tipo entero.

# A continuación le preguntaremos al usuario su estatura en metros. Este es un dato de tipo float,
# y usaremos esta información para calcular los centimetros

# Finalmente escribiremos en pantalla los datos que hemos recordado del usuario usando print y le solicitaremos
# que escriba un mensaje para desplegar en pantalla.

############################################################
# Lo primero que haremos será escribir un mensaje de bienvenida al usuario
# con el nombre de la red. Puedes modificar este mensajes para que represente el nombre de tu propia red
# Considera que al escribir """ también estamos delimitado un string, pero al hacerlo de esta manera,
# cambios de línea que ocurran en el código se considerarán como parte del string.
# Si no estás convencido, prueba el funcionamiento reemplazando los delimitadores por "

import time
import os

nombre: str
edad: int
estatura: float
estatura_m: float
estatura_cm: float
num_amigos: int
genero: str
correo_electronico: str
telefono: str
pais_residencia: str
ciudad: str
agno: int = 0

def mostrar_perfil(nombre,
                   edad,
                   estatura_m,
                   estatura_cm,
                   num_amigos,
                   genero,
                   correo_electronico,
                   telefono,
                   pais_residencia,
                   ciudad):
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "años")
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
    print("Amigos:  ", num_amigos)
    print("Genero:  ", genero)
    print("Correo:  ", correo_electronico)
    print("Telefono:", telefono)
    print("Pais:    ", pais_residencia)
    print("Ciudad   ", ciudad)
    print("--------------------------------------------------")


def mostar_mensaje_publico(nombre, mensaje):
    print()
    print("--------------------------------------------------")
    print(nombre, "dice:", mensaje)
    print("--------------------------------------------------")


def mostrar_mensaje_amigos(nombre, amigos: list, mensaje):
    textoamigos = ""
    i = 0
    while (i < len(amigos)):
        textoamigos += amigos[i]
        textoamigos += ", "
        i += 1

    print()
    print("--------------------------------------------------")
    print(nombre, "dice:", textoamigos, " ", mensaje)
    print("--------------------------------------------------")


def borrarPantalla():  # Definimos la función estableciendo el nombre que queramos
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
    nombre = input("Para empezar, dime como te llamas. ")
    print()
    print("Hola ", nombre, ", bienvenido a Mi Red")
    print()
    return nombre


# Segunda interacción. Solicitamos el ingreso del año, y utilizamos este
# dato para estimar la edad de la persona. ¿Por qué decimos que solo estamos "estimando" su edad?
# ¿Qué ocurre si eliminamos la conversión a tipo de dato 'int' de la siguiente línea?
def actualizacion_anno(agno):
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


mostrar_logo()
nombre = actualizacion_nombre()
edad = actualizacion_anno(agno)
estatura_m, estatura_cm = actualizacion_estatura()
num_amigos = actualizacion_amigos()
genero = actualizar_genero()
correo_electronico = actualizar_correo()
telefono = actualizar_telefono()
pais_residencia = actualizar_pais()
ciudad = actualizar_ciudad()


# Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, genero,
               correo_electronico, telefono, pais_residencia, ciudad)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

# Usaremos una variable bool para indicar si el usuario desea continuar
# utilizando el programa o no
continuar = True
salir = True
# Este ciclo se mantiene en ejecuciÃ³n hasta que el usuario desee salir
while continuar:

    # Solicitamos opciones al usuario
    time.sleep(2)
    borrarPantalla()
    mostrar_logo()
    print("Share-it - ", nombre)
    print("1 - Escribir Mensaje Publico")
    print("2 - Escribir Mensaje solo a algunos amigos")
    print("3 - Mostrar datos de perfil")
    print("4 - Actualizar el perfil de usuario")
    print("0 - Salir de Share-It")
    Opcion = str(input("Elije la opción"))

    # Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if Opcion == "1":
        mensaje = input("Vamos a publicar un mensaje publico. Â¿QuÃ© piensas hoy? ")
        mostar_mensaje_publico(nombre, mensaje)
        time.sleep(2)
    elif Opcion == "2":
        lamigos = []
        mensaje = input("Vamos a publicar un mensaje para ellos:")
        print("Ingresa los nombres de tu amigos o amigas: (introduce 0 cuando termines) -> ")
        for i in range(num_amigos):
            print(" ", i, ": ")
            nombre_amigo = input()
            if nombre_amigo == "0":
                break
            else:
                lamigos.append(nombre_amigo)

        time.sleep(2)
        mostrar_mensaje_amigos(nombre, lamigos, mensaje)
    elif Opcion == "2":
        nombre = input("Dame tu nombre (actual " + nombre + "): ")
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, genero,
                       correo_electronico, telefono, pais_residencia, ciudad)
    elif Opcion == "3":
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, genero,
                       correo_electronico, telefono, pais_residencia, ciudad)
    elif Opcion == "4":
        nombre = actualizacion_nombre()
        edad = actualizacion_anno(agno)
        estatura_m, estatura_cm = actualizacion_estatura()
        num_amigos = actualizacion_amigos()
        genero = actualizar_genero()
        correo_electronico = actualizar_correo()
        telefono = actualizar_telefono()
        pais_residencia = actualizar_pais()
        ciudad = actualizar_ciudad()

        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, genero,
                       correo_electronico, telefono, pais_residencia, ciudad)
    elif Opcion == "0":
        print(Opcion)
        while salir:
            print(salir)
            salir = input("¿Desea salir?")
            if salir == "s" or salir == "S":
                print("Gracias por usar Mi Red. Â¡Hasta pronto!")
                salir = False
                continuar = False
    else:
        print("Selecciona una opción valida")
