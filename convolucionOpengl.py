#Universidad Central del ecuador
#Facultad de ingenieria y ciencias aplicadas
#Victor Daniel Maldonado Nolivos
#Programa que enseña el funcionamiento de convolucion usando Opengl
#Selecciona una imagen y aplica los filtros
import tkinter as tk
from tkinter import filedialog, Label, Button
import pygame
from OpenGL.GL import *
from PIL import Image, ImageTk, ImageFilter
import numpy as np

# Inicialización global
imagen_original = None
imagen_procesada = None
ventana_gl_creada = False
screen = None  # Variable para mantener la ventana pygame abierta

# Cargar imagen
def cargar_imagen():
    global imagen_original
    ruta = filedialog.askopenfilename(filetypes=[("Imagenes", "*.jpg *.png *.ico")])
    if ruta:
        try:
            imagen_original = Image.open(ruta)
            mostrar_imagen(imagen_original)
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

# Mostrar imagen en Tkinter
def mostrar_imagen(imagen):
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen.config(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk

# Aplicar filtro de borde
def filtro_borde():
    aplicar_filtro(ImageFilter.FIND_EDGES)

# Aplicar filtro de suavizado
def filtro_suavizado():
    aplicar_filtro(ImageFilter.SMOOTH)

# Filtro de desenfoque
def filtro_desenfoque():
    aplicar_filtro(ImageFilter.BLUR)

# Filtro de nitidez
def filtro_nitidez():
    aplicar_filtro(ImageFilter.SHARPEN)

# Aplicar filtro con OpenGL
def aplicar_filtro(filtro):
    global imagen_original, imagen_procesada
    if imagen_original:
        try:
            imagen_procesada = imagen_original.filter(filtro)
            mostrar_imagen(imagen_procesada)
        except Exception as e:
            print(f"Error al aplicar el filtro: {e}")

# Interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Procesamiento de Imágenes con Convolución")
root.geometry("400x300")

boton_cargar = Button(root, text="Cargar Imagen", command=cargar_imagen)
boton_cargar.pack()

boton_borde = Button(root, text="Filtro de Borde", command=filtro_borde)
boton_borde.pack()

boton_suavizado = Button(root, text="Filtro de Suavizado", command=filtro_suavizado)
boton_suavizado.pack()

boton_desenfoque = Button(root, text="Filtro de Desenfoque", command=filtro_desenfoque)
boton_desenfoque.pack()

boton_nitidez = Button(root, text="Filtro de Nitidez", command=filtro_nitidez)
boton_nitidez.pack()

etiqueta_imagen = Label(root)
etiqueta_imagen.pack()

root.mainloop()
