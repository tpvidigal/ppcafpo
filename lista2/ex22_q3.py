# Problema
# max Z = 2*x_1 + 6*x_2
# s.a.
# 4*x_1 + 3*x_2 <= 12
# 2*x_1 + 1*x_2 <= 8
# x_1, x_2 >= 0

# Dicionário de equações
# Z   =  0 +2*x_1 +6*x_2
# x_3 = 12 -4*x_1 -3*x_2
# x_4 =  8 -2*x_1 -1*x_2
# x_1, x_2, x_3, x_4 >= 0
#
# Variáveis basicas:     Z, x_3, x_4
# Variáveis não-basicas: x_1, x_2
# Maior incremento de Z: x_2

# Maximizando variavel-basica de x_2
# x_2 >= 0
# x_3 = 12 -3*x_2 >= 0  ->  x_2 <= 4
# x_4 =  8 -1*x_2 >= 0  ->  x_2 <= 8
#
# Soluções viáveis:     0 <= x_2 <= 4
# Maior valor positivo: 4
# Maior restrição:      x_3 = 12 -3*x_2

# Atualizando dicionário por x_2
# Maior restrição da variavel: x_3 = 12 -4*x_1 -3*x_2
# Adaptando a restrição:       x_2 = 4 -4/3*x_1 -1/3*x_3
#
# Z   = 24   -6*x_1   -2*x_3
# x_2 =  4 -4/3*x_1 -1/3*x_3
# x_4 =  4 -2/3*x_1 +1/3*x_3
# x_1, x_2, x_3, x_4 >= 0
#
# Variáveis basicas:     Z, x_2, x_4
# Variáveis não-basicas: x_1, x_3
# Maior incremento de Z: Nenhum (todos os coeficientes são negativos)

# Solução ótima: variáveis não-basicas = 0
# Z   = 24
# x_1 =  0
# x_2 =  4
# x_3 =  0
# x_4 =  4
