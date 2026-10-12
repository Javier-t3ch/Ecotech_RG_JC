# DOMINIOS
from dominio.departamento import Departamento
from dominio.proyecto import Proyecto
from dominio.Gestion_departamento import GestionDepartamento
from dominio.gestionPermisos import GestionPermisos
from dominio.registroTiempo import RegistroTiempo
from dominio.usuario import Usuario
from dominio.empleado import Empleado

# PERSISTENCIA
from persistencia.crear_bd import crear_tablas
from persistencia.empleado_dao import EmpleadoDAO

# MENUS
from menus.menu_empleado import main_empleado
from menus.menu_departamento import main_departamento
from menus.menu_proyecto import main_proyecto
from menus.menu_registroTiempo import main_RegistroTiempo

from menus.menu_dominio_empleado import menu_dominio_empleado

def main():
    while True:
        print("\n===== ECOTECH SOLUTIONS =====")
        print("1. Empleado")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_dominio_empleado()
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    #crear_tablas()
    main()