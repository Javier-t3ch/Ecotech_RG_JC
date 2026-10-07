# persistencia/empleado_dao.py
from persistencia.conexion import abrir_conexion, obtener_motor, marcador_sql
from dominio.departamento import Departamento
class DepartamentoDAO:
    @staticmethod
    def _fila_de_departamento(fila):
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
            INSERT INTO empleado (nombre, empleados, proyectos)
            VALUES ({marcador}, {marcador}, {marcador})
        """
        cursor.execute(sql, (departamento._nombre, departamento._empleados, departamento._proyectos))
        departamento._id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return departamento 
    

    def actualizar(departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()

            marca = marcador_sql()
            sql = (
                "UPDATE empleado "
                f"SET nombre = {marca}, empleados = {marca}, proyectos = {marca}"
                f"WHERE id = {marca}"
            )

            cursor.execute(
                sql,
            (
                departamento.nombre,
                departamento.empleados,
                departamento.proyecto,
                departamento.id
            
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

    def eliminar(id_departamento):
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        marca = marcador_sql()
        sql = (
            "DELETE FROM Departamento "
        f"WHERE id = {marca}"
        )

        cursor.execute(sql,(id_departamento,))
        conexion.commit()

        eliminado = cursor.rowcount > 0
        conexion.close()
        return eliminado

    def buscar_por_id(id_departamento):
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()

            marca = marcador_sql()
            sql = f"""
                    SELECT id, nombre, empleados, proyectos 
                    FROM departmanto WHERE id = {marca}
                    """
            cursor.execute(sql, (id_departamento,))
            fila = cursor.fetchone()
            conexion.close()
            return DepartamentoDAO._fila_de_departamento(fila)
        except Exception as e:
            print(f"error: {e}")

    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()

        cursor.execute(
        "SELECT id, nombre, empleados, proyectos FROM departamento"
    )

        filas = cursor.fetchall()
        conexion.close()

        Departamento = []

        for fila in filas:
            Departamento.append(
                DepartamentoDAO._fila_de_departamento(fila)
            )
        return Departamento