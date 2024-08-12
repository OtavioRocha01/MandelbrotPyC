from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension

ext_modules = [
    Extension(
        "mandelbrot",
        sources=["mandelbrot.pyx", "mandelbrot.c"],
    )
]

setup(
    ext_modules=cythonize(ext_modules),
)
