import ctypes
import tkinter as tk
from tkinter import Canvas, PhotoImage
import numpy as np
import os

TAM_GRID = 500


# Carregando a biblioteca
# Testa o sistema operacional para o uso da flag
if os.name == 'nt':
    PATH = os.path.abspath('./mandelbrot.dll')
    mandelbrot_lib = ctypes.CDLL(PATH, winmode=0)
else:
    PATH = './mandelbrot.so'
    mandelbrot_lib = ctypes.CDLL(PATH)


# Definição da estrutura em C
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
            # Normaliza
            color_val = int(128 * (contador[y][x] - min_val) / (max_val - min_val))
            
            # Criando um gradiente de cores
            r = color_val
            g = int(255 * (1 - (color_val / 255)))
            b = int(255 * (1 - (color_val / 255)))

            # Formatação para hexadecimal
            color = f"#{r:02x}{g:02x}{b:02x}"
            img.put(color, (x, y))
    
    canvas.create_image((TAM_GRID//2, TAM_GRID//2), image=img, state="normal")


def main():
    # Definições do Tkinter
    # Cria a janela
    root = tk.Tk()
    root.title("Fractal de Mandelbrot")

    # Cria o canvas
    canvas = Canvas(root, width=TAM_GRID, height=TAM_GRID)
    canvas.pack()

    # Cria a imagem
    img = PhotoImage(width=TAM_GRID, height=TAM_GRID)

    # Definindo os tipos de retorno e argumentos das funções
    mandelbrot_lib.inicializa.restype = ctypes.POINTER(MANDELBROT)
    mandelbrot_lib.calcula.restype = ctypes.POINTER(MANDELBROT)
    
    # Inicializa a estrutura
    M = mandelbrot_lib.inicializa()

    # Calcula o fractal
    mandelbrot_lib.calcula(M)

    # Converte o ponteiro para um array numpy
    data = np.ctypeslib.as_array(M.contents.contador).reshape((TAM_GRID, TAM_GRID))

    # Exibe o fractal
    exibir_fractal(canvas, img, data)
    
    root.mainloop()


if __name__ == '__main__':
    main()