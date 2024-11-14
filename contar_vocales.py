frase = input("Ingrese una plabara o frase: ")
contador_vocales = 0
contador_numeros = 0
contador_espacios = 0
contador_consonantes = 0
contador_signos = 0
for letra in frase:
    if letra.lower() in "aeiou":
        contador_vocales += 1
    elif letra in "0123456789":
        contador_numeros += 1
    elif letra in " ":
        contador_espacios += 1
    elif letra.lower() in "bcdfghjklmnñpqrstvwxyz":
        contador_consonantes += 1
    elif letra in "!#$%&/()=;:,._-*/'\+<>?¡¿":
        contador_signos += 1
    else:
        print("Hay caracteres no revisados")

print(
    f"""El texto tiene {contador_vocales} vocales
      El texto tiene {contador_espacios} espacios
      El texto tiene {contador_numeros} numeros
      El texto tiene {contador_consonantes} consonantes
      El texto tiene {contador_signos} signos
      """
)
