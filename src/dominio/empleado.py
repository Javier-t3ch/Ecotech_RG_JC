class Empleado:

    def __init__(self, nombre, direccion, numero, correo, fecha_contrato, salario, cargo, id=None ):
        self._id= id
        self._nombre = nombre
#        self._direccion = direccion
#        self._numero = numero
        self._correo = correo
#        self._fecha_contrato = fecha_contrato
#        self._salario = salario
#        self._cargo = cargo
#        self._registros_tiempo = []

    def mostrar_datos(self):
        return f"{self._id_empleado} - {self._nombre} - {self._direccion} - {self._numero} - {self._correo} - {self._fecha_contrato} - {self._salario} - {self._cargo}"

    def ver_salario(self):
        return self._salario

    def registrar_horas(self, registro):
        self._registros_tiempo.append(registro)
        return True


"""
    def calcular_pago(self) -> float:
        raise NotImplementedError
class EmpleadoMensual(Empleado):
    def __init__(self, sueldo: float):
        self.sueldo = sueldo
    def calcular_pago(self) -> float:
        return self.sueldo
class EmpleadoPorHora(Empleado):
    def __init__(self, horas: float, valor_hora: float):
        self.horas = horas
        self.valor_hora = valor_hora
    def calcular_pago(self) -> float:
        return self.horas * self.valor_hora"""