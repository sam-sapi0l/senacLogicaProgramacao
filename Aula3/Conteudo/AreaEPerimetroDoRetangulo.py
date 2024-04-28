"""
Exemplo 2

Faça um programa que recebe a base e a altura de um retângulo, calcular a
sua área e seu perímetro.

"""

base = float(input("Digite a base do Retângulo: "))
altura = float(input("Digite a altura do Retângulo: "))
area = base * altura / 2
perimetro = 2 * (base + altura)

print(f"A área do Retângulo com os valores informados é: {area}")
print(f"O perímetro do Retângulo com os valores informados é: {perimetro}")
