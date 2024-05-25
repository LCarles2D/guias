#!/usr/bin/env python3

import sympy as sp

def Richardson(x_valor, ecuacion, h, nivel, finita, orden=None): # dinita es si se desea una diferncias hacia atras, central o hacia adelante, donde 1 es hacia adelante, 2 central, 3 atrase
    h_lista = [h/(2**(n)) for n in range(0,nivel)]
    D1 = [ diferencia_finita(x_valor,hi,ecuacion,finita) for hi in h_lista ]
    print(D1)

def diferencia_finita(x_valor,h,ecuacion,finita):
    x = sp.symbols("x")
    if finita == 1: #adelante
        return (ecuacion.subs(x, (x_valor+h)).evalf() - ecuacion.subs(x,x_valor).evalf())/h



x = sp.symbols("x")
Richardson(0.5, (0.10*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2), 0.1, 3, 1)

