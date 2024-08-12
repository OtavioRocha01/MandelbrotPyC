cdef extern from "mandelbrot.c":
    ctypedef struct MANDELBROT:
        pass

    MANDELBROT* inicializa()
    void calcula(MANDELBROT* M)

cdef class MandelbrotSet:
    cdef MANDELBROT* m

    def __cinit__(self):
        self.m = inicializa()

    def calculate(self):
        calcula(self.m)

    def get_data(self):
        return [[self.m.contador[y][x] for x in range(500)] for y in range(500)]
