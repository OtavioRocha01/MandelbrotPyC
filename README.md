# MandelbrotPyC
Para executar o arquivo C:

gcc mandelbrot.c -o mandelbrot -lm

Para alterar o zoom da função, alterar as seguintes variáveis no inicializa()
```
    M->x_ini = -0.3787675;
    M->y_ini = +0.6212361;
    M->passo = 5e-7;
```
Para
```
    M->x_ini = -2;
    M->y_ini = +2;
    M->passo = 4;
```
