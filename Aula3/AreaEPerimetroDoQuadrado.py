"""
Exercício 1

Faça um programa que recebe o lado de um quadrado, calcular a área e o
perímetro do mesmo.

"""
lado = float(input("Digite o valor dos lados do Quadrado: "))
base = float(input("Digite o valor da base do Quadrado: "))
altura = float(input("Digite o valor da altura do Quadrado: "))


area = base * altura / 2
perimetro = lado * 4

print(f"A área do Quadrado com os valores informados é:{area}")
print(f"o perímetro do Quadrado com os valores informados é:{perimetro}")

