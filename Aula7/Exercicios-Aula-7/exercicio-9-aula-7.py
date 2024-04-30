'''
9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

'''
# incializando uma lista vazia
vetorA = []
vetorB = []
# controlador de numeros inseridos
contador = 0

# loop for para determinar numero de inputs necessarios
for numero in range(1, 11):
    try:
        numero = int(input('Digite um número: '))
        vetorA.append(numero)
        contador += 1
        print(f'Números Inseridos no Vetor: {contador} / 10')
    except:
        print('Entrada Inválida!')

# loop for para determinar raiz quadrada de cada número    
for n in vetorA:
    n *= n
    vetorB.append(n)    
   
print(f'Números Inseridos: {vetorA}')
print(f'Raiz Quadrada: {vetorB}')