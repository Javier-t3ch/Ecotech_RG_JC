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


def crear_empleado(nombre, cargo):
    return Empleado(
        nombre=nombre,
        direccion="Calle 123",
        numero="56912345678",
        correo=nombre.lower().replace(" ", "") + "@correo.cl",
        fecha_contrato="2026-10-12",
        salario=800000,
        cargo=cargo
    )


def probar_empleado():
    empleado = crear_empleado("Ana", "Recursos Humanos")
    proyecto = Proyecto("Sistema Web", "2026-10-01", "Proyecto de prueba")
    registro = RegistroTiempo(5, "2026-10-12", "Programacion", empleado, proyecto)

    horas = empleado.registrar_horas(registro)
    print("  Datos:", empleado.mostrar_datos())
    print("  Horas acumuladas:", horas)
    return empleado.ver_salario() == 800000 and horas == 5


def probar_departamento():
    departamento = Departamento("Tecnologia")
    encargado = crear_empleado("Carla", "Recursos Humanos")
    trabajador = crear_empleado("Pedro", "Programador")
    no_autorizado = crear_empleado("Luis", "Ventas")
    proyecto = Proyecto("Sistema Web", "2026-10-01", "Prueba")

    contratado = departamento.contratar_empleado(trabajador, encargado)
    repetido = departamento.contratar_empleado(trabajador, encargado)
    rechazado = departamento.contratar_empleado(no_autorizado, trabajador)
    creado = departamento.crear_proyecto(proyecto)
    editado = departamento.editar_proyecto(proyecto, "Sistema Actualizado")
    print("  Empleados:", departamento.cantidad_empleados())
    print("  Proyecto editado:", proyecto._nombre)

    # Estas pruebas comprueban los cambios de validacion que acordamos.
    sin_encargado = departamento.contratar_empleado(trabajador, None)
    proyecto_vacio = departamento.crear_proyecto(None)
    nombre_vacio = departamento.editar_proyecto(proyecto, "   ")

    return (contratado is True and repetido is False
            and rechazado is False and creado is True
            and editado is True and proyecto._nombre == "Sistema Actualizado"
            and sin_encargado is False and proyecto_vacio is False
            and nombre_vacio is False)


def probar_proyecto():
    empleado = crear_empleado("Pedro", "Programador")
    proyecto = Proyecto("App EcoTech", "2026-10-01", "Gestion de empleados")
    asignado = proyecto.asignar_empleado(empleado)
    duplicado = proyecto.asignar_empleado(empleado)
    registro = RegistroTiempo(6, "2026-10-12", "Diseno", empleado, proyecto)
    registrado = proyecto.agregar_registro_tiempo(registro)
    registro_repetido = proyecto.agregar_registro_tiempo(registro)
    informe = proyecto.generar_informe()
    print("  Informe:\n" + informe)

    return (asignado is True and duplicado is False
            and registrado is True and registro_repetido is False
            and "Horas registradas: 6" in informe)


def probar_registro_tiempo():
    ana = crear_empleado("Ana", "Programador")
    pedro = crear_empleado("Pedro", "Programador")
    proyecto_a = Proyecto("A", "2026-10-01", "Primero")
    proyecto_b = Proyecto("B", "2026-10-01", "Segundo")

    r1 = RegistroTiempo(5, "2026-10-10", "Tarea 1", ana, proyecto_a)
    r2 = RegistroTiempo(3, "2026-10-11", "Tarea 2", ana, proyecto_b)
    r3 = RegistroTiempo(4, "2026-10-12", "Tarea 3", pedro, proyecto_a)
    registros = [r1, r2, r3]

    total_ana = r1.calculo_horas(registros)
    total_ana_a = r1.calculo_horas_proyecto(registros, proyecto_a)
    print("  Horas de Ana:", total_ana)
    print("  Horas de Ana en proyecto A:", total_ana_a)
    return total_ana == 8 and total_ana_a == 5


def probar_usuario():
    empleado = crear_empleado("Ana", "Programador")
    usuario = Usuario("Ana", "ana@correo.cl", "ClaveSegura123", empleado)

    acceso_bueno = usuario.autenticar("ClaveSegura123")
    acceso_malo = usuario.autenticar("ClaveIncorrecta")
    cambio = usuario.cambiar_contrasenia("ClaveSegura123", "NuevaClave456")
    acceso_nuevo = usuario.autenticar("NuevaClave456")
    print("  Autenticacion correcta:", acceso_bueno)
    print("  Autenticacion incorrecta rechazada:", not acceso_malo)
    print("  Cambio de clave:", cambio)

    return (acceso_bueno is True and acceso_malo is False
            and cambio is True and acceso_nuevo is True
            and usuario._contrasenia_hash != "NuevaClave456")


def probar_gestion_permisos():
    empleado = crear_empleado("Ana", "Recursos Humanos")
    administrador = Usuario("Admin", "admin@correo.cl", "ClaveAdmin123", empleado)
    usuario = Usuario("Ana", "ana@correo.cl", "ClaveSegura123", empleado)
    gestion = GestionPermisos()
    # SOLO PARA ESTA PRUEBA: simula el permiso del administrador inicial.
    # No se debe usar esta asignacion directa en la aplicacion definitiva.
    administrador._permisos.append("administrar_permisos")
    otorgado = gestion.otorgar_permiso(administrador, usuario, "ver_informes")
    duplicado = gestion.otorgar_permiso(administrador, usuario, "ver_informes")
    rechazado = gestion.otorgar_permiso(usuario, administrador, "editar_usuarios")
    print("  Permiso otorgado:", otorgado)
    print("  Permiso duplicado rechazado:", not duplicado)
    print("  Usuario sin autorizacion rechazado:", not rechazado)
    return (otorgado is True and duplicado is False
            and rechazado is False and "ver_informes" in usuario._permisos)


def probar_gestion_departamento():
    gestion = GestionDepartamento()
    dpto = gestion.crear_departamento("Tecnologia")
    encontrado = gestion.buscar_departamento("tecnologia")
    duplicado = gestion.crear_departamento("TECNOLOGIA")
    editado = gestion.editar_departamento(dpto, "Informatica")
    encontrado_nuevo = gestion.buscar_departamento("informatica")
    eliminado = gestion.eliminar_departamento(dpto)
    print("  Departamento creado:", dpto._nombre)
    print("  Departamento editado:", editado)
    print("  Departamento eliminado:", eliminado)
    return (encontrado == dpto and duplicado is False
            and editado is True and encontrado_nuevo == dpto
            and eliminado is True and gestion.buscar_departamento("Informatica") is False)


def main():
    pruebas = [
        ("Empleado", probar_empleado),
        ("Departamento", probar_departamento),
        ("Proyecto", probar_proyecto),
        ("RegistroTiempo", probar_registro_tiempo),
        ("Usuario", probar_usuario),
        ("GestionPermisos", probar_gestion_permisos),
        ("GestionDepartamento", probar_gestion_departamento)
    ]
    aprobadas = 0
    for nombre, prueba in pruebas:
        print("\n=====", nombre, "=====")
        try:
            if prueba():
                print("[OK]", nombre)
                aprobadas += 1
            else:
                print("[FALLO]", nombre, "(resultado inesperado)")
        except Exception as error:
            print("[FALLO]", nombre, "-", error)
    print("\nRESULTADO FINAL:", aprobadas, "de", len(pruebas), "clases superaron sus pruebas basicas")


if __name__ == "__main__":
    main()










"""
def main():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestionar Empleados")
        print("2. Gestionar Departamentos")
        print("3. Gestionar Proyectos")
        print("4. Gestionar Registro de Tiempo")
        print("5. Salir")

        opcion = input("Selecciona una opcion")

        if opcion == "1":
            main_empleado()
        elif opcion == "2":
            main_departamento()
        elif opcion == "3":
            main_proyecto()
        elif opcion == "4":
            main_RegistroTiempo()
        elif opcion == "5":
            print("hasta Luego")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()






empleado_ana = Empleado(
    nombre= "Miguel Bosse",
    direccion= "Calle #123",
    numero= "56912345678",
    correo= "Miguelito_rico.negroBosse@correo.cl",
    fecha_contrato= "15/05/26",
    salario= 1232153,
    cargo= "Recursos Humanos"
)

EmpleadoDAO.insertar(empleado_ana)

encontrado = EmpleadoDAO.buscar_por_id(empleado_ana._id)
print("Encontrado:", encontrado)


print("Listado:")
for item in EmpleadoDAO.listar():
    print(item.mostrar_datos())

try:
    actualizado = EmpleadoDAO.actualizar(empleado_ana)

    if actualizado:
        print("Empleado actualizado correctamente.")
    else:
        print("Empleado no encontrado.")
except Exception:
    print(
        "no fue posible completar la operacion"
    )
"""