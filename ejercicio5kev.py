import random

numCPU=random.randint(1, 100)

while True:
    UserNum=int(input('Ingrese un num del 0 al 100:'))

    if numCPU >  UserNum:
        print('El numero es bajo')
    elif numCPU < UserNum:
        print('El numero es alto')
    else:
        print("Ganaste")
        break