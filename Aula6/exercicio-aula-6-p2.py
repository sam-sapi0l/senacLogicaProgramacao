'''

Faça um programa que (FUPQ) lê um número não determinado de nomes de alunos e 
suas duas notas, calcular sua média aritmética e informar se >= 7 APROVADO senão REPROVADO TERMINAR o Programa quando nome == fim

'''

lista = []
nome = input('Digite o nome do aluno: ')
lista.append(nome)
print(lista)
nota = float(input('Digite sua nota 1: '))
lista.append(nota)
print(lista)
nota2 = float(input('Digite sua nota 2: '))
lista.append(nota2)
print(lista)
media = (nota + nota2) / 2
contador = 1
while contador <= 3: 
    if media >= 7:
        print(f'Nome do aluno: {lista[0]}')
        print(f'Primeira nota do aluno: {lista[1]}')
        print(f'Segunda nota do aluno: {lista[2]}')
        print(f'Média: {media}')
        print(f'APROVADO')
        break
    elif media < 7:
        print(f'Nome do aluno: {lista[0]}')
        print(f'Primeira nota do aluno: {lista[1]}')
        print(f'Segunda nota do aluno: {lista[2]}')
        print(f'Média: {media}')
        print(f'REPROVADO')
        contador += 1
        print(f'Tentativas: {contador} / 3')

        lista = []
        nome = input('Digite o nome do aluno: ')
        lista.append(nome)
        print(lista)
        nota = float(input('Digite sua nota 1: '))
        lista.append(nota)
        print(lista)
        nota2 = float(input('Digite sua nota 2: '))
        lista.append(nota2)
        print(lista)
        media = (nota + nota2) / 2
    else:
        print('Inválido!')
else:
    print('FIM!')