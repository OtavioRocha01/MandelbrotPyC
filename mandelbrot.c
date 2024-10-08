#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>

#define TAM_GRID 500
#define MAX_ITER 400
#define TAM_BLOCO (2.0 / TAM_GRID)
#define MAT2X(j) ((j) * (TAM_BLOCO) - 1.0)
#define MAT2Y(i) (1.0 - (i) * (TAM_BLOCO))


// Estrutura que representa o conjunto de Mandelbrot
typedef struct mandelbrot_set{
    double x_ini;
    double y_ini;
    double passo;
    double incr;
    int contador[TAM_GRID][TAM_GRID];
    int menor, maior;
    int cor, coord;
}MANDELBROT;

// Inicializa a estrutura do conjunto de Mandelbrot
MANDELBROT* inicializa() {
    MANDELBROT* M = (MANDELBROT*) malloc(sizeof(MANDELBROT));
    if ( M != NULL ) {
        M->cor = 0;
        M->coord = 1;
        M->x_ini = -2;
        M->y_ini = +2;
        M->passo = 4;
        M->incr = M->passo / TAM_GRID;
    }

    return M;
}

// Calcula o conjunto de Mandelbrot
void calcula(MANDELBROT* M) {
    int x, y, iter;
    double py, px;
    double complex z0, z;
    py = M->y_ini;

    for ( y = 0 ; y < TAM_GRID ; y++ ) {
        px = M->x_ini;
        for ( x = 0 ; x < TAM_GRID ; x++ ) {
            M->contador[y][x] = 0;
            z0 = px + py * I;
            z = z0;
            for ( iter = 0 ; iter < MAX_ITER ; iter++ ) {
                z = z * z + z0;
                if ( cabs(z) > 2.0 ) {M->contador[y][x]++; break;}
            }
            px += M->incr;
        }
        py -= M->incr;
    }
    
    M->menor = M->maior = M->contador[0][0];
    for ( y = 0 ; y < TAM_GRID ; y++ ) {
        for ( x = 0 ; x < TAM_GRID ; x++ ) {
            if ( M->contador[y][x] < M->menor ) {M->menor = M->contador[y][x];}
            if ( M->contador[y][x] > M->maior ) {M->maior = M->contador[y][x];}
        }
    }
}