# src/main.py
from dominio.departamento import Departamento
from dominio.proyecto import Proyecto
from dominio.Gestion_departamento import GestionDepartamento
from dominio.gestionPermisos import GestionPermisos
from dominio.registroTiempo import RegistroTiempo
from dominio.usuario import Usuario
from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO

"""""
crear_tablas()
empleado_ana = Empleado(
    nombre= "Ana Torres",
    direccion= "Calle #123",
    numero= "56912345678",
    correo= "ana.torres@correo.cl",
    fecha_contrato= "15/05/26",
    salario= 1232153,
    cargo= "Recursos Humanos"
)
print("Antes:", empleado_ana._id)
# None
EmpleadoDAO.insertar(empleado_ana)
print("Después:", empleado_ana._id)
# id generado por la BD
"""
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
