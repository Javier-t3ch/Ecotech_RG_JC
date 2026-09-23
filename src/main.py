# src/main.py
from dominio.empleado import Empleado
from dominio.departamento import Departamento
from dominio.proyecto import Proyecto
from dominio.Gestion_departamento import GestionDepartamento
from dominio.gestionPermisos import GestionPermisos
from dominio.registroTiempo import RegistroTiempo
from dominio.usuario import Usuario
from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO




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