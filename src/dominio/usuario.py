class Usuario:
    def __init__(self, id_usuario, nombre, mail, contrasenia_hash):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._mail = mail
        self._contrasenia_hash = contrasenia_hash
        self._permisos = []

    def autenticar(self, contrasenia):
        if contrasenia == self._contrasenia_hash:
            return True
        return False

    def cambiar_contrasenia(self, contrasenia_nueva):
        if contrasenia_nueva == self._contrasenia_hash:
            return False
        self._contrasenia_hash = contrasenia_nueva
        return True

    def agregar_permiso(self, permiso):
        if permiso not in self._permisos:
            self._permisos.append(permiso)
            return True
        return False