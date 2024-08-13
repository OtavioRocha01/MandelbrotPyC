# Fractal de Mandelbrot

Uma implementação gráfica do Fractal de Mandelbrot que combina as linguagens Python e C.

**Autores:**
- Otavio Salomão Rocha ([seuemail@inf.ufpel.edu.br](mailto:seuemail@inf.ufpel.edu.br))
- Guilherme Hepp da Fonseca ([ghfonseca@inf.ufpel.edu.br](mailto:ghfonseca@inf.ufpel.edu.br))


## Repositório
Repositório composto pelos seguintes arquivos:
- **`main.py`**: Responsável pela interface e por gerar a imagem do fractal.
- **`mandelbrot.c`**: Responsável pelo cálculo do Fractal de Mandelbrot.
- **`Documentação.pdf`**: Documentação do código implementado.
- **Arquivos extras**: Arquivos de utilidade para o projeto.
  - **`.gitignore`**: Arquivo de configuração que especifica quais arquivos e diretórios devem ser ignorados pelo Git.
  - **`makefile`**: Arquivo de automação de compilação.
  - **`mandelbrot.h`**: Cabeçalhos e definições para a geração do fractal.
  - **`utils.h`/`utils.c`**: Arquivos com funções úteis para a execução dos cálculos necessários.

## Linux

### Requisitos
Antes de executar o projeto, é essencial garantir que os seguintes pacotes estejam instalados: gcc, make, python3, tkinter e pillow. Se algum desses pacotes ainda não estiver instalado, siga os comandos abaixo para realizá-lo:
```
sudo apt-get install gcc
sudo apt install make
sudo apt-get install python3.9
sudo apt install python3-tk
sudo apt install python3-pil
sudo apt install python3-pil.imagetk
```

### Execução
Para compilar e executar o projeto, você pode usar o Makefile fornecido:
```
make
```
Alternativamente, você pode compilar e executar manualmente com os seguintes comandos:
```
gcc -fPIC -shared -o raytracing.so raytracing.c utils.c
python3 interface.py
```

## Windows

### Requisitos
Antes de executar o projeto, é essencial garantir que os seguintes pacotes estejam instalados:
- **gcc:**
Para instalar o pacote gcc no Windows, recomendamos seguir o seguinte tutorial: [Como Instalar GCC/G++ MinGW no Windows](https://terminalroot.com.br/2022/12/como-instalar-gcc-gpp-mingw-no-windows.html)
- **python:**
Para instalar Python no Windows, recomendamos a seguinte página: [Python](https://www.python.org/downloads/windows/), **é importante que a versão mais recente do python seja instalada para evitar possíveis erros. Recomendamos versão >= 3.12.2**
- **tkinter:**
```
pip install tk
```
- **numpy:**
```
pip install numpy
```

### Execução utilizando variáveis padrões
Para compilar e executar o projeto, você pode usar o Makefile fornecido:
```
mingw32-make
```
Alternativamente, você pode compilar e executar manualmente com os seguintes comandos:
```
gcc -fPIC -shared -o mandelbrot.dll mandelbrot.c
python main.py
```

### Execução alterando o zoom da imagem
Para alterar o zoom da imagem resultante, alterar as seguintes variáveis na função inicializa() do arquivo mandelbrot.c,

De:
```
    M->x_ini = -2;
    M->y_ini = +2;
    M->passo = 4;
```
Para:
```
    M->x_ini = -0.3787675;
    M->y_ini = +0.6212361;
    M->passo = 5e-7;
```
Logo após seguir os mesmos passos da Execução padrão utilizando o Makefile ou compilar e executar manualmente.

