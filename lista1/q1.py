#TRABALHO FPO
#Q1
#pip insall matplotlib

#natação
#Custo: R$3,00
#Horas: 2h
#Calorias: 1.500
#
#ciclismo
#Custo: R$2,00
#Horas: 2h
#Calorias: 1.000
#
#orçamento
#Valor: R$70,00
#Tempo: 18 horas
#Calorias: 80.000

#variáveis de decisão
#x1 -> qtd de sessões de treinamento de natação
#x2 -> qtd de sessões de treinamento de ciclismo

# f(x) = x1 + x2

#restrições
#3x1 + 2y1 <= 70
#1500x2 + 1000y2 <= 80.000
#2x3 + 2y3 <= 18
#x1, x2 >= 1 ( obrigatoriamente tem de ter um de cada)

#=>  x1 = (70-2y1)/3

# Import the necessary packages and modules
import matplotlib.pyplot as plt

#restrição orçamentária

x1 = [-22.33, 0]
y1 = [0, -35]

plt.plot(x1, y1, label = "Restrição orçamentária")

#restrição calórica
x2 = [-53.33, 0]
y2 = [0, -80]

plt.plot(x2, y2, label = "Restrição calórica")

#restrição temporal
x3 = [-9, 0]
y3 = [0, -9]

plt.plot(x3, y3, label = "Restrição temporal")

x4 = [-1, -1]
y4 = [0, -80]

plt.plot(x4, y4, label = "Restrição pelo menos uma modalidade")

plt.show();