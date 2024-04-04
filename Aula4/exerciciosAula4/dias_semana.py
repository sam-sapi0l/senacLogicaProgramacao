'''

9. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

'''


dia_digitado = int(input('Digite um número de [1-7]: '))
dia = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']


if dia_digitado == 1:
    print(f'{dia[0]}')
elif dia_digitado == 2:
    print(f'{dia[1]}')
elif dia_digitado == 3:
    print(f'{dia[2]}')
elif dia_digitado == 4:
    print(f'{dia[3]}')
elif dia_digitado == 5:
    print(f'{dia[4]}')
elif dia_digitado == 6:
    print(f'{dia[5]}')
elif dia_digitado == 7:
    print(f'{dia[6]}')
else:
    print('Valor inválido!')       
