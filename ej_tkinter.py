import tkinter as tk
from tkinter import ttk
import random
from tkinter.messagebox import showinfo
from tkinter import messagebox

#EJERCICIO 1 (HELLO WORLD)
#root = tk.Tk()
#message = tk.Label(root, text="Gerson Borile")
#message.pack()
#root.mainloop()

#EJERCICIO2 (HELLO WORLD)

#root = tk.Tk()
#message = tk.Label(root, text="Algoritmos y estructuras de datos")
#message.pack()
#root.mainloop()

#EJERCICIO 1 (WINDOW)

#root = tk.Tk()
#root.title("Ventana de aplicacion")
#window_width = 500
#window_height = 300
#screen_width = root.winfo_screenwidth()
#screen_height = root.winfo_screenheight()
#center_x = int(screen_width/2 - window_width / 2)
#center_y = int(screen_height/2 - window_height / 2)
#root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#root.mainloop()

#EJERCICIO 2 (WINDOW)

#root =tk.Tk()
#root.geometry("400x250")
#root.resizable(False,False)
#root.attributes('-alpha', 0.7)
#root.mainloop()

#EJERCICIO 3 (WINDOW)

#root=tk.Tk()
#root.title("Ventana en primer plano")
#root.attributes('-topmost', -1)
#root.iconbitmap('./assets/icono.ico')
#root.mainloop()

#EJERCICIO 1 (WIDGETS)

#def saludar():
#    print("¡Hola! Bienvenido/a a la aplicación")

#root=tk.Tk()
#button = ttk.Button(root, text="¡Hola! Bienvenido/a a la aplicación", command=saludar)
#button.pack(pady=20)
#root.mainloop()


#EJERCICIO 2 (WIDGETS)

#colores = ["red", "green", "blue", "yellow", "magenta", "black", "white", "orange", "pink", "gray"]

#def cambiar_color():
#   color = random.choice(colores)
#    root.config(bg=color)


#root = tk.Tk()
#root.title("Botón de cambio de color")
#root.geometry("400x200")

#boton = tk.Button(root, text="Cambiar Color", command=cambiar_color)
#boton.pack(pady=50)
#root.mainloop()

#EJERCICIO 3 (WIDGETS)

#root = tk.Tk()
#root.title('Boton descargar')

#def boton_clicado():
#    showinfo(
#        title='Informacion',
#        message='Boton descargar clicado'
#    )

#download_icon = tk.PhotoImage(file='./assets/download.png')
#download_button = ttk.Button(
#    root,
#    image=download_icon,
#    text='Descargar',
#    compound=tk.LEFT,
#    command=boton_clicado
#)

#download_button.pack(
#    ipadx=5,
#   ipady=5,
#   expand=True
#)
#root.mainloop()


#EJERCICIO 1 (CHECKBOX)

#root = tk.Tk()
#root.geometry('300x200')
#root.resizable(False, False)
#root.title('Checkbox')

#aceptacion = tk.StringVar()


#def aceptacion_cambio():
#    tk.messagebox.showinfo(title='Resultado',
#                        message=aceptacion.get())


#ttk.Checkbutton(root,
#                text='Acepto los terminos y condiciones',
#                command=aceptacion_cambio,
#                variable=aceptacion,
#                onvalue='"Has aceptado los términos"',
#                offvalue='"No has aceptado los términos"').pack()


#root.mainloop()


#EJERCICIO 2 (CHECKBOX)

#root = tk.Tk()
#root.geometry('300x200')
#root.resizable(False, False)
#root.title('Checkbox')

#notificacion = tk.StringVar()


#def notificacion_correo():
#    tk.messagebox.showinfo(title='Resultado',
#                        message=notificacion.get())


#ttk.Checkbutton(root,
#                text='Recibir notificaciones por correo',
#                command=notificacion_correo,
#                variable=notificacion,
#                onvalue='Recibiras notificacion por correo',
#                offvalue='Debes seleccionar una opcion').pack()


#def notificacion_sms():
  #  tk.messagebox.showinfo(title='Resultado',
 #                       message=notificacion.get())


#ttk.Checkbutton(root,
                #text='Recibir notificaciones por sms',
                #command=notificacion_sms,
                #variable=notificacion,
                #onvalue='Recibiras notificacion por sms',
                #offvalue= "Debes seleccionar una opcion").pack()


#root.mainloop()


#EJERCICIO 1 (ENTRY)

#root = tk.Tk()
#root.geometry("300x150")
#root.resizable(False, False)
#root.title('Sign In')


#nombre = tk.StringVar()

#def mostrar_nombre():

#    msg = f"El nombre ingresado es {nombre}"
#    showinfo(
#        title='Información',
#        message=msg
 #   )


#entrada = ttk.Entry(root, textvariable=nombre)
#entrada.pack(pady=20)

#boton = tk.Button(root, text="Mostrar nombre", command=mostrar_nombre)
#boton.pack(pady=10)

#root.mainloop()

#EJERCICIO 2 (ENTRY)

#root = tk.Tk()
#root.geometry("300x150")
#root.resizable(False, False)
#root.title('Acceso')


#usuario = tk.StringVar()
#contraseña = tk.StringVar()


#def mensaje_contraseña():

#    msg = 'Contraseña ingresada'
#    showinfo(
#        title='Information',
#        message=msg
#    )



#signin = ttk.Frame(root)
#signin.pack(padx=10, pady=10, fill='x', expand=True)



#usuario_label = ttk.Label(signin, text="Usuario:")
#usuario_label.pack(fill='x', expand=True)

#usuario_entry = ttk.Entry(signin, textvariable=usuario)
#usuario_entry.pack(fill='x', expand=True)
#usuario_entry.focus()


#contraseña_label = ttk.Label(signin, text="Contraseña:")
#contraseña_label.pack(fill='x', expand=True)

#contraseña_entry = ttk.Entry(signin, textvariable=contraseña, show="*")
#contraseña_entry.pack(fill='x', expand=True)

#login_button = ttk.Button(signin, text="Acceso", command=mensaje_contraseña)
#login_button.pack(fill='x', expand=True, pady=10)


#root.mainloop()


#EJERCICIO 3 (ENTRY)

#root = tk.Tk()
#root.title('Acceso')


#usuario = tk.StringVar()
#contraseña = tk.StringVar()
#telefono = tk.StringVar()


#def submit():

#    usuario_valor = usuario.get()
#    contraseña_valor = contraseña.get()
#    telefono_valor = telefono.get()


#    if not usuario_valor or not contraseña_valor or not telefono_valor:
#        messagebox.showwarning("Campos incompletos, completa todos los campos.")



#signin = ttk.Frame(root)
#signin.pack(padx=10, pady=10, fill='x', expand=True)

#usuario_label = ttk.Label(signin, text="Usuario:")
#usuario_label.pack(fill='x', expand=True)
#usuario_entry = ttk.Entry(signin, textvariable=usuario)
#usuario_entry.pack(fill='x', expand=True)
#usuario_entry.focus()


#contraseña_label = ttk.Label(signin, text="Contraseña:")
#contraseña_label.pack(fill='x', expand=True)
#contraseña_entry = ttk.Entry(signin, textvariable=contraseña, show="*")
#contraseña_entry.pack(fill='x', expand=True)

#telefono_label = ttk.Label(signin, text="Teléfono:")
#telefono_label.pack(fill='x', expand=True)
#telefono_entry = ttk.Entry(signin, textvariable=telefono)
#telefono_entry.pack(fill='x', expand=True)

#login_button = ttk.Button(signin, text="Acceso", command=submit)
#login_button.pack(fill='x', expand=True, pady=10)


#root.mainloop()

#EJERCICIO 1 (FRAME)

#root=tk.Tk()
#frame=ttk.Frame(root, relief="ridge", borderwidth=3)
#frame.pack(padx=10, pady=10, fill="both", expand=True)
#label = ttk.Label(frame, text="Hola desde el frame")
#label.pack(padx=10, pady=10)
#root.mainloop()

#EJERCICIO 2 (FRAME)


# root = tk.Tk()

# entry_frame = ttk.Frame(root, padding="10")
# entry_frame.pack(padx=10, pady=10, fill="x", expand=True)

# nombre_label = ttk.Label(entry_frame, text="Nombre:")
# nombre_label.pack(fill='x', pady=5)
# nombre_entry = ttk.Entry(entry_frame)
# nombre_entry.pack(fill='x', pady=5)

# edad_label = ttk.Label(entry_frame, text="Edad:")
# edad_label.pack(fill='x', pady=5)
# edad_entry = ttk.Entry(entry_frame)
# edad_entry.pack(fill='x', pady=5)

# button_frame = ttk.Frame(root, padding="10")
# button_frame.pack(padx=10, pady=10, fill="x", expand=True)

# accept_button = ttk.Button(button_frame, text="Aceptar")
# accept_button.pack(side="left", padx=10)

# cancel_button = ttk.Button(button_frame, text="Cancelar")
# cancel_button.pack(side="left", padx=10)

# root.mainloop()


#EJERCICIO 3 (FRAME)

# root = tk.Tk()

# frame_flat = ttk.Frame(root, relief="flat", borderwidth=3, padding="10")
# frame_flat.pack(padx=10, pady=10, fill="both", expand=True)

# label_flat = ttk.Label(frame_flat, text="Borde: Flat")
# label_flat.pack(padx=10, pady=10)

# frame_groove = ttk.Frame(root, relief="groove", borderwidth=3, padding="10")
# frame_groove.pack(padx=10, pady=10, fill="both", expand=True)

# label_groove = ttk.Label(frame_groove, text="Borde: Groove")
# label_groove.pack(padx=10, pady=10)

# frame_sunken = ttk.Frame(root, relief="sunken", borderwidth=3, padding="10")
# frame_sunken.pack(padx=10, pady=10, fill="both", expand=True)

# label_sunken = ttk.Label(frame_sunken, text="Borde: Sunken")
# label_sunken.pack(padx=10, pady=10)

# root.mainloop()

#EJERCICIO 1 (LABEL)

# import tkinter as tk
# from tkinter import ttk

# EJERCICIO 1
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Label')

# label = ttk.Label(
#     root,                     
#     text='Bienvenido a Tkinter',  
#     font=("Helvetica", 16),    
#     background="blue"         
# )

# label.pack(ipadx=10, ipady=10)

# root.mainloop()


# EJERCICIO 2 (LABEL)
# root = tk.Tk()

# root.geometry('300x200')

# root.title('Label Imagen')

# imagen = tk.PhotoImage(file='./assets/cumpleañito.png')

# image_label = ttk.Label(
#     root,         
#     image=imagen, 
#     padding=5     
# )

# image_label.pack()

# root.mainloop()


# EJERCICIO 3 (LABEL)
# root = tk.Tk()

# root.geometry('300x200')

# root.title('Label Texto e Imagen')

# foto = tk.PhotoImage(file='./assets/cumpleañito.png')

# image_label = ttk.Label(
#     root,        
#     image=foto,   
#     text='Cumpleaños',  
#     compound='top'  
# )

# image_label.pack()

# root.mainloop()

#EJERCICIO 1 (LabelFrame)

# root = tk.Tk()

# root.geometry('300x200')

# root.resizable(False, False)

# root.title('Seleccionar idioma')

# lf = ttk.LabelFrame(root, text='idiomas')

# lf.grid(column=0, row=0, padx=20, pady=20)

# idiomas_var = tk.StringVar()

# opciones = ('Español', 'Ingles', 'Frances')

# grid_column = 0

# for idiomas in opciones:
    # radio = ttk.Radiobutton(lf, text=idiomas, value=idiomas, variable=idiomas_var)
    # radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    # grid_column += 1

# root.mainloop()

# EJERCICIO 2 (LabelFrame)

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# root.geometry('300x200')

# root.resizable(False, False)

# root.title('Preferencias de interfaz')

# lf = ttk.LabelFrame(root, text='Preferencias de interfaz')

# lf.grid(column=0, row=0, padx=20, pady=20)

# modo_var = tk.StringVar()

# opciones = ('Modo Claro', 'Modo Oscuro')

# grid_column = 0

# for modo in opciones:
    # radio = ttk.Radiobutton(lf, text=modo, value=modo, variable=modo_var, command=lambda: cambiar_modo(modo_var.get()))
    # radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    # grid_column += 1

# def cambiar_modo(modo):
    # if modo == "Modo Claro":
        # root.config(bg="white")
        # lf.config(bg="white")
    # else:
        # root.config(bg="gray20")
        # lf.config(bg="gray20")

# root.mainloop()

# EJERCICIO 3 (LabelFrame)

# root = tk.Tk()

# root.geometry('300x200')

# root.resizable(False, False)

# root.title('Controles de Volumen')

# lf = ttk.LabelFrame(root, text='Controles de Volumen')

# lf.grid(column=0, row=0, padx=20, pady=20)

# volumen_var = tk.StringVar()

# opciones = ('Bajo', 'Medio', 'Alto')

# def mostrar_volumen():
    # nivel = volumen_var.get()
    # label_volumen.config(text=f"Nivel de volumen: {nivel}")

# grid_column = 0

# for volumen in opciones:
    # radio = ttk.Radiobutton(lf, text=volumen, value=volumen, variable=volumen_var, command=mostrar_volumen)
    # radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    # grid_column += 1

# label_volumen = ttk.Label(root, text="Nivel de volumen: Ninguno")

# label_volumen.grid(column=0, row=1, pady=10)

# root.mainloop()

#EJERCICIO 1 (MenuButton)

# from tkinter import Menu

# def cambiar_tema(tema):
#     if tema == "Claro":
#         root.config(bg="white")
#         root.config(fg="black")
#     elif tema == "Oscuro":
#         root.config(bg="black")
#         root.config(fg="white")
#     else:
#         root.config(bg="SystemButtonFace")
#         root.config(fg="black")

# root = tk.Tk()
# root.geometry('300x200')
# root.title('Seleccionar Tema')

# menubutton = tk.Menubutton(root, text="Seleccionar Tema", relief="raised")
# menubutton.pack(padx=20, pady=20)

# menu = Menu(menubutton, tearoff=0)
# menu.add_command(label="Claro", command=lambda: cambiar_tema("Claro"))
# menu.add_command(label="Oscuro", command=lambda: cambiar_tema("Oscuro"))
# menu.add_command(label="Por Defecto", command=lambda: cambiar_tema("Por Defecto"))

# menubutton.config(menu=menu)

# root.mainloop()

# EJERCICIO 2 (MenuButton)

# import tkinter as tk
# from tkinter import Menu

# def cambiar_volumen(nivel):
#     if nivel == "Silencio":
#         root.config(bg="white")
#     elif nivel == "Bajo":
#         root.config(bg="yellow")
#     elif nivel == "Medio":
#         root.config(bg="green")
#     elif nivel == "Alto":
#         root.config(bg="red")

# root = tk.Tk()
# root.geometry('300x200')
# root.title('Control de Volumen')

# menubutton = tk.Menubutton(root, text="Control de Volumen", relief="raised")
# menubutton.pack(padx=20, pady=20)

# menu = Menu(menubutton, tearoff=0)
# menu.add_command(label="Silencio", command=lambda: cambiar_volumen("Silencio"))
# menu.add_command(label="Bajo", command=lambda: cambiar_volumen("Bajo"))
# menu.add_command(label="Medio", command=lambda: cambiar_volumen("Medio"))
# menu.add_command(label="Alto", command=lambda: cambiar_volumen("Alto"))

# menubutton.config(menu=menu)

# root.mainloop()

# EJERCICIO 3 (MenuButton)

# import tkinter as tk
# from tkinter import Menu

# def cambiar_idioma(idioma):
#     if idioma == "Español":
#         label.config(text="Hola")
#     elif idioma == "Inglés":
#         label.config(text="Hello")
#     elif idioma == "Francés":
#         label.config(text="Bonjour")

# root = tk.Tk()
# root.geometry('300x200')
# root.title('Seleccionar Idioma')

# menubutton = tk.Menubutton(root, text="Seleccionar Idioma", relief="raised")
# menubutton.pack(padx=20, pady=20)

# menu = Menu(menubutton, tearoff=0)
# menu.add_command(label="Español", command=lambda: cambiar_idioma("Español"))
# menu.add_command(label="Ingles", command=lambda: cambiar_idioma("Ingles"))
# menu.add_command(label="Francés", command=lambda: cambiar_idioma("Francés"))

# menubutton.config(menu=menu)

# label = tk.Label(root, text="Selecciona un idioma", font=("Helvetica", 16))
# label.pack(pady=20)

# root.mainloop()

#EJERCICIO 1 (PanedWindow)
# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.geometry('300x200')
# root.title('Paned Window')

# paned_window = ttk.PanedWindow(root, orient=tk.VERTICAL)
# paned_window.pack(fill=tk.BOTH, expand=True)

# label = ttk.Label(paned_window, text="Arrastra la barra")
# paned_window.add(label)

# listbox = tk.Listbox(paned_window)
# frutas = ['Manzana', 'Banana', 'Naranja', 'Sandia']
# for fruta in frutas:
#     listbox.insert(tk.END, fruta)
# paned_window.add(listbox)

# root.mainloop()

#EJERCICIO 2 (PanedWindow)

# root = tk.Tk()
# root.geometry('400x200')
# root.title('Paned Window')

# paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
# paned_window.pack(fill=tk.BOTH, expand=True)

# columna1 = ttk.Label(paned_window, text="Columna 1", width=20, anchor="center")
# paned_window.add(columna1)

# columna2 = ttk.Label(paned_window, text="Columna 2", width=20, anchor="center")
# paned_window.add(columna2)

# columna3 = ttk.Label(paned_window, text="Columna 3", width=20, anchor="center")
# paned_window.add(columna3)

# root.mainloop()

#EJERCICIO 3 (PanedWindow)

# def enviar_mensaje():
#     mensaje = entry.get()
#     text_chat.insert(tk.END, "Otro: " + mensaje + "\n")
#     entry.delete(0, tk.END)

# root = tk.Tk()
# root.geometry('400x300')
# root.title('Chat')

# paned_window = ttk.PanedWindow(root, orient=tk.VERTICAL)
# paned_window.pack(fill=tk.BOTH, expand=True)

# text_chat = tk.Text(paned_window, height=10, width=50, state=tk.DISABLED)
# paned_window.add(text_chat)

# bottom_frame = ttk.Frame(paned_window)
# entry = ttk.Entry(bottom_frame, width=40)
# entry.pack(side=tk.LEFT, padx=5)
# send_button = ttk.Button(bottom_frame, text="Enviar", command=enviar_mensaje)
# send_button.pack(side=tk.LEFT)
# paned_window.add(bottom_frame)

# root.mainloop()

#ejercicio 1 (radiobutton)

#root = tk.Tk()
#root.geometry('300x220')
#root.resizable(False, False)
#root.title('Selección de Color')

#def mostrar_color_elegido():
#    showinfo(
#        title='Resultado',
#        message=f"Color seleccionado: {color_elegido.get()}"
#    )

#color_elegido = tk.StringVar()
#colores = ('Rojo', 'Verde', 'Azul')

#label = ttk.Label(root, text="Elegi un color")
#label.pack(fill='x', padx=5, pady=5)

#for color in colores:
#    r = ttk.Radiobutton(
#        root,
#        text=color,
#        value=color,
#        variable=color_elegido
#    )
#    r.pack(fill='x', padx=5, pady=5)

#button = ttk.Button(
#    root,
#    text="Confirmar Seleccióo",
#    command=mostrar_color_elegido
#)

#button.pack(fill='x', padx=5, pady=5)

#root.mainloop()

#ejercicio 2 (panedwindow)

#root = tk.Tk()
#root.geometry('300x220')
#root.resizable(False, False)
#root.title('Seleccion de genero')

#def mostrar_genero_elegido():
#    showinfo(
#        title='Resultado',
#        message=f"Genero seleccionado: {genero_elegido.get()}"
#    )

#genero_elegido = tk.StringVar()
#generos = ('Masculino', 'Femenino', 'Otro')

#label = ttk.Label(root, text="cual es tu genero?")
#label.pack(fill='x', padx=5, pady=5)

#for genero in generos:
#    r = ttk.Radiobutton(
#        root,
#        text=genero,
#        value=genero,
#        variable=genero_elegido
#    )
#    r.pack(fill='x', padx=5, pady=5)

#button = ttk.Button(
#    root,
#    text="Confirmar",
#    command=mostrar_genero_elegido
#)

#button.pack(fill='x', padx=5, pady=5)

#root.mainloop()

#ejercicio 3 (paned window)

#root = tk.Tk()
#root.geometry('300x220')
#root.resizable(False, False)
#root.title('Seleccion de Tipo de Cafe')

#def mostrar_tipo_de_cafe():
#    showinfo(
#        title='Confirmacion de pedido',
#        message=f"Tipo de cafe seleccionado: {tipo_de_cafe.get()}"
#    )

#tipo_de_cafe = tk.StringVar()
#cafes = ('Café Negro', 'Latte', 'Capuchino')

#label = ttk.Label(root, text="elegi un tipo de cafe")
#label.pack(fill='x', padx=5, pady=5)

#for cafe in cafes:
#    r = ttk.Radiobutton(
#        root,
#        text=cafe,
#        value=cafe,
#        variable=tipo_de_cafe
#    )
#    r.pack(fill='x', padx=5, pady=5)

#button = ttk.Button(
#    root,
#    text="Confirmar Pedido",
#    command=mostrar_tipo_de_cafe
#)

#button.pack(fill='x', padx=5, pady=5)

#root.mainloop()

# Ejercicio 1 (Slider)

# root = tk.Tk()
# root.geometry('300x200')
# root.title('Volumen')

# def config_volumen(val):
#     label.config(text=f"Volumen: {val}%")

# volumen = tk.DoubleVar()
# volumen.set(50)

# slider = tk.Scale(
#     root,
#     from_=0,
#     to=100,
#     orient="horizontal",
#     variable=volumen,
#     command=config_volumen
# )
# slider.pack(fill='x', padx=5, pady=5)

# label = tk.Label(root, text=f"Volumen: {volumen.get()}%")
# label.pack(fill='x', padx=5, pady=5)

# root.mainloop()

# Ejercicio 2 (Slider)

# root = tk.Tk()
# root.geometry('300x200')
# root.title('Brillo')

# def actualizar_brillo(val):
#     etiqueta.config(text=f"Brillo: {val}%")

# brillo = tk.DoubleVar()
# brillo.set(50)

# slider = tk.Scale(
#     root,
#     from_=100,
#     to=0,
#     orient="vertical",
#     variable=brillo,
#     command=actualizar_brillo
# )
# slider.pack(fill='y', padx=5, pady=5)

# etiqueta = tk.Label(root, text=f"Brillo: {brillo.get()}%")
# etiqueta.pack(fill='x', padx=5, pady=5)

# root.mainloop()

# Ejercicio 3 (Slider)

# def actualizar_temperatura(val):
#     temperatura_label.config(text=f"Temperatura: {val}°C")

# root = tk.Tk()
# root.geometry('300x200')
# root.title('Termostato')

# temperatura_label = tk.Label(root, text="Temperatura: 0°C", font=("Helvetica", 14))
# temperatura_label.pack(pady=10)

# slider_temperatura = tk.Scale(root, from_=-10, to=40, orient="horizontal", command=actualizar_temperatura)
# slider_temperatura.pack(pady=20)

# root.mainloop()

# Ejercicio 1 (Spinbox)

# def mostrar_edad():
#     edad = edad_var.get()
#     label.config(text=f"Edad seleccionada: {edad} años")

# root = tk.Tk()
# root.geometry('300x200')
# root.title('Edad')

# edad_var = tk.StringVar()

# spinbox = ttk.Spinbox(root, from_=0, to=100, textvariable=edad_var)
# spinbox.pack(padx=5, pady=5)

# label = ttk.Label(root, text="Edad seleccionada: 0 años")
# label.pack(padx=5, pady=5)

# button = ttk.Button(root, text="Mostrar Edad", command=mostrar_edad)
# button.pack(padx=5, pady=5)

# root.mainloop()


# Ejercicio 2 (SpinBox)

# def actualizar_cantidad():
#     cantidad = cantidad_var.get()
#     label.config(text=f"Cantidad seleccionada: {cantidad}")

# root = tk.Tk()
# root.geometry('300x200')
# root.title('Ajuste de Cantidad de Productos')

# cantidad_var = tk.IntVar()

# spinbox = ttk.Spinbox(root, from_=1, to=10, textvariable=cantidad_var, command=actualizar_cantidad)
# spinbox.pack(padx=5, pady=5)

# label = ttk.Label(root, text="Cantidad seleccionada: 1")
# label.pack(padx=5, pady=5)

# root.mainloop()


# Ejercicio 3 (Spinbox)

# import tkinter as tk
# from tkinter import ttk

# def actualizar_hora():
#     hora = hora_var.get()
#     minuto = minuto_var.get()
#     etiqueta.config(text=f"Hora seleccionada: {hora}:{minuto:02d}")

# root = tk.Tk()
# root.geometry('300x200')
# root.title('Seleccion de hora')

# hora_var = tk.IntVar()
# minuto_var = tk.IntVar()

# spinbox_hora = ttk.Spinbox(root, from_=1, to=12, textvariable=hora_var, width=5, command=actualizar_hora)
# spinbox_hora.pack(padx=5, pady=5)

# spinbox_minuto = ttk.Spinbox(root, from_=0, to=59, textvariable=minuto_var, width=5, command=actualizar_hora)
# spinbox_minuto.pack(padx=5, pady=5)

# etiqueta = ttk.Label(root, text="Hora seleccionada: 1:00")
# etiqueta.pack(padx=5, pady=5)

# root.mainloop()

# Ejercicio 1 (Combobox)

# def mostrar_dia(event):
#     dia = combobox.get()
#     etiqueta.config(text=f"Dia seleccionado: {dia}")

# root = tk.Tk()
# root.geometry('300x200')
# root.title('Seleccion de Dia')

# dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# combobox = ttk.Combobox(root, values=dias)
# combobox.set('Lunes') 
# combobox.pack(padx=5, pady=5)

# combobox.bind('<<ComboboxSelected>>', mostrar_dia)

# etiqueta = ttk.Label(root, text="Dia seleccionado: Lunes")
# etiqueta.pack(padx=5, pady=5)

# root.mainloop()

# Ejericio 2 (ComboBox)

# def mostrar_tema_seleccionado(event):
#     tema = combobox.get()
#     showinfo(title="Tema Seleccionado", message=f"Has seleccionado el tema: {tema}")

# root = tk.Tk()
# root.geometry('300x200')
# root.title('Selección de Tema')

# temas = ['Economía Circular', 'Energía Renovable', 'Tecnología']

# combobox = ttk.Combobox(root, values=temas, state='readonly')
# combobox.set('Economía Circular')
# combobox.pack(padx=5, pady=5)

# combobox.bind('<<ComboboxSelected>>', mostrar_tema_seleccionado)

# root.mainloop()

# EjERCICIO 3 (ComboBox)

# import calendar

# def mostrar_mes_seleccionado(event):
#     mes = combobox.get()
#     numero_mes = list(calendar.month_name).index(mes)
#     showinfo(title="Mes Seleccionado", message=f"Has seleccionado el mes {mes}, el número de mes es: {numero_mes}")

# root = tk.Tk()
# root.geometry('300x200')
# root.title('Selección de Mes')

# meses = list(calendar.month_name)[1:]

# combobox = ttk.Combobox(root, values=meses, state='readonly')
# combobox.set('Enero')
# combobox.pack(padx=5, pady=5)

# combobox.bind('<<ComboboxSelected>>', mostrar_mes_seleccionado)

# root.mainloop()

# Ejercicio 1 (Notebook)

# root = tk.Tk()
# root.geometry('600x300')
# root.title('Pestañas')

# notebook = ttk.Notebook(root)
# notebook.pack(fill='both', expand=True)

# pagina_inicio = ttk.Frame(notebook)
# notebook.add(pagina_inicio, text='Inicio')
# label_inicio = ttk.Label(pagina_inicio, text="Bienvenido a la página principal")
# label_inicio.pack(padx=10, pady=10)

# pagina_config = ttk.Frame(notebook)
# notebook.add(pagina_config, text='Configuración')
# button_guardar = ttk.Button(pagina_config, text="Guardar cambios")
# button_guardar.pack(padx=10, pady=10)

# pagina_ayuda = ttk.Frame(notebook)
# notebook.add(pagina_ayuda, text='Ayuda')
# lista_faq = tk.Listbox(pagina_ayuda)
# lista_faq.pack(padx=10, pady=10)
# preguntas = ["Como usar la aplicación?", "Donde guardar los archivos?"]
# for pregunta in preguntas:
#     lista_faq.insert(tk.END, pregunta)

# root.mainloop()

# Ejercicios 2 (Notebook)

# def mostrar_resumen():
#     nombre = entry_nombre.get()
#     correo = entry_correo.get()
#     etiqueta_resumen.config(text=f"Nombre: {nombre}\nCorreo: {correo}")

# root = tk.Tk()
# root.geometry('400x300')
# root.title('Formulario y Resumen')

# notebook = ttk.Notebook(root)
# notebook.pack(fill='both', expand=True)

# pestana_registro = ttk.Frame(notebook)
# notebook.add(pestana_registro, text="Registro")

# label_nombre = ttk.Label(pestana_registro, text="Nombre:")
# label_nombre.pack(padx=10, pady=5)
# entry_nombre = ttk.Entry(pestana_registro)
# entry_nombre.pack(padx=10, pady=5)

# label_correo = ttk.Label(pestana_registro, text="Correo:")
# label_correo.pack(padx=10, pady=5)
# entry_correo = ttk.Entry(pestana_registro)
# entry_correo.pack(padx=10, pady=5)

# boton_enviar = ttk.Button(pestana_registro, text="Enviar", command=mostrar_resumen)
# boton_enviar.pack(padx=10, pady=10)

# pestana_resumen = ttk.Frame(notebook)
# notebook.add(pestana_resumen, text="Resumen")

# etiqueta_resumen = ttk.Label(pestana_resumen, text="Nombre: \nCorreo: ", font=("Helvetica", 14))
# etiqueta_resumen.pack(padx=10, pady=20)

# root.mainloop()

# Ejercicio 3 (Notebook)

# def ocultar_pestana():
#     notebook.hide(pestana2)

# def mostrar_pestana():
#     notebook.add(pestana2, text="Tab 2")

# root = tk.Tk()
# root.geometry('400x300')
# root.title('ocultar pestaña')

# notebook = ttk.Notebook(root)
# notebook.pack(fill='both', expand=True)

# pestana1 = ttk.Frame(notebook)
# notebook.add(pestana1, text="Tab 1")
# label1 = ttk.Label(pestana1, text="Contenido de la pestaña 1")
# label1.pack(padx=10, pady=10)

# pestana2 = ttk.Frame(notebook)
# noteboook.add(pestana2, text="Tab 2")
# label2 = ttk.Label(pestana2, text="Contenido de la pestaña 2")
# label2.pack(padx=10, pady=10)

# pestana3 = ttk.Frame(notebook)
# notebook.add(pestana3, text="Tab 3")
# label3 = ttk.Label(pestana3, text="Contenido de la pestaña 3")
# label3.pack(padx=10, pady=10)

# boton_ocultar = ttk.Button(root, text="Ocultar Pestaña 2", command=ocultar_pestana)
# boton_ocultar.pack(padx=10, pady=10)

# boton_mostrar = ttk.Button(root, text="Mostrar Pestaña 2", command=mostrar_pestana)
# boton_mostrar.pack(padx=10, pady=10)

# root.mainloop()

#Ejercicio 1 (ProgressBar)
# def iniciar():
#     progressbar.start()
# 
# def detener():
#     progressbar.stop()
# 
# root = tk.Tk()
# root.geometry('400x200')
# root.title('Progressbar ')
# 
# progressbar = ttk.Progressbar(root, length=300, mode='indeterminate')
# progressbar.pack(padx=10, pady=20)
# 
# boton_iniciar = ttk.Button(root, text="Iniciar", command=iniciar)
# boton_iniciar.pack(padx=10, pady=5)
# 
# boton_detener = ttk.Button(root, text="Detener", command=detener)
# boton_detener.pack(padx=10, pady=5)
# 
# root.mainloop()

#Ejercicio 2 (ProgressBar)

# 
# def avanzar():
#     global progreso
#     progreso += 20
#     progressbar["value"] = progreso
#     etiqueta.config(text=f"Progreso: {progreso}%")
#     if progreso == 100:
#         messagebox.showinfo("Completado", "Progreso completado")
# 
# def detener():
#     global progreso
#     progreso = progressbar["value"]
#     etiqueta.config(text=f"Progreso: {progreso}%")
# 
# root = tk.Tk()
# root.geometry('400x200')
# root.title('Progressbar con Progreso')
# 
# progreso = 0
# 
# progressbar = ttk.Progressbar(root, length=300, mode='determinate', maximum=100)
# progressbar.pack(padx=10, pady=20)
# 
# etiqueta = ttk.Label(root, text=f"Progreso: {progreso}%")
# etiqueta.pack(padx=10, pady=5)
# 
# boton_avanzar = ttk.Button(root, text="Avanzar", command=avanzar)
# boton_avanzar.pack(padx=10, pady=5)
# 
# boton_detener = ttk.Button(root, text="Detener", command=detener)
# boton_detener.pack(padx=10, pady=5)
# 
# root.mainloop()

#EJERCICIO 3 (ProgressBar)


# def actualizar_progreso():
#     global progreso
#     if progreso < 100:
#         progreso += 1
#         progressbar.step(1)  
#         etiqueta.config(text=f"Progreso: {progreso}%")
#         root.after(100, actualizar_progreso)  # Actualiza cada 100ms
#     else:
#         etiqueta.config(text="Progreso completado")
# 
# root = tk.Tk()
# root.geometry('400x200')
# root.title('Progressbar ')
# 
# progreso = 0
# 
# # Estilo personalizado
# style = ttk.Style()
# style.configure("TProgressbar",
#                 thickness=30,  # Grosor de la barra
#                 length=300,  # Largo de la barra
#                 barcolor='blue',  # Color de la barra
#                 )
# 
# progressbar = ttk.Progressbar(root, style="TProgressbar", mode='determinate', maximum=100)
# progressbar.pack(padx=10, pady=20)
# 
# etiqueta = ttk.Label(root, text=f"Progreso: {progreso}%")
# etiqueta.pack(padx=10, pady=5)
# 
# boton_iniciar = ttk.Button(root, text="Iniciar", command=actualizar_progreso)
# boton_iniciar.pack(padx=10, pady=5)
# 
# root.mainloop()

#EJERCICIO 1 (Separator)

def boton1_presionado():
    print("Boton 1 presionado")

def boton2_presionado():
    print("Boton 2 presionado")

root = tk.Tk()
root.geometry('400x200')
root.title('Separador')

boton1 = ttk.Button(root, text="Boton 1", command=boton1_presionado)
boton1.pack(padx=10, pady=10)

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', padx=10)

boton2 = ttk.Button(root, text="Botón 2", command=boton2_presionado)
boton2.pack(padx=10, pady=10)

root.mainloop()

#Ejercicio 2 (Separator)

root = tk.Tk()
root.geometry('400x200')
root.title('Separador Vertical')

frame_izquierda = ttk.Frame(root, width=150)
frame_izquierda.pack(side='left', fill='y', padx=10, pady=10)

label_izquierda = ttk.Label(frame_izquierda, text="Izquierda")
label_izquierda.pack(padx=10, pady=10)

separator = ttk.Separator(root, orient='vertical')
separator.pack(side='left', fill='y', padx=10)

frame_derecha = ttk.Frame(root, width=150)
frame_derecha.pack(side='right', fill='y', padx=10, pady=10)

label_derecha = ttk.Label(frame_derecha, text="Derecha")
label_derecha.pack(padx=10, pady=10)

root.mainloop()

#Ejercicio 3 (Separator)



def imprimir_valores():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    correo = entry_correo.get()
    print(f"Nombre: {nombre}, Apellido: {apellido}, Correo: {correo}")

root = tk.Tk()
root.geometry('400x300')
root.title('Separador')


label_nombre = ttk.Label(root, text="Nombre:")
label_nombre.pack(padx=10, pady=5)
entry_nombre = ttk.Entry(root)
entry_nombre.pack(padx=10, pady=5)


separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', padx=10, pady=10)


label_apellido = ttk.Label(root, text="Apellido:")
label_apellido.pack(padx=10, pady=5)
entry_apellido = ttk.Entry(root)
entry_apellido.pack(padx=10, pady=5)

label_correo = ttk.Label(root, text="Correo electronico:")
label_correo.pack(padx=10, pady=5)
entry_correo = ttk.Entry(root)
entry_correo.pack(padx=10, pady=5)

boton_enviar = ttk.Button(root, text="Enviar", command=imprimir_valores)
boton_enviar.pack(padx=10, pady=20)

root.mainloop()
