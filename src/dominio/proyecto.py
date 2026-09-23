class Proyecto:
    def __init__(self, id_proyecto, nombre, fecha_inicio, descripcion):
        self._id_proyecto = id_proyecto
        self._nombre = nombre
        self._fecha_inicio = fecha_inicio
        self._descripcion = descripcion
        self._empleados = []
        self._registros_tiempo = []

    def asignar_empleado(self, empleado):
        if empleado not in self._empleados:
            self._empleados.append(empleado)
            return True
        return False

    def desvincular_empleado(self, empleado):
        if empleado in self._empleados:
            self._empleados.remove(empleado)
            return True
        return False

    def agregar_registro_tiempo(self, registro):
        self._registros_tiempo.append(registro)
        return True

    def generar_informe(self):
        return (
            f"Proyecto: {self._nombre}\n"
            f"Descripción: {self._descripcion}\n"   
            f"Cantidad de empleados: {len(self._empleados)}"
        )