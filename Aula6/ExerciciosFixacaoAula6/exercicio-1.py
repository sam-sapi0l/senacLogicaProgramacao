# -*- coding: cp1252 -*-
'''
 Programa de Contagem com Loop For: Escreva um programa que solicite ao usuário um número e, em seguida, use um loop for para contar de 1 até esse número, exibindo cada número no processo.

'''

numero_usuario = int(input('Digite um número maior que [1]: '))
numero_usuario += 1

for i in range(1, numero_usuario):
    print(i)

