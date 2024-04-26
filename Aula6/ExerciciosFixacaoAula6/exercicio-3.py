'''
Programa de Tabuada com Loop For: Faça um programa que peça ao usuário um número e, em seguida, use um loop for para exibir a tabuada desse número, de 1 a 10.

'''

numero = int(input('Digite um número: '))
for i in range(1, 11):
    tabuada = i * numero
    print(tabuada)