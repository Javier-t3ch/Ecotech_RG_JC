from persistencia.departamento_dao import DepartamentoDAO
#from src.main import main

def mostrar_menu_departementos():
    print("\n===== ECOTECH =====")
    print("1. Registrar Departamento")
    print("2. Listar Departamentos")
    print("3. Buscar Departamento")
    print("4. Actualizar Departamento")
    print("5. Eliminar Departamento")
    print("0. Salir")

def main_departamento():
    while True:
        mostrar_menu_departementos()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
                    DepartamentoDAO.registrar_departamento()
        
        elif opcion == "2":
                    DepartamentoDAO.listar_departamento()
        
        elif opcion == "3":
                    DepartamentoDAO.buscar_departamento()
        
        elif opcion == "4":
                    DepartamentoDAO.actualizar_departamento()
        
        elif opcion == "5":
                    DepartamentoDAO.eliminar_departamento()
        
        elif opcion == "0":
                    input(print("Hasta luego."))
                    break
        
        else:
                    print("Opción no válida.")
    #revisar
if __name__ == "__main__":
        main_departamento()