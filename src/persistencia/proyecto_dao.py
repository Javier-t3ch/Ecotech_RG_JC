from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.proyecto import Proyecto


class ProyectoDao:

    @staticmethod
    def _fila_a_proyecto(fila):
        return Proyecto(
            id_proyecto=fila[0],
            nombre=fila[1],
            fecha_inicio=fila[2],
            descripcion=fila[3]
    )


    def insertar(proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "INSERT INTO proyecto (nombre, fecha_inicio, descripcion) "
                f"VALUES ({marca}, {marca}, {marca})"
            )
            cursor.execute(sql, (
                proyecto._nombre,
                proyecto._fecha_inicio,
                proyecto._descripcion
            ))
            conexion.commit()
            proyecto._id_proyecto = cursor.lastrowid
            return proyecto
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    def actualizar(proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "UPDATE proyecto SET "
                f"nombre = {marca}, fecha_inicio = {marca}, descripcion = {marca} "
                f"WHERE id = {marca}"
            )
            cursor.execute(sql, (
                proyecto._nombre,
                proyecto._fecha_inicio,
                proyecto._descripcion,
                proyecto._id_proyecto
            ))
            actualizado = cursor.rowcount > 0
            conexion.commit()
            return actualizado
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    def eliminar(id_proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"DELETE FROM proyecto WHERE id = {marca}"
            cursor.execute(sql, (id_proyecto,))
            eliminado = cursor.rowcount > 0
            conexion.commit()
            return eliminado
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    def buscar_por_id(id_proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "SELECT id, nombre, fecha_inicio, descripcion "
                f"FROM proyecto WHERE id = {marca}"
            )
            cursor.execute(sql, (id_proyecto,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return ProyectoDao._fila_a_proyecto(fila)
        finally:
            if conexion:
                conexion.close()

    def listar():
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id, nombre, fecha_inicio, descripcion FROM proyecto"
            )
            filas = cursor.fetchall()
            proyectos = []
            for fila in filas:
                proyectos.append(ProyectoDao._fila_a_proyecto(fila))
            return proyectos
        finally:
            if conexion:
                conexion.close()
