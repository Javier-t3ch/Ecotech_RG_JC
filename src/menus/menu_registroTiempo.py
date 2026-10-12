from persistencia.registroTiempo_dao import RegistroTiempoDAO
#from src.main import main


def mostrar_menu_RegistroTiempo():
        print("\n===== ECOTECH =====")
        print("1. Registrar Registro de Tiempo")
        print("2. Listar Registros de Tiempo")
        print("3. Buscar Registro de Tiempo")
        print("4. Actualizar Registro de Tiempo")
        print("5. Eliminar Registro de Tiempo")
        print("0. Salir")

def main_RegistroTiempo():
        while True:
                mostrar_menu_RegistroTiempo()
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                        RegistroTiempoDAO.registrar_RegistroTiempo()
                elif opcion == "2":
                        RegistroTiempoDAO.listar_RegistroTiempo()
                elif opcion == "3":
                        RegistroTiempoDAO.buscar_RegistroTiempo()
                elif opcion == "4":
                        RegistroTiempoDAO.actualizar_RegistroTiempo()
                elif opcion == "5":
                        RegistroTiempoDAO.eliminar_RegistroTiempo()
                elif opcion == "0":
                        input(print("Hasta luego."))
                        break
                else:
                        print("Opción no válida.")
        #revisar
if __name__ == "__main__":
        main_RegistroTiempo()