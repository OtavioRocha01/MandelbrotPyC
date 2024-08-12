import ctypes
import tkinter as tk
from tkinter import Canvas, PhotoImage
import numpy as np
import os

TAM_GRID = 500

# Carregando a biblioteca
# Testa o sistema operacional para o uso da flag
PATH = './mandelbrot.so'
if os.name == 'nt':
    mandelbrot_lib = ctypes.CDLL(PATH, winmode=0)
else:
    mandelbrot_lib = ctypes.CDLL(PATH)

class MANDELBROT(ctypes.Structure):
    _fields_ = [("x_ini", ctypes.c_double),
                ("y_ini", ctypes.c_double),
                ("passo", ctypes.c_double),
                ("incr", ctypes.c_double),
                ("contador", ctypes.c_int * TAM_GRID * TAM_GRID), 
                ("menor", ctypes.c_int),
                ("maior", ctypes.c_int),
                ("cor", ctypes.c_int),
                ("coord", ctypes.c_int),
                ]


def exibir_fractal(canvas, img, contador):
    min_val, max_val = contador.min(), contador.max()
    for y in range(TAM_GRID):
        for x in range(TAM_GRID):
            color_val = int(255 * (contador[y][x] - min_val) / (max_val - min_val))
            color = f"#{color_val:02x}{color_val:02x}{color_val:02x}"
            img.put(color, (x, y))
    
    canvas.create_image((TAM_GRID//2, TAM_GRID//2), image=img, state="normal")


def main():
    root = tk.Tk()
    root.title("Fractal de Mandelbrot")

    canvas = Canvas(root, width=TAM_GRID, height=TAM_GRID)
    canvas.pack()
    img = PhotoImage(width=TAM_GRID, height=TAM_GRID)

    # Definindo os tipos de retorno e argumentos das funções
    mandelbrot_lib.inicializa.restype = ctypes.POINTER(MANDELBROT)
    mandelbrot_lib.calcula.restype = ctypes.POINTER(MANDELBROT)
    
    M = mandelbrot_lib.inicializa()

    mandelbrot_lib.calcula(M)

    data = np.ctypeslib.as_array(M.contents.contador).reshape((TAM_GRID, TAM_GRID))

    exibir_fractal(canvas, img, data)

    root.mainloop()


if __name__ == '__main__':
    main()