import random
import string

longitud = int(input("Ingrese la Longitud de su pasword: "))

caracteres = string.ascii_letters + string.digits + "!@#$%"

password = ""

for i in range(longitud):
    password += random.choice(caracteres)

print("Contraseña generada:", password)