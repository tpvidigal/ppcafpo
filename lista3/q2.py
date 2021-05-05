from scipy.optimize import linprog as lp_solver

# Min  Z = 600x_1 + 800x_2 + 700x_3 + 400x_4 + 900x_5 + 600x_6
# s.a  1x_1 + 0x_2 + 0x_3 + 1x_4 + 0x_5 + 0x_6 = 300
#      0x_1 + 1x_2 + 0x_3 + 0x_4 + 1x_5 + 0x_6 = 200
#      0x_1 + 0x_2 + 1x_3 + 0x_4 + 0x_5 + 1x_6 = 400
#      1x_1 + 1x_2 + 1x_3 + 0x_4 + 0x_5 + 0x_6 = 400
#      0x_1 + 0x_2 + 0x_3 + 1x_4 + 1x_5 + 1x_6 = 500

c = [600, 800, 700, 400, 900, 600]
A_eq = [[1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1]]
b_eq = [300, 200, 400, 400, 500]

res = lp_solver(c=c, A_eq=A_eq, b_eq=b_eq)
print(res)
print("")
print("Result:", res.fun)
print("X:     ", res.x)
