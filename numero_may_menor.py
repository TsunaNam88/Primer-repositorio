""""
encontrar el mayor de tres numeros
Pide ingresar 3 numeros
Crea una lista de los numeros agregados
usando la funcion Max aplicado a la lista
nos muestra el resultado"""

numero1 = input("Ingrese el primer numero: ")
numero2 = input("Ingrese el segundo numero: ")
numero3 = input("ingrese el tercer numero: ")

lista_de_nums = [numero1, numero2, numero3]
numero_mas_alto = max(lista_de_nums)
print(f"El numero mas alto es {numero_mas_alto}")
