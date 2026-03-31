n = int(input("Ingrese un número positivo: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b