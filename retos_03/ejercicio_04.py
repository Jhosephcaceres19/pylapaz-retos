catalogo = (
    ("978-3-16-148410-0", "EL QUIJOTE", "Miguel de Cervantes", 1605),
    ("978-0-14-044913-6", "LA ODISEA", "Homero", -800),
    ("978-0-452-28423-4", "1984", "George Orwell", 1949),
    ("978-0-7432-7356-5", "EL GRAN GATSBY", "F. Scott Fitzgerald", 1925)
)

isbns = (
    "978-3-16-148410-0",
    "978-0-14-044913-6",
    "978-0-452-28423-4",
    "978-0-7432-7356-5"
)

isbn = input("Ingrese ISBN: ")



existe = isbn in isbns
resultado = (
    existe
    and catalogo[isbns.index(isbn)]
    or "Libro no encontrado."
)


salida = (
    isinstance(resultado, tuple)
    and f"Título: {resultado[1].title()}, Autor: {resultado[2]}, Año: {resultado[3]}"
    or resultado
)

print(salida)
