import tkinter as tk
from tkinter import messagebox

# Clase para manejar la interfaz y las funciones de la tarea
class AplicacionTareas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mi Lista de Tareas")
        self.ventana.geometry("400x500")

        # Elementos de la parte superior (entrada de texto)
        self.lbl_titulo = tk.Label(ventana, text="Tarea nueva:")
        self.lbl_titulo.pack(pady=10)

        self.caja_entrada = tk.Entry(ventana, width=35)
        self.caja_entrada.pack(pady=5)
        
        # Evento para añadir con la tecla Enter
        self.caja_entrada.bind("<Return>", lambda e: self.agregar())

        # Botones principales
        self.marco_botones = tk.Frame(ventana)
        self.marco_botones.pack(pady=15)

        self.btn_add = tk.Button(self.marco_botones, text="Añadir", command=self.agregar, width=10)
        self.btn_add.grid(row=0, column=0, padx=5)

        self.btn_done = tk.Button(self.marco_botones, text="Completada", command=self.marcar, width=10)
        self.btn_done.grid(row=0, column=1, padx=5)

        self.btn_del = tk.Button(self.marco_botones, text="Eliminar", command=self.borrar, width=10, fg="red")
        self.btn_del.grid(row=0, column=2, padx=5)

        # Listbox para ver las tareas
        self.lista = tk.Listbox(ventana, width=45, height=18)
        self.lista.pack(pady=10, padx=20)
        
        # Evento de doble clic para marcar rápido
        self.lista.bind("<Double-Button-1>", lambda e: self.marcar())

    # Metodo para meter tareas a la lista
    def agregar(self):
        texto = self.caja_entrada.get()
        if texto != "":
            self.lista.insert(tk.END, texto)
            self.caja_entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Escribe algo primero")

    # Metodo para cambiar el estado de la tarea
    def marcar(self):
        try:
            index = self.lista.curselection()[0]
            item = self.lista.get(index)
            if " [OK]" not in item:
                nueva_linea = item + " [OK]"
                self.lista.delete(index)
                self.lista.insert(index, nueva_linea)
                self.lista.itemconfig(index, fg="green")
        except:
            messagebox.showwarning("Error", "Selecciona una tarea de la lista")

    # Metodo para quitar tareas
    def borrar(self):
        try:
            index = self.lista.curselection()[0]
            self.lista.delete(index)
        except:
            messagebox.showwarning("Error", "No has seleccionado nada para borrar")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionTareas(root)
    root.mainloop()
