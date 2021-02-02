
#Hola, para empezar con nuestro proyecto de red social, vamos a utilizar
#las herramientas que conocemos para ejecutar algunas acciones.
#
#Primero, mostraremos un mensaje en pantalla dando la bienvenida al usuario
#y escribiendo el nombre de la red.

#A continuación preguntaremos algunos datos al usuario para poder construir su perfil,
#y guardaremos esta información en variables.

#Finalmente, escribiremos en pantalla todos los datos que hemos recolectado, y permitiremos
#al usuario escribir un mensaje de estado.

#Te invito a examinar el código, leer los comentarios y comprender los tipos de datos
#que estamos utilizando en cada caso.


#Para conocer un poco más del usuario, vamos a preguntarle algunos datos.
#Por ejemplo, su año de nacimiento, y aprovecharemos este dato descubrir la edad del usuario.
#¿Cómo lo haremos?, usaremos una variable para guardar el resultado del cálculo de
#la edad del usuario. Este es un dato de tipo entero.

#A continuación le preguntaremos al usuario su estatura en metros. Este es un dato de tipo float,
#y usaremos esta información para calcular los centimetros

#Finalmente escribiremos en pantalla los datos que hemos recordado del usuario usando print y le solicitaremos
#que escriba un mensaje para desplegar en pantalla.

############################################################
# Lo primero que haremos será escribir un mensaje de bienvenida al usuario
# con el nombre de la red. Puedes modificar este mensajes para que represente el nombre de tu propia red
# Considera que al escribir """ también estamos delimitado un string, pero al hacerlo de esta manera,
# cambios de línea que ocurran en el código se considerarán como parte del string.
# Si no estás convencido, prueba el funcionamiento reemplazando los delimitadores por "
def mostrar_perfil():
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


def mostar_mensaje():
    print()
    print("--------------------------------------------------")
    print(nombre, "dice:", mensaje)
    print("--------------------------------------------------")

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

#Primera interacción. Solicitamos al usuario que ingrese su nombre,
#y lo guardamos en una variable de tipo str
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

#Segunda interacción. Solicitamos el ingreso del año, y utilizamos este
#dato para estimar la edad de la persona. ¿Por qué decimos que solo estamos "estimando" su edad?
#¿Qué ocurre si eliminamos la conversión a tipo de dato 'int' de la siguiente línea?
agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2017-agno-1
print()

#Tercera interacción. Solicitamos la estatura, medida en metros.
#Utilizamos la conversión a 'int', y una expresión para convertir esto
#a una medida en metros y centímetros
estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

#Cuarta interacción. Consultamos cuántos amigos tiene el usuario.
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

#Quinta interacción .
genero = str(input("Genero:"))
correo_electronico = str(input("Correo electronico:"))
telefono = str(input("Numero de telefono:"))
pais_residencia = str(input("Pais de Residencia:"))
ciudad = str(input("Ciudad:"))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
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
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True
salir = True
#Este ciclo se mantiene en ejecuciÃ³n hasta que el usuario desee salir
while continuar:

    #Solicitamos opciones al usuario
    print("1 - Escribir Mensaje")
    print("2 - Modificar Nombre")
    print("3 - Modificar Correo")
    print("S - Salir de Share-It")
    Opcion = str(input("Elije la opción"))

    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if Opcion == "1":
        mensaje = input("Vamos a publicar un mensaje. Â¿QuÃ© piensas hoy? ")
        mostar_mensaje()
    elif Opcion == "2":
        nombre = input("Dame tu nombre (actual " + nombre + "): ")
        mostrar_perfil()
    elif Opcion == "3":
        correo_electronico = input("Dame tu correo (actual " + correo_electronico + ": ")
        mostrar_perfil()
    elif Opcion == "S":
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




