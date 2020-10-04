def calcula_f(x):
    return x**3 + 5 * x ** 2 - 5 * x - 12

iteracao_maxima = 100
iteracao = 0 
erro_definido = 0.0001
parar = 0

a = -6.0
b = -4.0

y1 = calcula_f(a)
y2 = calcula_f(b)

x0_anterior =  2 * b

if y1 * y2 > 0:
    print('erro de execucao - redefinir valores de a e b')
else:
    while parar == 0:
        print('no loop')
        iteracao = iteracao + 1
        x0 = (a + b)/2 
        y0 = calcula_f(x0)

        if y1 * y0 > 0:
            a = x0

        if y2 * y0 > 0:
            b = x0

        erro = abs(x0 - x0_anterior)

        x0_anterior = x0 

        if (iteracao > iteracao_maxima) or (erro > erro_definido):
            parar = 1

print('\ntotal de iteração', iteracao)
print('\nvalor de x = ', x0)
print('\nErro encontrado, erro = ', erro, '\n')

