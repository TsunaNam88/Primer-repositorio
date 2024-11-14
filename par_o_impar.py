print("Trabajando en entorno virtual")

""""
Definir si un numero es par o impar
Pedir un numero al usuario
convertirlo a entero
Con modulo interpretar si el resto es 0
si lo es es, enviar el mensaje el numero es par 
si no, envia el mensaje el numero es impar"""
# def par_o_impar():

numero = input("indica un numero: ")
numero = int(numero)
if numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")
