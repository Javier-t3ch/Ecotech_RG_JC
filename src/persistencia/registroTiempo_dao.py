from persistencia.conexion import abrir_conexion, obtener_motor, marcador_sql
from dominio.registroTiempo import RegistroTiempo

class RegistroTiempoDAO:
    @staticmethod
    def _fila_de_registroTiempo(fila):
        return RegistroTiempo(
            id_registro=fila[0],
            horas_trabajadas=fila[1],
            fecha_trabajada=fila[2],
            descripcion_tarea=fila[3],
            empleado=fila[4],
            proyecto=fila[5]    
        )

    def insertar(registroTiempo):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = "?" if obtener_motor() == "sqlite" else "%s"

        sql = f"""
            INSERT INTO registroTiempo (horas_trabajadas, fecha_trabajada, descripcion_tarea, empleado, proyecto)
            VALUES ({marcador}, {marcador}, {marcador}, {marcador}, {marcador})
        """
        cursor.execute(sql, (registroTiempo._horas_trabajada, registroTiempo._fecha_trabajada, registroTiempo._descripcion_tarea, registroTiempo._empleadom, registroTiempo._proyecto))
        registroTiempo._id_registro = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return registroTiempo 
    

    def actualizar(registroTiempo):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()

            marca = marcador_sql()
            sql = (
                "UPDATE empleado "
                f"SET horas_trabajadas = {marca}, fecha_trabajada = {marca}, descripcion_tarea = {marca}, empleado = {marca}, proyecto = {marca}"
                f"WHERE id = {marca}"
            )

            cursor.execute(
                sql,
            (
                registroTiempo.horas_trabajadas,
                registroTiempo.fecha_trabajadas,
                registroTiempo.descripcion_tarea,
                registroTiempo.empleado,
                registroTiempo.proyecto
            
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

    def eliminar(id_registro):
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        marca = marcador_sql()
        sql = (
            "DELETE FROM registroTiempo "
        f"WHERE id = {marca}"
        )

        cursor.execute(sql,(id_registro,))
        conexion.commit()

        eliminado = cursor.rowcount > 0
        conexion.close()
        return eliminado

    def buscar_por_id(id_registro):
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()

            marca = marcador_sql()
            sql = f"""
                    SELECT id, horas_trabajadas, fecha_trabajada, descripcion_tarea, empleado, proyecto 
                    FROM departmanto WHERE id = {marca}
                    """
            cursor.execute(sql, (id_registro,))
            fila = cursor.fetchone()
            conexion.close()
            return RegistroTiempoDAO._fila_de_registroTiempo(fila)
        except Exception as e:
            print(f"error: {e}")

    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        cursor.execute(
        "SELECT id, horas_trabajadas, fecha_trabajada, descripcion_tarea, empleado, proyecto FROM departamento"
    )

        filas = cursor.fetchall()
        conexion.close()

        RegistroTiempo = []

        for fila in filas:
            RegistroTiempo.append(
                RegistroTiempoDAO._fila_de_registroTiempo(fila)
            )
        return RegistroTiempo