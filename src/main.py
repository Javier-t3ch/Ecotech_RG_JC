# src/main.py
from dominio.empleado import Empleado
from dominio.departamento import Departamento
from dominio.proyecto import Proyecto


empleado_ana = Empleado(
    id_empleado = "",
    nombre= "Ana Torres",
    direccion= "Calle #123",
    numero= "56912345678",
    correo= "ana.torres@correo.cl",
    fecha_contrato= "15/05/26",
    salario= 1232153,
    cargo= 1
)

empleado_javer = Empleado(
    id_empleado = "",
    nombre= "javier Torres",
    direccion= "Calle #123",
    numero= "56912345678",
    correo= "ana.torres@correo.cl",
    fecha_contrato= "15/05/26",
    salario= 1232153,
    cargo= 1
)

desarrollo = Departamento(
    nombre= "Departamento Finanzas"
)

empleado_p = Proyecto(
    nombre= "Proyecto: 'Alcatraz'"
    
)

dep1 = Departamento(
    nombre= "Departamento: Recursos Humanos,"
    )

Gerente = Departamento(
    nombre= "Nombre Gerente: Javier , "
)


# Uso desde main.py
desarrollo.agregar_empleado(empleado_ana)
print(desarrollo.cantidad_empleados())
for empleado in desarrollo.empleados:
    print(empleado.mostrar_datos())
    print(empleado_p.mostrar_datos())
    print(f"{dep1.nombre} ID DEPARTAMENTO: {dep1.id}") 
    print(f"{Gerente.nombre} ID GERENTE: {Gerente.id}")