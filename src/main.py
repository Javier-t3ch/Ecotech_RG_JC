# src/main.py
from dominio.empleado import Empleado
from dominio.departamento import Departamento
from dominio.proyecto import Proyecto


empleado_ana = Empleado(
    nombre="Ana Torres",
    correo="ana.torres@ecotech.cl"
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