import pymysql

# Función para conectar a la base de datos MySQL
def conectar_bd():
    try:
        conexion = pymysql.connect(
            host="localhost",  # Cambiar según tu configuración
            user="root",       # Usuario de la base de datos
            password="curso",       # Contraseña de la base de datos
            database="encuestas"  # Nombre de la base de datos
        )
        return conexion
    except pymysql.MySQLError as err:
        print(f"Error al conectar con la base de datos: {err}")
        return None

# Función para leer registros de la base de datos con opción de ordenación
def leer_registros(ordenar_por=None):
    conexion = conectar_bd()
    if not conexion:
        return []

    try:
        cursor = conexion.cursor()

        # Si se especifica un campo de ordenación, agregarlo a la consulta SQL
        if ordenar_por:
            consulta = f"SELECT * FROM ENCUESTA ORDER BY {ordenar_por}"
        else:
            consulta = "SELECT * FROM ENCUESTA"  # Si no se especifica, no ordena

        cursor.execute(consulta)
        registros = cursor.fetchall()
        conexion.close()
        return registros
    except Exception as e:
        print(f"Error al leer registros: {e}")
        return []

# Función para leer registros con filtro condicional
def leer_registros_con_filtro(filtro=None):
    conexion = conectar_bd()
    if not conexion:
        return []

    try:
        cursor = conexion.cursor()

        # Si se especifica un filtro, agregarlo a la consulta SQL
        if filtro:
            consulta = f"SELECT * FROM ENCUESTA WHERE {filtro}"
        else:
            consulta = "SELECT * FROM ENCUESTA"  # Si no se especifica, no filtra

        cursor.execute(consulta)
        registros = cursor.fetchall()
        conexion.close()
        return registros
    except Exception as e:
        print(f"Error al leer registros con filtro: {e}")
        return []

# Función para insertar un nuevo registro
def insertar_registro(edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana,
                      perdidas_control, diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza):
    conexion = conectar_bd()
    if not conexion:
        return False

    try:
        cursor = conexion.cursor()
        consulta = """
        INSERT INTO ENCUESTA (edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana,
                              perdidas_control, diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(consulta, (edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas_semana, vinos_semana,
                                  perdidas_control, diversion_dependencia_alcohol, problemas_digestivos, tension_alta, dolor_cabeza))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al insertar registro: {e}")
        return False
# Función para actualizar un registro
def actualizar_registro(id, edad, sexo, consumo_semanal, problemas_salud, perdidas_control):
    conexion = conectar_bd()
    if not conexion:
        return False

    try:
        cursor = conexion.cursor()
        consulta = "UPDATE ENCUESTA SET edad=%s, sexo=%s, consumo_semanal=%s, problemas_salud=%s, perdidas_control=%s WHERE id=%s"
        cursor.execute(consulta, (edad, sexo, consumo_semanal, problemas_salud, perdidas_control, id))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al actualizar registro: {e}")
        return False

# Función para eliminar un registro
def eliminar_registro(id):
    conexion = conectar_bd()
    if not conexion:
        return False

    try:
        cursor = conexion.cursor()
        consulta = "DELETE FROM ENCUESTA WHERE id=%s"
        cursor.execute(consulta, (id,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al eliminar registro: {e}")
        return False
