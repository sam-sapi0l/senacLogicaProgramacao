'''
5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

'''

# listas vazias para cada numero impar, par e uma lista para cada numero digitado
lista_par = []
lista_impar = []
lista_numeros_digitados = []

# controlador de tentativas
contador = 0

# loop for para ler o input im determinado número de vezes
for numero_digitado in range(1, 21):
    while True:
        try:
            numero_digitado = int(input('Digite um número inteiro: '))
            if numero_digitado % 2 != 0 and numero_digitado not in lista_numeros_digitados:
                contador += 1
                print(f'Números inseridos: {contador} / 20')
                print('Ímpar!')
                lista_impar.append(numero_digitado)
                lista_numeros_digitados.append(numero_digitado)
                print(lista_impar)
            elif numero_digitado % 2 == 0 and numero_digitado not in lista_numeros_digitados:
                contador += 1
                print(f'Números inseridos: {contador} / 20')
                print('Par!')
                lista_par.append(numero_digitado)
                lista_numeros_digitados.append(numero_digitado)
                print(lista_par)
            else:
                print('Número já inserido!')
            
            if contador == 20:
                print('Total de números já inserido!')
            break

        except:
            print('Entrada Inválida!') 
    else:
        print('FIM DO WHILE')      

# imprime listas contendo números ímpares, pares e todos inseridos
print('\n\n')        
print('Números inseridos: ')
print(sorted(lista_numeros_digitados))
print()
print('Lista com números pares: ')        
print(sorted(lista_par))
print()
print('Lista com números ímpares: ')
print(sorted(lista_impar))
print('PROGRAMA ENCERRADO')

