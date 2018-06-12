def analisa_funcao(funcao, valor):
    string_aux = ''

    for e in funcao:
        if e == 'x':
            string_aux += valor
        else:
            string_aux += e

    return eval(string_aux)


def metodo_insercao(funcao, x1, x2, qnt_vezes):
    lista_raizes = []

    f_x1 = analisa_funcao(funcao, x1)
    if f_x1 == 0:
        lista_raizes.append(f_x1)

    f_x2 = analisa_funcao(funcao, x2)
    if f_x2 == 0:
        lista_raizes.append(f_x2)


    flag = False
    for i in xrange(qnt_vezes):
        xc = (float(x1) + float(x2)) / 2.0
        f_xc = analisa_funcao(funcao, str(xc))
        if f_xc == 0:
            lista_raizes.append(xc)
            flag = True
            break

        elif f_x1 * f_xc > 0:
            x1 = xc

        elif f_x1 * f_xc < 0:
            x2 = xc

    if not flag:
        lista_raizes.append(float('%.2f' % xc))

    return lista_raizes


funcao = raw_input()
x1 = raw_input()
x2 = raw_input()
qnt_vezes = int(raw_input())

print metodo_insercao(funcao,x1,x2,qnt_vezes)
