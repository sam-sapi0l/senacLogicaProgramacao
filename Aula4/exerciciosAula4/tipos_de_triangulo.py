'''
11. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;

'''


lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))
lados = [lado1, lado2, lado3]
tipos_de_triangulo = ['Triângulo Equilátero: Possui os três lados iguais.', 'Triângulo Isósceles: quaisquer dos lados iguais.', 'Triângulo Escaleno: três lados diferentes.']

for lado in lados:
    if lado == lados[0] and lado == lados[1] and lado == lados[2]:
        print(tipos_de_triangulo[0])
    elif lado != lados[0] or lado != lados[1] or lado != lados[2]:
        print(tipos_de_triangulo[1])
    elif lado != lados:
        print(tipos_de_triangulo[2])
    else:
        print('Não foi possível identificar o triângulo.')