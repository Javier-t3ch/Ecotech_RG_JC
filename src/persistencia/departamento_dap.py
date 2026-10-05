# persistencia/empleado_dao.py
from persistencia.conexion import abrir_conexion, obtener_motor, marcador_sql
from dominio.departamento import Departamento
class DepartamentoDAO:
    @staticmethod
    def _fila_a_empleado(fila):
        return Departamento(
            id_departamento=fila[0],
            nombre=fila[1],
            empleados=fila[2],
            proyectos=fila[3],    
        )

    def insertar(departamento):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = "?" if obtener_motor() == "sqlite" else "%s"

        sql = f"""
            INSERT INTO empleado (nombre, correo)
            VALUES ({marcador}, {marcador})
        """
        cursor.execute(sql, (departamento._nombre, departamento._correo))
        departamento._id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return departamento 
    

    def actualizar(empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()

            marca = marcador_sql()
            sql = (
                "UPDATE empleado "
                f"SET nombre = {marca}, correo = {marca} "
                f"WHERE id = {marca}"
            )

            cursor.execute(
                sql,
            (
                empleado.nombre,
                empleado.correo,
                empleado.id
            
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
            return DepartamentoDAO._fila_a_empleado(fila)
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