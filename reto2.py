"""
Desarrollar una aplicacion para gestionar la asistencia
de una clase creando una funcion llamada calcular asitencia:

Esta funcion toma argumentos de una lista de estudiantes
Y con un diccionario mapea el nombre de cada estudiante y su estado de asistencia 

Args:

Str: Nombre del estudiante 
Boleano: True en caso de asistencia, en caso contrario False
 
Devuelve: 
El porcentaje de asistencia total de clase
Lista de estudiantes presentes

"""


def convertir_booleano(presente):
    """
    Funcion para convertir a booleano la entrada
    """
    return (
        True
        if presente.lower() == "si"
        else False if presente.lower() == "no" else None
    )


def alumnos():
    """
    recibir los datos de los alumnos y su estado
    """
    asistencias = {}

    while True:
        nombre = input(
            "Escriba salir para finalizar la lista\nIngrese el nombre del alumno: "
        )
        if nombre.lower() == "salir":
            break
        presente = input(f"{nombre} Asistio(si/no): ")
        asistencia = convertir_booleano(presente)
        if asistencia is None:
            print("Ingrese 'Si' o 'no' correctamente")
            continue
        asistencias[nombre] = asistencia
    print(asistencias)


alumnos()
