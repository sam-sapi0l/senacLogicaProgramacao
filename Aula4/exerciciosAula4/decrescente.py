'''

5. Faça um Programa que leia três números e mostre-os em ordem decrescente.

'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

lista = [num1, num2, num3]
lista.sort(reverse=True)

print(lista)