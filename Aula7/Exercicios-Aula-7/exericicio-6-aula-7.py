'''
6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

'''
from itertools import count


# inicializando lista vazia
lista_aprovado = []
lista_reprovado = []

# controlador de alunos
contador = 0

while True:
    while contador < 10:
        try:
            nota1 = float(input('Digite sua 1° nota: '))
            nota2 = float(input('Digite sua 2° nota: '))
            nota3 = float(input('Digite sua 3° nota: '))
            nota4 = float(input('Digite sua 4° nota: '))
        except:
           print('Apenas números!')         
        
        media = (nota1 + nota2 + nota3 + nota4) / 4
            
        if media >= 7:
            lista_aprovado.append(media)
            contador += 1
            print(f'Alunos Aprovados: {lista_aprovado}')
            print(f'Alunos: {contador} / 3')
        else:
            lista_reprovado.append(media)
            contador += 1
            print(f'Alunos: {contador} / 3')
            print(f'Alunos Reprovados: {lista_reprovado}')
        
        if contador == 10:
               print('Números de alunos necessários já satisfeito!')
               break
    
    else:
        print('FIM DO WHILE')

    if media <= 7:
        print(f'Número de alunos com média maior ou igual a 7: {len(lista_aprovado)}')
        print(f'Maior média: {max(lista_aprovado)}')
    break
else:
    print('FIM DO SEGUNDO WHILE')
print('PROGRAMA ENCERRADO')