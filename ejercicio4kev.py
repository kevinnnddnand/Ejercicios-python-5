con=input("Cree una contrasena:")

tiene_mayuscula = False
tiene_minuscula = False
tiene_numero = False
tiene_simbolo = False

for c in con:
    if c.isupper():
        tiene_mayuscula = True
    elif c.islower():
        tiene_minuscula = True
    elif c.isdigit():
        tiene_numero = True
    else:
        tiene_simbolo = True

if (len(con) >= 8 and
    tiene_mayuscula and
    tiene_minuscula and
    tiene_numero and
    tiene_simbolo):

    print("Contrasena valida")
else:
    print("Contrasena invalida")