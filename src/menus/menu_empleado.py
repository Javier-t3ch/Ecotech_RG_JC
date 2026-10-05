from persistencia.empleado_dao import EmpleadoDAO
def mostrar_menu_empleado():
    print("\n===== ECOTECH =====")
    print("1. Registrar empleado")
    print("2. Listar empleados")
    print("3. Buscar empleado")
    print("4. Actualizar empleado")
    print("5. Eliminar empleado")
    print("0. Salir")


def main_empleado():
    while True:
        mostrar_menu_empleado()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            EmpleadoDAO.registrar_empleado()

        elif opcion == "2":
            EmpleadoDAO.listar_empleados()

        elif opcion == "3":
            EmpleadoDAO.buscar_por_id()

        elif opcion == "4":
            EmpleadoDAO.actualizar()

        elif opcion == "5":
            EmpleadoDAO.eliminar()

        elif opcion == "0":
            input(print("Hasta luego."))
            break

        else:
            print("Opción no válida.")
#revisar
if __name__ == "__main__":
    main()