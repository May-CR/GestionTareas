from tkinter import messagebox
from Controller.Mensaje import *
import traceback
from Controller.Servicio import *

class Gestor:

    #Gestionar servicios de conexion 
    def conexionBBDD():
        try:
            Servicio.conectar()
            messagebox.showinfo("Conexión", Mensaje.EXITO_BD)
        except:
            messagebox.showerror("Conexión", Mensaje.ERROR_BD)

    #Gestionar servicios de CRUD

    def mostrar(tree, idUser):
        registros = tree.get_children()
        [tree.delete(elemento) for elemento in registros]
        try:
            usuario = Servicio.consultar(idUser)
            for row in usuario:
                tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
        except:
            traceback.print_exc()
            messagebox.showerror("Mostrar", Mensaje.ERROR_MOSTRAR) 

    def crearTarea(titulo, prioridad, fechaCulminacion, categoria, estado, idUser):
        try:
            if (titulo != "" or prioridad != "" or fechaCulminacion != "" or categoria != "" or estado != "" or idUser != ""):
                Servicio.crearTarea(titulo, prioridad, fechaCulminacion, categoria, estado, idUser)
            else:
                messagebox.showinfo("Crear", Mensaje.CAMPOS_FALTANTES)
        except:
            traceback.print_exc()
            messagebox.showerror("Error", Mensaje.ERROR_CREAR)

    def crearUsuario(name, password, confirm):
        try:
            if ((name != "" or password != "" or confirm != "") and password == confirm):
                Servicio.crearUsuario(name, password)
            else:
                if password != confirm:
                    messagebox.showinfo("Crear", Mensaje.ERROR_CONTRASEÑAS_DISTINTAS)
                else:
                    messagebox.showinfo("Crear", Mensaje.CAMPOS_FALTANTES)
        except:
            traceback.print_exc() 
            messagebox.showerror("Crear", Mensaje.ERROR_CREAR)

    def verificarUsuario(name, password):
        try:
            if ((name != "" or password != "")):
                messagebox.showinfo("Registro", Mensaje.ACCESO_VALIDO)
                return Servicio.existeUsuario(name, password)
            else:
                messagebox.showinfo("Registro", Mensaje.ERROR_LOGIN)
        except:
            messagebox.showerror("Registro", Mensaje.ERROR_BUSCAR)

    def actualizar(titulo, prioridad, fechaCulminacion, categoria, estado, idUser, idTarea):
        try:
            if (titulo != "" or prioridad != "" or fechaCulminacion != "" or categoria != "" or estado != "" or idUser != ""):
                Servicio.actualizarTarea(titulo, prioridad, fechaCulminacion, categoria, estado, idUser, idTarea)
            else:
                messagebox.showinfo("Crear", Mensaje.CAMPOS_FALTANTES)
        except:
            messagebox.showerror("Crear", Mensaje.ERROR_ACTUALIZAR)

    def eliminar(idTarea):
        if messagebox.askyesno("Eliminar", Mensaje.CONFIRMAR):
            try:
                Servicio.eliminarTarea(idTarea)
            except:
                messagebox.showerror("Eliminar", Mensaje.ERROR_ELIMINAR)