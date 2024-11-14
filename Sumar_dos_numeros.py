print("Prueba de entorno virtual")

""""
Pide dos datos
Intenta sumarlos convirtiendolos a int
Si lanza una excepcion envia un mensaje pidiendo solo numeros
Si todo sale bien se termina el bucle"""


def sumar_solo_numeros():
    while True:
        numero1 = input("Indica un numero: ")
        numero2 = input("indica un numero: ")
        try:
            suma = int(numero1) + int(numero2)
        except ValueError:
            print("Deben ser solo numeros")
        else:
            break

    print(f"La suma de {numero1} y {numero2} da como resultado")
    return suma


print(sumar_solo_numeros())
