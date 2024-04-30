"""
Exercicio 4


Faça os programas individuais para calcular os perímetros e as áreas das figuras
geométricas abaixo. Alguns programas precisarão de vários valores de entrada. 


"""
import math

forma = int(input("Digite a forma geométrica que deseja calcular [1]Acutângulo [2]Quadrado [3]Retângulo [4]Paralelograma [5]Losângulo [6]Escaleno [7]Círculo: "))


if forma == 1:
    a = float(input("Digite o valor do lado A:"))
    b = float(input("Digite o valor do lado B:"))
    c = float(input("Digite o valor do lado C:"))
    base = float(input("Digite o valor da base:"))
    altura = float(input("Digite o valor da altura:"))
    perim = a + b + c
    area = base * altura / 2
    print(f"O perímetro do Acutângulo é {perim} e sua área é {area}")
elif forma == 2:
    valor = float(input("Digite o valor dos lados do Quadrado: "))
    area = valor * valor
    perim = valor * 4
    print(f"A área do Quadrado é {area} e seu perímetro é {perim}")
elif forma == 3:
    a = float(input("Digite o valor do 1A: "))
    b = float(input("Digite o valor de 1B: "))
    area = a - b
    perim = (a * 2) + (b * 2)
    print(f"O valor da área do Retângulo é {area} e seu perímetro é {perim}")
elif forma == 4:
    base = float(input("Digite o valor da base do Paralelograma: "))
    altura = float(input("Digite a altura do Paralelograma: "))
    a = float(input("Digite o valor do lado A: "))
    b = float(input("Digite o valor do lado B: "))
    area = base * altura
    perim = (a * 2) + (b * 2)
    print(f"O valor da área do Paralelograma é {area} e seu perímetro é {perim}")
elif forma == 5:
    l = float(input("Digite o valor do lado do losângulo: "))
    diagonal_maior = float(input("Digite o valor da Diagonal Maior do Losângulo: "))
    diagonal_menor = float(input("Digite o valor da Diagonal Menor do Losângulo: "))
    area = (diagonal_maior * diagonal_menor) / 2
    perim = l * 4
    print(f"O valor da área do losângulo é {area} e seu perímetro é {perim}")
elif forma == 6:
    a = float(input("Digite o valor do lado A do Triângulo Escaleno: "))
    b = float(input("Digite o valor do lado B do Triângulo Escaleno: "))
    c = float(input("Digite o valor do lado C do Triângulo Escaleno: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perim = a + b + c
    print(f"A área do Triângulo Escaleno com os valores informados é {area} e seu perímetro é {perim}")
elif forma == 7:
    r = float(input("Digite o valor do Raio do Círculo: "))
    c = float(input("Digite o valor da Circunferencia do Círculo: "))
    raio = r * 2
    area = math.pi * raio ** 2
    print(f"O raio do círculo com valor informado é {raio} e sua área é {area}")