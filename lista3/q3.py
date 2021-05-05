import time
from scipy.optimize import linprog as lp_solver
import numpy as np

# Min  Z =  25x_11 + 25x_12 + 25x_13 + 25x_14 + 25x_15
#          +26x_21 + 26x_22 + 26x_23 + 26x_24 + 26x_25
#          +24x_31 + 24x_32 + 24x_33 + 24x_34 + 24x_35
#          +23x_41 + 23x_42 + 23x_43 + 23x_44 + 23x_45
#          +28x_51 + 28x_52 + 28x_53 + 28x_54 + 28x_55
#          +30x_61 + 30x_62 + 30x_63 + 30x_64 + 30x_65
# s.a -1x_11 -1x_12 -1x_13 -1x_14 -1x_15 <= -8
#     -1x_21 -1x_22 -1x_23 -1x_24 -1x_25 <= -8
#     -1x_31 -1x_32 -1x_33 -1x_34 -1x_35 <= -8
#     -1x_41 -1x_42 -1x_43 -1x_44 -1x_45 <= -8
#     -1x_51 -1x_52 -1x_53 -1x_54 -1x_55 <= -7
#     -1x_61 -1x_62 -1x_63 -1x_64 -1x_65 <= -7
#      1x_11 +1x_21 +1x_31 +1x_41 +1x_51 +1x_61 = 14
#      1x_12 +1x_22 +1x_32 +1x_42 +1x_52 +1x_62 = 14
#      1x_13 +1x_23 +1x_33 +1x_43 +1x_53 +1x_63 = 14
#      1x_14 +1x_24 +1x_34 +1x_44 +1x_54 +1x_64 = 14
#      1x_15 +1x_25 +1x_35 +1x_45 +1x_55 +1x_65 = 14
#      0 <= x_11 <= 6
#           x_12  = 0
#      0 <= x_13 <= 6
#           x_14  = 0
#      0 <= x_15 <= 6
#           x_21  = 0
#      0 <= x_22 <= 6
#           x_23  = 0
#      0 <= x_24 <= 6
#           x_25  = 0
#      0 <= x_31 <= 4
#      0 <= x_32 <= 8
#      0 <= x_33 <= 4
#           x_34  = 0
#      0 <= x_35 <= 4
#      0 <= x_41 <= 5
#      0 <= x_42 <= 5
#      0 <= x_43 <= 5
#           x_44  = 0
#      0 <= x_45 <= 5
#      0 <= x_51 <= 3
#           x_52  = 0
#      0 <= x_53 <= 3
#      0 <= x_54 <= 8
#           x_55  = 0
#           x_61  = 0
#           x_62  = 0
#           x_63  = 0
#      0 <= x_64 <= 6
#      0 <= x_65 <= 2

c = [25]*5 + [26]*5 + [24]*5 + [23]*5 + [28]*5 + [30]*5
A_ub = [[-1]*5 + [0]*5 + [0]*5 + [0]*5 + [0]*5 + [0]*5,
        [0]*5 + [-1]*5 + [0]*5 + [0]*5 + [0]*5 + [0]*5,
        [0]*5 + [0]*5 + [-1]*5 + [0]*5 + [0]*5 + [0]*5,
        [0]*5 + [0]*5 + [0]*5 + [-1]*5 + [0]*5 + [0]*5,
        [0]*5 + [0]*5 + [0]*5 + [0]*5 + [-1]*5 + [0]*5,
        [0]*5 + [0]*5 + [0]*5 + [0]*5 + [0]*5 + [-1]*5]
b_ub = [-8, -8, -8, -8, -7, -7]
A_eq = [[1, 0, 0, 0, 0]*6,
        [0, 1, 0, 0, 0]*6,
        [0, 0, 1, 0, 0]*6,
        [0, 0, 0, 1, 0]*6,
        [0, 0, 0, 0, 1]*6]
b_eq = [14, 14, 14, 14, 14]
x11_bounds = (0, 6)
x12_bounds = (0, 0)
x13_bounds = (0, 6)
x14_bounds = (0, 0)
x15_bounds = (0, 6)
x21_bounds = (0, 0)
x22_bounds = (0, 6)
x23_bounds = (0, 0)
x24_bounds = (0, 6)
x25_bounds = (0, 0)
x31_bounds = (0, 4)
x32_bounds = (0, 8)
x33_bounds = (0, 4)
x34_bounds = (0, 0)
x35_bounds = (0, 4)
x41_bounds = (0, 5)
x42_bounds = (0, 5)
x43_bounds = (0, 5)
x44_bounds = (0, 0)
x45_bounds = (0, 5)
x51_bounds = (0, 3)
x52_bounds = (0, 0)
x53_bounds = (0, 3)
x54_bounds = (0, 8)
x55_bounds = (0, 0)
x61_bounds = (0, 0)
x62_bounds = (0, 0)
x63_bounds = (0, 0)
x64_bounds = (0, 6)
x65_bounds = (0, 2)
bounds = [x11_bounds, x12_bounds, x13_bounds, x14_bounds, x15_bounds,
          x21_bounds, x22_bounds, x23_bounds, x24_bounds, x25_bounds,
          x31_bounds, x32_bounds, x33_bounds, x34_bounds, x35_bounds,
          x41_bounds, x42_bounds, x43_bounds, x44_bounds, x45_bounds,
          x51_bounds, x52_bounds, x53_bounds, x54_bounds, x55_bounds,
          x61_bounds, x62_bounds, x63_bounds, x64_bounds, x65_bounds]

res = lp_solver(c=c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
print(res)
print("")
print("Result:", res.fun)
print("X:     \n", np.reshape(res.x, [6, 5]))
print("")

tempos = []
for _ in range(100):
    inicio = time.process_time()
    lp_solver(c=c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
    tempos += [time.process_time() - inicio]
print("Tempo de execução:", np.mean(tempos), "+-", np.std(tempos), "segundos")
