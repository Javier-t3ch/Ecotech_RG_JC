# persistencia/empleado_dao.py
from persistencia.conexion import abrir_conexion, obtener_motor, marcador_sql
from dominio.proyecto import Proyecto
class EmpleadoDAO:
    @staticmethod
    def _fila_a_empleado(fila):
        return Proyecto(
            id=fila[0],
            nombre=fila[1],
            fecha_inicio=fila[2],
            descripcion=fila[3],

        )

    def insertar(proyecto):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = "?" if obtener_motor() == "sqlite" else "%s"

        sql = f"""
            INSERT INTO proyecto (nombre, fecha_inicio, descripcion)
            VALUES ({marcador}, {marcador}, {marcador})
        """
        cursor.execute(sql, (proyecto._nombre, proyecto._fecha_inicio, proyecto._descripcion))
        proyecto._id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return proyecto 
    

    def actualizar(proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()

            marca = marcador_sql()
            sql = (
                "UPDATE proyecto "
                f"SET nombre = {marca}, fecha_inicio = {marca}, descripcion = {marca} "
                f"WHERE id = {marca}"
            )

            cursor.execute(
                sql,
            (
                proyecto.nombre,
                proyecto.fecha_inicio,
                proyecto.descripcion,
                proyecto.id
            
            )
        )
    
            conexion.commit()
            return cursor.rowcount > 0
        
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        
        finally:
            if conexion:
                conexion.close()

    def eliminar(id_empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        marca = marcador_sql()
        sql = (
            "DELETE FROM empleado "
        f"WHERE id = {marca}"
        )

        cursor.execute(sql,(id_empleado,))
        conexion.commit()

        eliminado = cursor.rowcount > 0
        conexion.close()
        return eliminado

    def buscar_por_id(id_empleado):
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()

            marca = marcador_sql()
            sql = f"""
                    SELECT id, nombre, correo 
                    FROM empleado WHERE id = {marca}
                    """
            cursor.execute(sql, (id_empleado,))
            fila = cursor.fetchone()
            conexion.close()
            return EmpleadoDAO._fila_a_empleado(fila)
        except Exception as e:
            print(f"error: {e}")

    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        cursor.execute(
        "SELECT id, nombre, correo FROM empleado"
    )

        filas = cursor.fetchall()
        conexion.close()

        empleados = []

        for fila in filas:
            empleados.append(
                EmpleadoDAO._fila_a_empleado(fila)
            )
        return empleados