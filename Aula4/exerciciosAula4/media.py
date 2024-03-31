'''
2. Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.

'''

nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
calcula_media = (nota1 + nota2) / 2

if calcula_media >= 7 and calcula_media != 10:
    print(f'O aluno {nome} foi Aprovado, sua média foi {calcula_media}.')
elif calcula_media < 7:
    print(f'O aluno {nome} foi reprovado, sua média foi {calcula_media}')
elif calcula_media == 10:
    print(f'O aluno {nome} foi Aprovado com Distinção, sua média foi {calcula_media}')
else:
    print('Apenas números!')