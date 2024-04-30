'''

7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

'''

# criando lista vazia
lista_numeros = []

# controlador de elementos
contador = 0

for n in range(1, 6):
    try:
        numero = int(input('Digite um número inteiro: '))
    except:
        print('Apenas números inteiros!')
    
    lista_numeros.append(numero)
    contador += 1
    print(f'Números inseridos: {contador} / 5')

soma = 0
for s in lista_numeros:
    soma += s
multiplica = 1
for m in lista_numeros:
    multiplica *= m 
        
print(f'Lista com total de elementos: {lista_numeros}')
print(f'Lista somada: {soma}')
print(f'Lista Multiplicada: {multiplica}')

