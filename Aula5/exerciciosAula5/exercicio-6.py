'''
6. Média de uma Lista:
Modifique o programa anterior para calcular a média aritmética dos elementos de uma lista.

'''

lista = []

for var_numero in range(1, 11):
    numeros = float(input('Digite um número: '))
    lista.append(numeros)
    print(lista)
    for numero in lista:
        soma = sum(lista)
        soma_itens = numero + numeros
        media = soma / 2
print(soma)
print(f'A soma dos elementos é: {soma}')
print(f'A média é: {media}')
#media = soma / 2
#print(soma)
#print(media)
       
        

