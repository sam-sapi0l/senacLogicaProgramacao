'''

4. Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

'''

import re

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

maior_numero = max(num1, num2, num3)
menor_numero = min(num1, num2, num3)

if maior_numero == num1 and menor_numero == num2:
    print(f'O maior número é {num1} e o menor é {num2}')
elif maior_numero == num1 and menor_numero == num3:
    print(f'O maior número é {num1} e o menor é {num3}')
elif maior_numero == num2 and menor_numero == num1:
    print(f'O maior número é {num2} e o menor é {num1}')
elif maior_numero == num2 and menor_numero == num3:
    print(f'O maior número é {num2} e o menor é {num3}')
elif maior_numero == num3 and menor_numero == num1:
    print(f'O maior número é {num3} e o menor é {num1}')
elif maior_numero == num3 and menor_numero == num2:
    print(f'O maior número é {num3} e o menor é {num2}')
else:
    print('Resultado não encontrado!')