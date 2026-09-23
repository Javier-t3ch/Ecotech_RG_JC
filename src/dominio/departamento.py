from dominio.empleado import Empleado


class Departamento:
    contador_id = 0

    def __init__(self, nombre: str):
        Departamento.contador_id += 1
        self._id_departamento = f"D{Departamento.contador_id}"
        self._nombre = nombre
        self._empleados: list[Empleado] = []
        self._proyectos = []

    def contratar_empleado(self, empleado: Empleado, encargado: Empleado) -> bool:
        if encargado._cargo != "Recursos Humanos":
            return False
        if empleado in self._empleados:
            return False
        self._empleados.append(empleado)
        return True

    def agregar_empleado(self, empleado: Empleado) -> bool:
        if empleado in self._empleados:
            return False
        self._empleados.append(empleado)
        return True

    def eliminar_empleado(self, empleado: Empleado) -> None:
        if empleado not in self._empleados:
            return
        self._empleados.remove(empleado)

    def crear_proyecto(self, proyecto) -> bool:
        if proyecto in self._proyectos:
            return False
        self._proyectos.append(proyecto)
        return True

    def editar_proyecto(self, proyecto, nuevo_nombre: str) -> bool:
        if proyecto not in self._proyectos:
            return False
        proyecto._nombre = nuevo_nombre
        return True

    def eliminar_proyecto(self, proyecto) -> bool:
        if proyecto not in self._proyectos:
            return False
        self._proyectos.remove(proyecto)
        return True


    @property
    def empleados(self) -> tuple:
        return tuple(self._empleados)
    def cantidad_empleados(self) -> int:
        return len(self._empleados)












































































































































































































































































































