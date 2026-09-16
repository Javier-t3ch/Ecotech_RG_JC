class Proyecto:
    def __init__(self, id_proyecto: str, nombre: str, fecha_inicio: str, descripcion: str):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.descripcion = descripcion

    def mostrar_datos(self) -> str:
        return f"{self.id_proyecto} - {self.nombre} - {self.fecha_inicio} - {self.descripcion}"