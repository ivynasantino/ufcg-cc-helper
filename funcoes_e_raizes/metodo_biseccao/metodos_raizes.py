def func(f, x):
    funcao = ''
    for l in f:
        if l == 'x':
            funcao += str(x)
        else:
            funcao += str(l)

    return eval(funcao)



def bissecao(funcao, valor01, valor02):
    xc = (valor01 + valor02) / 2.0
    

    pass


# FALSA_POSICAO: FORMULA E ATUALIZACAO POR Xr
def falsa_posicao(f, x1, x2):
    float_x1 = float(x1)
    float_x2 = float(x2)
    formula = float_x2 - ((func(f, x2)*(float_x1-float_x2)) / (func(f, x1) - func(f, x2)))
    
    return formula


# SECANTE: FORMULA E ATUALIZACAO POR Xr
def secante(funcao, valor01, valor02):
    
    
    pass


# SECANTE_MODIFICADO: FORMULA E ITERACOES SOBRE Xr
def secante_modificado(funcao, valor, delta):
    xr = valor
    
    pass




