import matplotlib.pyplot as plt
import numpy as np

"""
Letra b: Enunciado padrão
"""

# Restrição 1
x_1 = np.linspace(0, 10, 11)
x_2 = np.linspace(10, 0, 11)
plt.plot(x_1, x_2, label=r"$x_1 + x_2 \leq 10$")
plt.fill_between(x_1, x_2, [0]*11, alpha=0.2)

# Restrição 2
x_1 = np.linspace(0, 6, 7)
x_2 = [(12 - 2*x) / 3 for x in x_1]
plt.plot(x_1, x_2, 'g', label=r"$20x_1 + 30x_2 \leq 120$")
plt.fill_between(x_1, x_2, [0]*7, color='g', alpha=0.2)

# Restrição 3
plt.plot([1,1], [0,10], 'r', label=r"$x_1 \geq 1$")
plt.fill_betweenx([0,10], [1,1], [10,10], color='r', alpha=0.1)

# Restrição 4
plt.plot([0,10], [3,3], 'y', label=r"$x_2 \geq 3$")
plt.fill_between([0,10], [3,3], [10,10], color='y', alpha=0.2)

plt.title("Pequeno produtor: Espaço de soluções")
plt.xlabel(r"$x_1$")
plt.ylabel(r"$x_2$")
plt.xticks(np.linspace(0, 10, 11))
plt.yticks(np.linspace(0, 10, 11))
plt.grid()
plt.legend()
plt.show()


"""
Letra d: Remoção de restrição excedente
"""

# Restrição 2
x_1 = np.linspace(0, 6, 7)
x_2 = [(12 - 2*x) / 3 for x in x_1]
plt.plot(x_1, x_2, 'g', label=r"$20x_1 + 30x_2 \leq 120$")
plt.fill_between(x_1, x_2, [0]*7, color='g', alpha=0.2)

# Restrição 3
plt.plot([1,1], [0,10], 'r', label=r"$x_1 \geq 1$")
plt.fill_betweenx([0,10], [1,1], [10,10], color='r', alpha=0.1)

# Restrição 4
plt.plot([0,10], [3,3], 'y', label=r"$x_2 \geq 3$")
plt.fill_between([0,10], [3,3], [10,10], color='y', alpha=0.2)

plt.title("Pequeno produtor: Espaço de soluções (sem restrição 1)")
plt.xlabel(r"$x_1$")
plt.ylabel(r"$x_2$")
plt.xticks(np.linspace(0, 10, 11))
plt.yticks(np.linspace(0, 10, 11))
plt.grid()
plt.legend()
plt.show()