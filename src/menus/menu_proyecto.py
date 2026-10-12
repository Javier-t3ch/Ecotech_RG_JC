from persistencia.proyecto_dao import ProyectoDao
#from src.main import main

def mostrar_menu_proyecto():
    print("\n===== ECOTECH =====")
    print("1. Registrar Proyecto")
    print("2. Listar  Proyecto")
    print("3. Buscar Proyecto")
    print("4. Actualizar Proyecto")
    print("5. Eliminar Proyecto")
    print("0. Salir")

def main_proyecto():
    while True:
        mostrar_menu_proyecto()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
                    ProyectoDao.registrar_proyecto()
        
        elif opcion == "2":
                    ProyectoDao.listar_proyectos()
        
        elif opcion == "3":
                    ProyectoDao.buscar_proyecto()
        
        elif opcion == "4":
                    ProyectoDao.actualizar_proyecto()
        
        elif opcion == "5":
                    ProyectoDao.eliminar_proyecto()
        
        elif opcion == "0":
                    input(print("Hasta luego."))
                    break
        
        else:
                    print("Opción no válida.")
    #revisar
if __name__ == "__main__":
        main_proyecto()