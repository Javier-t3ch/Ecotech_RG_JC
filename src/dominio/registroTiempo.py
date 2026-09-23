class RegistroTiempo:
    def __init__(self, id_registro, horas_trabajadas, fecha_trabajada, descripcion_tarea, empleado, proyecto):
        self._id_registro = id_registro
        self._horas_trabajadas = horas_trabajadas
        self._fecha_trabajada = fecha_trabajada
        self._descripcion_tarea = descripcion_tarea
        self._empleado = empleado
        self._proyecto = proyecto

    def calculo_horas(self, registros):
        total_horas = 0
        for registro in registros:
            if registro._empleado._id_empleado == self._empleado._id_empleado:
                total_horas += registro._horas_trabajadas
        return total_horas

    def calculo_horas_proyecto(self, registros, proyecto):
        total_horas = 0
        for registro in registros:
            if (registro._empleado._id_empleado == self._empleado._id_empleado
                    and registro._proyecto._id_proyecto == proyecto._id_proyecto):
                total_horas += registro._horas_trabajadas
        return total_horas