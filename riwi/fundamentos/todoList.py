def agregar_tarea(lista_tareas):
    nombre_tarea = input("Ingrese el nombre de la tarea: ")
    tarea = {"tarea": nombre_tarea, "completada": False}
    lista_tareas.append(tarea)
    print("Tarea agregada con éxito.")


def modificar_tarea(lista_tareas):
    mostrar_tareas(lista_tareas)
    indice = int(input("Ingrese el número de la tarea que desea modificar: ")) - 1
    if 0 <= indice < len(lista_tareas):
        nombre_nuevo = input("Ingrese el nuevo nombre de la tarea: ")
        lista_tareas[indice]["tarea"] = nombre_nuevo
        print("Tarea modificada con éxito.")
    else:
        print("Índice de tarea fuera de rango.")


def eliminar_tarea(lista_tareas):
    mostrar_tareas(lista_tareas)
    indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
    if 0 <= indice < len(lista_tareas):
        del lista_tareas[indice]
        print("Tarea eliminada con éxito.")
    else:
        print("Índice de tarea fuera de rango.")


def verificar_tarea(lista_tareas):
    mostrar_tareas(lista_tareas)
    indice = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
    if 0 <= indice < len(lista_tareas):
        lista_tareas[indice]["completada"] = True
        print("Tarea marcada como completada.")
    else:
        print("Índice de tarea fuera de rango.")


def mostrar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas en la lista.")
    else:
        print("Lista de tareas:")
        for i, tarea in enumerate(lista_tareas, 1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}. {tarea['tarea']} - Estado: {estado}")


def main():
    lista_tareas = []
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar tarea")
        print("2. Modificar tarea")
        print("3. Eliminar tarea")
        print("4. Verificar tarea")
        print("5. Mostrar tareas")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            agregar_tarea(lista_tareas)
        elif opcion == "2":
            modificar_tarea(lista_tareas)
        elif opcion == "3":
            eliminar_tarea(lista_tareas)
        elif opcion == "4":
            verificar_tarea(lista_tareas)
        elif opcion == "5":
            mostrar_tareas(lista_tareas)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")


main()
