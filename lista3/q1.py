from scipy.optimize import linprog as lp_solver

# Maquina       Dispon Prod1 Prod2 Prod3
# fresadora        500     9     3     5
# torno            350     5     4     0
# retificadora     150     3     0     2
#
# Potencial vendas       inf   inf    20
# Lucro por unidade       50    20    25

# Max  Z = 50x_1 + 20x_2 + 25x_3
# s.a  9x_1 + 3x_2 + 5x_3 <= 500
#      5x_1 + 4x_2 + 0x_3 <= 350
#      3x_1 + 0x_2 + 2x_3 <= 150
#                     x_3 <=  20

# Min  -Z = -50x_1 -20x_2 -25x_3
# s.a  9x_1 +3x_2 +5x_3 <= 500
#      5x_1 +4x_2 +0x_3 <= 350
#      3x_1 +0x_2 +2x_3 <= 150
#      0 <= x_1
#      0 <= x_2
#      0 <= x_3 <= 20

c = [-50, -20, -25]
A_ub = [[9, 3, 5],
        [5, 4, 0],
        [3, 0, 2]]
b_ub = [500, 350, 150]
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, 20)
bounds = [x1_bounds, x2_bounds, x3_bounds]

res = lp_solver(c=c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(res)
print("")
print("Result:", -res.fun)
print("X:     ", res.x)
