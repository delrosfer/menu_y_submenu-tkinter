import tkinter as tk
from tkinter import messagebox


def color_amarillo():
	ventana['bg'] = 'yellow'

def color_verde():
	ventana['bg'] = 'green'

def color_cafe():
	ventana['bg'] = 'brown'

def color_rojo():
	ventana['bg'] = 'red'

def color_gris():
	ventana['bg'] = 'gray'

def mensaje():
	answer=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
	if(answer):
		ventana.destroy()

ventana =tk.Tk()
ventana.title("Menu y submenu con Tkinter y Python")
ventana.geometry("600x300")

mi_menu = tk.Menu(ventana)
mi_menu.add_command(label='Amarillo', command=color_amarillo)
mi_menu.add_command(label='Verde', command=color_verde)
mi_menu.add_command(label='Cafe', command=color_cafe)

mi_dropdown_menu=tk.Menu(mi_menu, tearoff=0)

mi_dropdown_menu.add_command(label='Rojo', command=color_rojo)
mi_dropdown_menu.add_command(label='Gris', command=color_gris)

mi_menu.add_cascade(label='Otros Colores', menu=mi_dropdown_menu)

mi_menu.add_command(label='Salir', command=mensaje)

ventana.config(menu=mi_menu)

ventana.mainloop()