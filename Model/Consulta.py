class Consulta:
    INSERT_USER = "INSERT INTO user (name, password) VALUES (%s, %s)"

    INSERT_TASK = "INSERT INTO tareas (titulo, prioridad, fechaCulminacion, categoria, estado, idUser) VALUES (%s, %s, %s, %s, %s, %s)"

    SHOW_TASK = "SELECT * FROM tareas where idUser =%s"

    UPDATE_TASK = "UPDATE tareas SET titulo = %s, prioridad = %s, fechaCulminacion = %s, categoria = %s, estado = %s WHERE idTarea ="

    DELETE_TASK = "DELETE FROM tareas WHERE idTarea ="

    BUSCAR_TASK = "SELECT * FROM tareas WHERE estado LIKE '%' || %s || '%' "

    EXISTE_USER = "SELECT idUser, name FROM user WHERE name = %s AND password = %s"



