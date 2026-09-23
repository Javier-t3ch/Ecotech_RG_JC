from dominio.departamento import Departamento


class GestionDepartamento:

    def __init__(self):
        self._departamentos = []

    def crear_departamento(self, nombre):
        departamento = Departamento(nombre)
        self._departamentos.append(departamento)
        return departamento

    def eliminar_departamento(self, nombre):
        departamento = self.buscar_departamento(nombre)
        if departamento == False:
            return False
        self._departamentos.remove(departamento)
        return True

    def editar_departamento(self, nombre, nuevo_nombre):
        departamento = self.buscar_departamento(nombre)
        if departamento == False:
            return False
        departamento._nombre = nuevo_nombre
        return True

    def buscar_departamento(self, nombre):
        for departamento in self._departamentos:
            if departamento._nombre == nombre:
                return departamento
        return False