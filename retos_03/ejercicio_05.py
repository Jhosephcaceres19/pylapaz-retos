productos = input("Introduce los productos separados por coma: ").split(",")
precios = input("Introduce los precios separados por coma: ").split(",")

productos = [p.strip() for p in productos]
precios = [float(p.strip()) for p in precios]

empaquetado = list(zip(productos, precios))

total = sum(precios)

mas_caro = max(empaquetado, key=lambda x: x[1])[0]

mas_barato = min(empaquetado, key=lambda x: x[1])[0]

ordenados = [p[0] for p in sorted(empaquetado, key=lambda x: x[1])]

print(f"Total de la compra: {total}")
print(f"Producto más caro: {mas_caro}")
print(f"Producto más barato: {mas_barato}")
print(f"Productos ordenados por precio: {', '.join(ordenados)}")
