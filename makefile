# Nome do executável gerado
SO_NAME=mandelbrot.so

# Arquivos fonte
SOURCES=mandelbrot.c

# Detectando o sistema operacional
ifeq ($(OS),Windows_NT)
    PYTHON=python
else
    PYTHON=python3
endif

# Nome do script Python
PYTHON_SCRIPT=main.py

# Compilador e flags
CC=gcc
CFLAGS=-std=c99 -fPIC -shared -o -lm

# Alvo padrão
all: build run

# Alvo para compilar a DLL
build:
	$(CC) $(CFLAGS) $(SO_NAME) $(SOURCES)

# Alvo para executar o script Python
run:
	$(PYTHON) $(PYTHON_SCRIPT)