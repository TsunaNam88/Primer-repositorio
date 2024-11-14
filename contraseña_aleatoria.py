import random

# import string

""""
Generar una cadena aleatoria de caracteres con una longitud predeterminada
Usando la liibreria Random y la libreria String
libreria string:    string.ascii_letters
                    string.digits
                    string.punctuation
definimos una funcion 
creamos un for con la longitud
    funcion random.choice """


def generar_contrasena(longitud):
    caracteres = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&*+-/=@\_"
    )
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena


longitud = int(input("¿Cual es la longitud de la contraseña deseada?: "))

nueva_contrasena = generar_contrasena(longitud)
print("La nueva contraseña es", nueva_contrasena)
