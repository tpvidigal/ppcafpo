# Boneco: 27 reais

# Matéria-Prima: 10 reais
# Mão de Obra: 13 reais

# Trem: 21 reais

# Máreia-Prima: 9 reais
# Mão de obra: 10 reais

# --- Manufatura ---
# Boneco acabamento: 2h
# Boneco carpintaria: 1h


# Trem acabamento: 1h
# Trem carpintaria: 1h

# acabamento: 100h
# carpintaria: 80h

# trens demanda: ilimitada
# bonecos demanda: ≤40

# f(x) = x1 + y1 (boneco e trem)
# f(x) = 4x + 2y  (A1) (lucro boneco e trem)

# 2x + y ≤ 100    (A2) (restrição acabamento)
# x + y ≤ 80      (A3) (restrição carpintaria)
# x ≤ 40          (A4) (restrição unidades bonecos)

# Import the necessary packages and modules
import matplotlib.pyplot as plt

print("2.A=> Gráficos")

x1 = [50, 0]
y1 = [0, 100]

plt.plot(x1, y1, label = "Restrição Horas Acabamento")

x2 = [80, 0]
y2 = [0, 80]

plt.plot(x2, y2, label = "Restrição Horas Carpintaria")

x3 = [40, 40]
y3 = [0, 100]

plt.plot(x3, y3, label = "Restrição Unidades Bonecos")


#f(x) = 4x + 2y  (A1)

result1 = 4*(20) + 2*(60)
result2 = 4*(30) + 2*(40)
result3 = 4*(40) + 2*(20)
result4 = 4*(40) + 2*(0)

print("2.B")

print(result1)
print(result2)
print(result3)
print(result4)

print("2.C")

#f(x) = -1 * (5x + 3y)  (A1)
result1 = 5*(20) + 3*(60)
result2 = 5*(30) + 3*(40)
result3 = 5*(40) + 3*(20)
result4 = 5*(40) + 3*(0)


print(result1)
print(result2)
print(result3)
print(result4)



plt.grid()
plt.show()


