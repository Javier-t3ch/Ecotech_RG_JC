# src/dominio/empleado.py
class Empleado:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo

    def mostrar_datos(self) -> str:
        return f"{self.nombre} - {self.correo}"
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