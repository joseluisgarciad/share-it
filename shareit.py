import time
import os
import shareit_def as fun_red


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

fun_red.mostrar_logo()
nombre = fun_red.actualizacion_nombre()
edad = fun_red.actualizacion_anno(agno)
estatura_m, estatura_cm = fun_red.actualizacion_estatura()
num_amigos = fun_red.actualizacion_amigos()
genero = fun_red.actualizar_genero()
correo_electronico = fun_red.actualizar_correo()
telefono = fun_red.actualizar_telefono()
pais_residencia = fun_red.actualizar_pais()
ciudad = fun_red.actualizar_ciudad()

# Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
fun_red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, genero,
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
    fun_red.borrarpantalla()
    fun_red.mostrar_logo()
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
        fun_red.mostar_mensaje_publico(nombre, mensaje)
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

        fun_red.mostrar_mensaje_amigos(nombre, lamigos, mensaje)
        time.sleep(2)
    elif Opcion == "3":
        fun_red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, genero,
                               correo_electronico, telefono, pais_residencia, ciudad)
    elif Opcion == "4":
        fun_red.nombre = fun_red.actualizacion_nombre()
        fun_red.edad = fun_red.actualizacion_anno(agno)
        estatura_m, estatura_cm = fun_red.actualizacion_estatura()
        num_amigos = fun_red.actualizacion_amigos()
        genero = fun_red.actualizar_genero()
        correo_electronico = fun_red.actualizar_correo()
        telefono = fun_red.actualizar_telefono()
        pais_residencia = fun_red.actualizar_pais()
        ciudad = fun_red.actualizar_ciudad()

        fun_red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, genero,
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
