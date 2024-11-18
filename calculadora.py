"""Convertir numeros romanos a enteros
Usando un diccionario de valores de los numeros romanos
Usando Reversed que lee los valores de reversa
Usando la funcion upper para convertir los Strings en mayus"""

romano = "CIV"


def convertir_numromano_a_entero(romano):
    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    previo = 0
    for simbolo in reversed(romano):
        valor = valores[simbolo]
        if valor < previo:
            total -= valor
        else:
            total += valor
        previo = valor
    return total


romano = input("Ingrese un numero romano: ")
romano = romano.upper()
numero_entero = convertir_numromano_a_entero(romano)
print(f"El numero romano {romano}, es igual a", numero_entero)
