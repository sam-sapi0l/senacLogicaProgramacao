'''
4. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

'''

lista = []
nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))
nota3 = float(input('Digite a 3° nota: '))
nota4 = float(input('Digite a 4° nota: '))

lista.append(nota1)
lista.append(nota2)
lista.append(nota3)
lista.append(nota4)

soma = lista[0] + lista[1] + lista[2] + lista[3]

print(lista)
print()
print(soma)