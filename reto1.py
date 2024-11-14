"""
Desarrollo de una aplicacion que envie un mensaje recordatorio que 
tienen libros pendientes por devolver

1. Solicitar al usuario que ingrese:
Nombre, titulo del libre que tiene pendiente, fecha vencimiento
2. Crear la funcion generar_recordatorio
"""


def generar_recordatorio():

    mensaje = (
        "Hola {0}, recuerda devolver el libro '{1}' antes del {2} de {3} de {4}".format(
            nombre,
            titulo_del_libro,
            fecha_de_venciemiento[0:2],
            fecha_de_venciemiento[3:5],
            fecha_de_venciemiento[6:10],
        )
    )
    return mensaje


nombre = input("¿Cual es tu nombre: ")
titulo_del_libro = input("A continuacion, indique el titulo del libro: ")
fecha_de_venciemiento = input(
    "Finalmente, indique la fecha de vencimiento (DD/MM/AAAA): "
)
# Llamando a la funcion generar_recordatorio
recordatorio = generar_recordatorio()
print(recordatorio)
