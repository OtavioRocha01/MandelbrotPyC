# Arquivos fonte
SOURCES=mandelbrot.c

# Detectando o sistema operacional
ifeq ($(OS),Windows_NT)
	SO_NAME=mandelbrot.dll
    PYTHON=python
else
	SO_NAME=mandelbrot.so
    PYTHON=python3
endif

# Nome do script Python
PYTHON_SCRIPT=main.py

# Compilador e flags
CC=gcc
CFLAGS=-fPIC -shared -o

# Alvo padrão
all: build run

# Alvo para compilar a DLL
build:
	$(CC) $(CFLAGS) $(SO_NAME) $(SOURCES)

# Alvo para executar o script Python
run:
	$(PYTHON) $(PYTHON_SCRIPT)