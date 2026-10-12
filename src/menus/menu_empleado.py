from persistencia.empleado_dao import EmpleadoDAO
#from src.main import main
def mostrar_menu_empleado():
    print("\n===== ECOTECH =====")
    print("1. Registrar Empleado")
    print("2. Listar Empleados")
    print("3. Buscar Empleado")
    print("4. Actualizar Empleado")
    print("5. Eliminar Empleado")
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
            EmpleadoDAO.buscar_empleado()

        elif opcion == "4":
            EmpleadoDAO.actualizar_empleado()

        elif opcion == "5":
            EmpleadoDAO.eliminar_empleado()

        elif opcion == "0":
            input(print("Hasta luego."))
            break

        else:
            print("Opción no válida.")
#revisar
if __name__ == "__main__":
    main_empleado()