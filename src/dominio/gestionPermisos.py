class GestionPermisos:
    def otorgar_permiso(self, usuario, permiso):
        return usuario.agregar_permiso(permiso)