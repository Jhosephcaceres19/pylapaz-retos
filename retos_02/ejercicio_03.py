frase = input("Introduce una frase: ")

cantidad_palabras = len(frase.split())

cantidad_vocales = (
    frase.lower().count("a")
    + frase.lower().count("e")
    + frase.lower().count("i")
    + frase.lower().count("o")
    + frase.lower().count("u")
    + frase.lower().count("á")
    + frase.lower().count("é")
    + frase.lower().count("í")
    + frase.lower().count("ó")
    + frase.lower().count("ú")
)

solo_letras = (
    frase.lower()
    .replace(" ", "")
    .replace(".", "")
    .replace(",", "")
    .replace("!", "")
    .replace("?", "")
    .replace(":", "")
    .replace(";", "")
    .replace("¿", "")
    .replace("¡", "")
)

es_palindromo = solo_letras == solo_letras[::-1]

print("Cantidad de palabras:", cantidad_palabras)
print("Cantidad de vocales:", cantidad_vocales)
print("Es palíndromo:", es_palindromo)
