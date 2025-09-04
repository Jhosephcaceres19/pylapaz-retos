valores = {"True": True, "False": False }

entrada = input("Introduce True o False ")
resultado = valores[entrada]


# print(resultado )

valor = int(input("ingresa un numero de 1 a 100 "))

assert 0 <= valor <= 100, "numero fuera de rango"

print(resultado )
print(valor)

(resultado and valor < 30) and print("El sistema de riego no se activa")

(not resultado and valor > 30) and print("El sistema de riego no se activa")

(not resultado and valor <=30) and print("El sistema de riesgo se activa")




