# -*- coding: cp1252 -*-
'''
 Programa de Contagem com Loop For: Escreva um programa que solicite ao usu�rio um n�mero e, em seguida, use um loop for para contar de 1 at� esse n�mero, exibindo cada n�mero no processo.

'''

numero_usuario = int(input('Digite um n�mero maior que [1]: '))
numero_usuario += 1

for i in range(1, numero_usuario):
    print(i)

