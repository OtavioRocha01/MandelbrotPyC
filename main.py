import tkinter as tk
from tkinter import Canvas, PhotoImage
import numpy as np


TAM_GRID = 500


def ler_contador(filename):
    data = np.fromfile(filename, dtype=np.float32)
    data = data.reshape((TAM_GRID, TAM_GRID))
    return data


def exibir_fractal(canvas, img, contador):
    min_val, max_val = contador.min(), contador.max()
    for y in range(TAM_GRID):
        for x in range(TAM_GRID):
            color_val = int(255 * (contador[y][x] - min_val) / (max_val - min_val))
            color = f"#{color_val:02x}{color_val:02x}{color_val:02x}"
            img.put(color, (x, y))
    
    canvas.create_image((TAM_GRID//2, TAM_GRID//2), image=img, state="normal")


def main():
    contador = ler_contador("mandelbrot.bin")
    
    root = tk.Tk()
    root.title("Fractal de Mandelbrot")

    canvas = Canvas(root, width=TAM_GRID, height=TAM_GRID)
    canvas.pack()
    img = PhotoImage(width=TAM_GRID, height=TAM_GRID)

    exibir_fractal(canvas, img, contador)

    root.mainloop()


if __name__ == '__main__':
    main()