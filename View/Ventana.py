import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector
from datetime import datetime
from PIL import Image, ImageTk
from View.Gestor import *
import mysql.connector

class Ventana:
    def conexionBD():
        Gestor.conexionBBDD()

    def login(self, username, password):
        user = Gestor.verificarUsuario(username, password)
        self.current_user_id = user[0]
        self.current_user_name = user[1]
        self.create_task_screen()

    def create_task_screen(self):
        # Limpiar ventana actual
        self.root.geometry("1400x600")
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Crear frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame izquierdo para agregar tareas
        left_frame = ttk.Frame(main_frame, padding=20)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Campos para nueva tarea
        ttk.Label(left_frame, text="Título").pack()
        title_entry = ttk.Entry(left_frame)
        title_entry.pack(fill=tk.X, pady=5)
        
        ttk.Label(left_frame, text="Descripción").pack()
        desc_text = tk.Text(left_frame, height=5)
        desc_text.pack(fill=tk.X, pady=5)
        
        # Frame para prioridad
        priority_frame = ttk.Frame(left_frame)
        priority_frame.pack(fill=tk.X, pady=5)
        ttk.Label(priority_frame, text="Prioridad").pack()
        
        priority_var = tk.StringVar()
        ttk.Radiobutton(priority_frame, text="Baja", variable=priority_var, 
                       value="Baja").pack(side=tk.LEFT)
        ttk.Radiobutton(priority_frame, text="Media", variable=priority_var,
                       value="Media").pack(side=tk.LEFT)
        ttk.Radiobutton(priority_frame, text="Alta", variable=priority_var,
                       value="Alta").pack(side=tk.LEFT)
        
        # Fecha de culminación
        ttk.Label(left_frame, text="Fecha de culminación").pack()
        date_entry = DateEntry(left_frame, width=12, background='darkblue',
                             foreground='white', borderwidth=2)
        date_entry.pack(pady=5)
        
        # Frame para método de entrega
        delivery_frame = ttk.Frame(left_frame)
        delivery_frame.pack(fill=tk.X, pady=5)
        ttk.Label(delivery_frame, text="Entregar por").pack()
        
        delivery_var = tk.StringVar()
        ttk.Radiobutton(delivery_frame, text="Correo", variable=delivery_var,
                       value="Correo").pack(side=tk.LEFT)
        ttk.Radiobutton(delivery_frame, text="Portal Web", variable=delivery_var,
                       value="Portal Web").pack(side=tk.LEFT)
        ttk.Radiobutton(delivery_frame, text="Físico", variable=delivery_var,
                       value="Físico").pack(side=tk.LEFT)
        
        # Estado
        ttk.Label(left_frame, text="Estado").pack()
        status_combo = ttk.Combobox(left_frame, 
                                  values=["Pendiente", "En Progreso", "Completada"])
        status_combo.pack(fill=tk.X, pady=5)
        
        # Botones
        button_frame = ttk.Frame(left_frame)
        button_frame.pack(fill=tk.X, pady=20)
        
        ttk.Button(button_frame, text="Añadir Tarea",
                  command=lambda: self.add_task(
                      title_entry.get(),
                      #desc_text.get("1.0", tk.END),
                      priority_var.get(),
                      date_entry.get(),
                      delivery_var.get(),
                      status_combo.get()
                  )).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Cancelar",
                  command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        
        # Frame derecho para lista de tareas
        right_frame = ttk.Frame(main_frame, padding=20)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Tabla de tareas
        columns = ("Título", "Prioridad", "Fecha de Culminación",
                  "Categoria", "Estado")
        self.task_tree = ttk.Treeview(right_frame, columns=columns, show="headings")
        
        # Configurar columnas
        for col in columns:
            self.task_tree.heading(col, text=col)
            self.task_tree.column(col, width=100)
        
        self.task_tree.pack(fill=tk.BOTH, expand=True)

        # Cargar tareas
        try:
            self.load_tasks()
        except Exception as e:
            traceback.print_exc()
        
        # Botón de logout
        ttk.Button(right_frame, text="LogOut",
                  command=self.create_login_screen).pack(pady=10)

    def register_user(self, username, password, confirm):
        Gestor.crearUsuario(username, password, confirm)
        try:
            self.create_login_screen()
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "El usuario ya existe")

    def clear_fields(self):
        self.title_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)
        self.priority_var.set("")
        self.date_entry.set_date(datetime.now())
        self.delivery_var.set("")
        self.status_combo.set("")

    def add_task(self, title, priority, due_date, category, status):
        Gestor.crearTarea(title, priority, due_date, category, status, self.current_user_id)
        try:
            self.load_tasks()
        except Exception as e:
            traceback.print_exc()
            messagebox.showerror("ERROR", f"Error al agregar tarea: {str(e)}")

    def load_tasks(self):
        # Limpiar tabla actual
        for item in self.task_tree.get_children():
            self.task_tree.delete(item)
        try:
            Gestor.mostrar(self.task_tree, self.current_user_id)
        except Exception as e:
            traceback.print_exc()

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestor de Tareas")
        self.root.geometry("800x600")
        
        # Configurar el estilo
        self.style = ttk.Style()
        self.style.configure("Custom.TFrame", background="#2196F3")
        
        # Variables para mantener la sesión
        self.current_user_id = None
        self.current_user_name = None
        
        # Iniciar con la pantalla de login
        self.create_login_screen()

    def create_login_screen(self):
        self.root.geometry("800x600")
        # Limpiar ventana actual
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame izquierdo (información de contacto)
        left_frame = ttk.Frame(main_frame, style="Custom.TFrame")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Añadir logo y texto informativo
        logo_label = ttk.Label(left_frame, text="✓", font=("Arial", 48))
        logo_label.pack(pady=(100,10))
        
        title_label = ttk.Label(left_frame, text="Gestor de Tareas",
                                  font=("Arial", 24, "bold"))
        title_label.pack(pady=10)

        phone_label = ttk.Label(left_frame, text="555-222-333",
                                  font=("Arial", 12))
        phone_label.pack(pady=5)
        
        email_label = ttk.Label(left_frame, text="gestion@soporte.com",
                                  font=("Arial", 12))
        email_label.pack(pady=5)
        
        # Frame derecho (formulario de login)
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Frame del formulario
        form_frame = ttk.Frame(right_frame)
        form_frame.pack(pady=100)
        
        # Icono de candado
        lock_label = ttk.Label(form_frame, text="🔒", font=("Arial", 24))
        lock_label.pack(pady=20)
        
        # Campos de entrada
        ttk.Label(form_frame, text="Username").pack()
        username_entry = ttk.Entry(form_frame, width=30)
        username_entry.pack(pady=5)
        
        ttk.Label(form_frame, text="Password").pack()
        password_entry = ttk.Entry(form_frame, show="*", width=30)
        password_entry.pack(pady=5)
        
        # Botones
        login_button = ttk.Button(form_frame, text="Login",
                                command=lambda: self.login(
                                    username_entry.get(),
                                    password_entry.get()))
        login_button.pack(pady=20)
        
        # Link para registro
        register_frame = ttk.Frame(form_frame)
        register_frame.pack(pady=10)
        
        ttk.Label(register_frame, text="No estas registrado?").pack(side=tk.LEFT)
        register_link = ttk.Button(register_frame, text="Register",
                                 command=self.create_register_screen)
        register_link.pack(side=tk.LEFT, padx=5)

    def create_register_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Frame principal con fondo verde azulado
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configurar el estilo de fondo
        main_frame.configure(style="Custom.TFrame")
        
        # Frame para el formulario
        form_frame = ttk.Frame(main_frame, padding=20)
        form_frame.pack(pady=100)
        
        # Icono de candado
        lock_label = ttk.Label(form_frame, text="🔒", font=("Arial", 40))
        lock_label.pack(pady=10)
        
        # Título
        title_label = ttk.Label(form_frame, text="Registrar Usuario", font=("Arial", 16))
        title_label.pack(pady=10)
        
        # Campos de entrada
        username_label = ttk.Label(form_frame, text="Username")
        username_label.pack()
        username_entry = ttk.Entry(form_frame, width=30)
        username_entry.pack(pady=5)
        
        password_label = ttk.Label(form_frame, text="Password")
        password_label.pack()
        password_entry = ttk.Entry(form_frame, show="*", width=30)
        password_entry.pack(pady=5)
        
        confirm_label = ttk.Label(form_frame, text="Confirm Password")
        confirm_label.pack()
        confirm_entry = ttk.Entry(form_frame, show="*", width=30)
        confirm_entry.pack(pady=5)
        
        # Botones
        button_frame = ttk.Frame(form_frame)
        button_frame.pack(pady=20)
        
        register_button = ttk.Button(button_frame, text="Registrar",
                                   command=lambda: self.register_user(
                                       username_entry.get(),
                                       password_entry.get(),
                                       confirm_entry.get()))
        register_button.pack(side=tk.LEFT, padx=5)
        
        cancel_button = ttk.Button(button_frame, text="Cancelar",
                                 command=self.root.quit)
        cancel_button.pack(side=tk.LEFT, padx=5)
  
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Ventana()
    app.run()