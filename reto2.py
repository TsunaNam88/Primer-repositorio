"""
Desarrollar una aplicacion para gestionar la asistencia
de una clase creando una funcion llamada calcular asitencia:

Esta funcion toma argumentos de una lista de estudiantes
Y con un diccionario mapea el nombre de cada estudiante y su estado de asistencia 

Args:

nombre (str): Nombre del estudiante 
asistencia (Boleano): True en caso de asistencia, en caso contrario False
 
Devuelve: 
int: El porcentaje de asistencia total de clase
str: Lista de estudiantes presentes

"""


def convertir_booleano(presente):
    """
    Funcion para convertir a booleano la entrada
    """
    cierto = {"si", "s", "i", "yes", "y", "1"}
    falso = {"no", "n", "o", "0"}
    return (
        True
        if presente.lower() in cierto
        else False if presente.lower() in falso else None
    )


def alumnos():
    """
    recibir el nombre del alumno y su estado de asistencia
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
    return asistencias


def calcular_asistencia(asistencias):
    """
    Calcular el porcentaje de los alumnos
    Imprimir la lista de quien asistio
    """
    num_de_estudiantes = len(asistencias)
    contar_asistencia = sum(1 for estado in asistencias.values() if estado is True)
    porcentaje = (
        (contar_asistencia / num_de_estudiantes) * 100 if num_de_estudiantes > 0 else 0
    )
    print(f"Porcentaje de asistencia: {porcentaje:.2f}%")
    alumnos_con_asistencia = [
        alumno for alumno, estado in asistencias.items() if estado is True
    ]
    print(f"Los alumnos que asistieron son: {alumnos_con_asistencia}")


asistencias = alumnos()
calcular_asistencia(asistencias)
