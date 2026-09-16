# src/dominio/empleado.py
class Empleado:
    contador_id = 0
    def __init__(self, id_empleado: str, nombre: str, direccion: str, numero: int, correo: str, fecha_contrato: int, salario: int, cargo: int):
        Empleado.contador_id =+  1
        self.id_empleado = Empleado.contador_id
        self.nombre = nombre
        self.direccion = direccion
        self.numero = numero
        self.correo = correo
        self.fecha_contrato = fecha_contrato
        self.salario = salario
        self.cargo = cargo
    def mostrar_datos(self) -> str:
        return f"{self.id_empleado} - {self.nombre} - {self.direccion} - {self.numero} - {self.correo} - {self.fecha_contrato} - {self.salario} - {self.cargo}"
    
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
        return self.horas * self.valor_hora