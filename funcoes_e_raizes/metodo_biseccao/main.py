# coding:utf-8

import metodos_raizes

# ENTRADA
funcao = raw_input()
x1 = raw_input()
x2 = raw_input()
qnt_vezes = int(raw_input())


# COMPUTAÇÃO
for i in range(qnt_vezes):
    xr = metodos_raizes.falsa_posicao(funcao, x1, x2)
    print xr

    if metodos_raizes.func(funcao, x1) * metodos_raizes.func(funcao, xr) > 0:
        x2 = str(xr)
    else:
        x1 = str(xr)


# SAÍDA
