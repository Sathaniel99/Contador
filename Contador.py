import os
import sys
import tkinter as tk
from tkinter import messagebox

# Función para obtener rutas relativas incluso dentro del .exe
def resource_path(relative_path):
    """ Devuelve la ruta absoluta al recurso, funciona para desarrollo y PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class EditorTXT:
    def __init__(self, root):
        path = os.path.expanduser("~").replace("\\", "/") + '/Documents/'
        archivo = path + 'Contador.ini'
        self.root = root
        self.archivo = archivo
        self.root.title("Contador")

        # Cargar ícono desde el recurso incrustado o carpeta local
        icon_path = resource_path("icon_exe.ico")
        if os.path.exists(icon_path):
            try:
                self.root.iconbitmap(icon_path)
            except Exception as e:
                print(f"No se pudo cargar el ícono: {e}")
        else:
            print("Ícono no encontrado:", icon_path)

        # Configurar tamaño y posicionamiento de la ventana
        ancho_ventana = 405
        alto_ventana = 160
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        x_pos = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y_pos = (alto_pantalla // 2) - (alto_ventana // 2)

        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
        self.root.resizable(False, False)

        # Verificar si existe el directorio
        if not os.path.exists(path):
            messagebox.showerror("Error", "No se encuentra el directorio.")
            self.root.destroy()
            return

        # Cargar valores iniciales
        self.cargar_valores()

        # Crear interfaz
        self.crear_interfaz()

        # Actualizar labels iniciales
        self.actualizar_labels()

        # Configurar guardado automático al cerrar
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def cargar_valores(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as f:
                    lineas = f.readlines()
                    self.valor_p = 0
                    self.valor_s = 0

                    for linea in lineas:
                        if linea.startswith("p"):
                            try:
                                self.valor_p = int(linea.split()[1])
                            except (IndexError, ValueError):
                                self.valor_p = 0
                        elif linea.startswith("s"):
                            try:
                                self.valor_s = int(linea.split()[1])
                            except (IndexError, ValueError):
                                self.valor_s = 0
            else:
                self.valor_p = 0
                self.valor_s = 0
                self.guardar_valores()

        except PermissionError:
            messagebox.showerror("Error", "No tienes permisos para leer el archivo.")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
            self.valor_p = 0
            self.valor_s = 0

    def guardar_valores(self):
        try:
            with open(self.archivo, 'w') as f:
                f.write(f"p {self.valor_p}\n")
                f.write(f"s {self.valor_s}\n")
        except PermissionError:
            messagebox.showerror("Error", "No tienes permisos para escribir el archivo.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

    def crear_interfaz(self):
        # Marco para la sección P
        marco_p = tk.LabelFrame(self.root, text="Pxxx", padx=10, pady=10, font=('Arial', 14))
        marco_p.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Label para el valor P
        self.label_valor_p = tk.Label(marco_p, text="0", font=('Arial', 20, 'bold'))
        self.label_valor_p.pack(pady=5)

        # Botones para P
        frame_botones_p = tk.Frame(marco_p)
        frame_botones_p.pack(pady=5)

        tk.Button(frame_botones_p, text="+", width=5, font=('Arial', 14, 'bold'), cursor='hand2',
                  command=lambda: self.cambiar_valor('p', 1)).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones_p, text="-", width=5, font=('Arial', 14, 'bold'), cursor='hand2',
                  command=lambda: self.cambiar_valor('p', -1)).pack(side=tk.LEFT, padx=5)

        # Marco para la sección S
        marco_s = tk.LabelFrame(self.root, text="Sxxx", padx=10, pady=10, font=('Arial', 14))
        marco_s.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Label para el valor S
        self.label_valor_s = tk.Label(marco_s, text="0", font=('Arial', 20, 'bold'))
        self.label_valor_s.pack(pady=5)

        # Botones para S
        frame_botones_s = tk.Frame(marco_s)
        frame_botones_s.pack(pady=5)

        tk.Button(frame_botones_s, text="+", width=5, font=('Arial', 14, 'bold'), cursor='hand2',
                  command=lambda: self.cambiar_valor('s', 1)).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones_s, text="-", width=5, font=('Arial', 14, 'bold'), cursor='hand2',
                  command=lambda: self.cambiar_valor('s', -1)).pack(side=tk.LEFT, padx=5)

    def cambiar_valor(self, variable, cambio):
        if variable == 'p':
            self.valor_p += cambio
            self.label_valor_p.config(text=str(self.valor_p))
        elif variable == 's':
            self.valor_s += cambio
            self.label_valor_s.config(text=str(self.valor_s))

        self.guardar_valores()

    def actualizar_labels(self):
        self.label_valor_p.config(text=str(self.valor_p))
        self.label_valor_s.config(text=str(self.valor_s))

    def on_closing(self):
        self.guardar_valores()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    try:
        app = EditorTXT(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Error al iniciar la aplicación: {e}")