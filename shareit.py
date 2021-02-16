import time
import shareit_def as fun_red
import shareit_data as fun_files


nombre: str
edad: int = 0
estatura: float = 0.0
estatura_m: float = 0.0
estatura_cm: float = 0.0
num_amigos: int = 0
amigos: list = []
genero: str = ""
correo_electronico: str = ""
telefono: str = ""
pais_residencia: str = ""
ciudad: str = ""
agno: int = 0
muro = []

fun_red.mostrar_logo()
nombre = fun_red.actualizacion_nombre()
fun_red.mensaje_bienvenida(nombre)

if fun_files.existe_fichero(nombre):
    (nombre, edad, estatura_m, estatura_cm, num_amigos, amigos, genero, correo_electronico, telefono, pais_residencia, ciudad, muro) = fun_files.leer_fichero_datos(nombre)
else:
    (edad, estatura_m, estatura_cm, num_amigos, amigos, genero, correo_electronico, telefono, pais_residencia, ciudad) = fun_red.actualizar_perfil()


# Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
fun_red.bienvenida_usuario(nombre)
fun_red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, amigos, genero, correo_electronico,
                       telefono, pais_residencia, ciudad)
print("Actualizando datos...")
time.sleep(1)
fun_files.grabar_fichero_datos(nombre, edad, estatura_m, estatura_cm, num_amigos, amigos, genero, correo_electronico,
                               telefono, pais_residencia, ciudad, muro)
fun_red.agradecimiento_usuario()

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
    print("1 - Escribir Mensaje")  # se actualiza en los mensajes de los ficheros de todos mis amigos
    print("2 - Mostrar mi muro")  # consiste en leer los mensajes recuperados de las ultimas lineas del fichero
                                  # que han sido grabados por todos mis amigos "amigo dice: mensaje"
    print("3 - Mostrar datos de perfil")
    print("4 - Actualizar el perfil de usuario")
    print("5 - Agregar amigo")
    print("6 - Cambiar de usuario")
    print("0 - Salir de Share-It")
    Opcion = str(input("Elije la opción"))

    # Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if Opcion == "1":
        mensaje = input("Vamos a publicar un mensaje publico. Â¿QuÃ© piensas hoy? ")
        fun_red.mostar_mensaje_publico(nombre, mensaje)
        fun_red.publicar_mensaje(nombre, amigos, mensaje, muro)
        time.sleep(2)
    elif Opcion == "2":
        fun_red.mostrar_muro(muro)
        time.sleep(2)
    elif Opcion == "3":
        fun_red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, amigos, genero,
                               correo_electronico, telefono, pais_residencia, ciudad)
        fun_red.mensaje_bienvenida(nombre)
    elif Opcion == "4":
        edad, estatura_m, estatura_cm, num_amigos, amigos, genero, correo_electronico, \
        telefono, pais_residencia, ciudad = fun_red.actualizar_perfil()

        fun_files.grabar_fichero_datos(nombre, edad, estatura_m, estatura_cm, num_amigos, amigos, genero,
                                       correo_electronico, telefono, pais_residencia, ciudad, muro)
        fun_red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, amigos, genero,
                               correo_electronico, telefono, pais_residencia, ciudad)
        fun_red.mensaje_bienvenida(nombre)
    elif Opcion == "5":
        nuevo_amigo = input("Dame el nombre del nuevo amigo")
        amigos.append(nuevo_amigo)
        print("Hemos añadido a ", nuevo_amigo, " a tu lista de amigos")
        print()
        time.sleep(2)
        fun_red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, amigos, genero,
                               correo_electronico, telefono, pais_residencia, ciudad)
        fun_red.mensaje_bienvenida(nombre)
    elif Opcion == "6":
        fun_files.grabar_fichero_datos(nombre, edad, estatura_m, estatura_cm, num_amigos, amigos, genero,
                                       correo_electronico, telefono, pais_residencia, ciudad, muro)
        temp_nombre = fun_red.actualizacion_nombre()
        if fun_files.existe_fichero(temp_nombre):
            nombre = temp_nombre
            (nombre, edad, estatura_m, estatura_cm, num_amigos, amigos, genero, correo_electronico, telefono,
             pais_residencia, ciudad, muro) = fun_files.leer_fichero_datos(nombre)
            fun_red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, amigos, genero,
                                   correo_electronico, telefono, pais_residencia, ciudad)
        else:
            print("No hay datos creados para el perfil: ", temp_nombre, "!!!!")
            fun_red.bienvenida_usuario(temp_nombre)
            nombre = temp_nombre
            (edad, estatura_m, estatura_cm, num_amigos, amigos, genero, correo_electronico, telefono, pais_residencia, ciudad) = fun_red.actualizar_perfil()
            fun_files.grabar_fichero_datos(nombre, edad, estatura_m, estatura_cm, num_amigos, amigos, genero,
                                           correo_electronico, telefono, pais_residencia, ciudad, muro)

        fun_red.mensaje_bienvenida(nombre)
        fun_red.bienvenida_usuario(nombre)
        fun_red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, amigos, genero, correo_electronico,
                               telefono, pais_residencia, ciudad)

    elif Opcion == "0":
        print(Opcion)
        while salir:
            print(salir)
            salir = input("¿Desea salir?")
            if salir == "s" or salir == "S":
                fun_files.grabar_fichero_datos(nombre, edad, estatura_m, estatura_cm, num_amigos, amigos, genero,
                                               correo_electronico, telefono, pais_residencia, ciudad, muro)
                print("Gracias por usar Mi Red. Â¡Hasta pronto!")
                salir = False
                continuar = False
    else:
        print("Selecciona una opción valida")
