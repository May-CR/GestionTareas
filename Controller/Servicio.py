import mysql.connector
from Model.Consulta import *
from Model.Task import *
from Model.Usuario import *

class Servicio:

    def conectar():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="P@ssw0rd",
        database="taskmanagement"
        )
        myCursor = mydb.cursor()
        return mydb, myCursor
    
    def consultar(idUser):
        mydb, myCursor = Servicio.conectar()
        myCursor.execute(Consulta.SHOW_TASK, (idUser,))
        return myCursor.fetchall()
    
    def crearTarea(titulo, prioridad, fechaCulminacion, categoria, estado, idUser):
        mydb, myCursor = Servicio.conectar()
        task = Task(titulo, prioridad, fechaCulminacion, categoria, estado, idUser)
        myCursor.execute(Consulta.INSERT_TASK,(titulo, prioridad, fechaCulminacion, categoria, estado, idUser))
        mydb.commit()

    def actualizarTarea(titulo, prioridad, fechaCulminacion, categoria, estado, idUser):
        mydb, myCursor = Servicio.conectar()
        task = Task(titulo, prioridad, fechaCulminacion, categoria, estado, idUser)
        myCursor.execute(Consulta.UPDATE_TASK+idUser, (task.info()))
        mydb.commit()

    def eliminarTarea(idTarea):
        mydb, myCursor = Servicio.conectar()
        myCursor.execute(Consulta.DELETE_TASK+idTarea)
        mydb.commit()

    def crearUsuario(name, password):
        mydb, myCursor = Servicio.conectar()
        user = Usuario(name, password)
        myCursor.execute(Consulta.INSERT_USER, (user.info()))
        mydb.commit()

    def existeUsuario(name, password):
        mydb, myCursor = Servicio.conectar()
        user = Usuario(name, password)
        myCursor.execute(Consulta.EXISTE_USER, (user.info()))
        return myCursor.fetchone()
    