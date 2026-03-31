peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura * altura)

print("Su IMC es:", imc)

if imc < 18.5:
    print("Categoría: talla S")
elif imc < 25:
    print("Categoría: talla M")
elif imc < 30:
    print("Categoría: talla L")
else:
    print("Categoría: talla XL")