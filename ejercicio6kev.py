tareasconjuntos = []


def agregar_t():
    description = input("Descripción: ")
    fecha = input("Fecha límite: ")
    prioridad = input("Prioridad: ")

    tarea = {
        "descripcion": description,
        "fecha": fecha,
        "prioridad": prioridad,
        "completa": False
    }

    tareasconjuntos.append(tarea)


def mostrartarea():
    if not tareasconjuntos:
        print("No hay tareas")
    else:
        for i, t in enumerate(tareasconjuntos):
            estado = "Completa" if t["completa"] else "No completada"
            print(f"{i} - {t['descripcion']} | {t['fecha']} | {t['prioridad']} | {estado}")


def eliminar_tarea():
    mostrartarea()
    try:
        i = int(input("Número de tarea a eliminar: "))
        tareasconjuntos.pop(i)
        print("Tarea eliminada")
    except:
        print("Error: índice inválido")


def completar_tarea():
    mostrartarea()
    try:
        i = int(input("Número de tarea completada: "))
        tareasconjuntos[i]["completa"] = True
        print("Tarea marcada como completada")
    except:
        print("Error: índice inválido")


while True:
    print("MENU")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Completar tarea")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        agregar_t()
    elif opcion == "2":
        mostrartarea()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        completar_tarea()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")