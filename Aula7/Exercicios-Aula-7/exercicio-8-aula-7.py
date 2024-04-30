'''
8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

'''


# criando listas vazias
lista_altura = []
lista_idade = []

# controlador de números de pessoas
controlador = 0

while controlador < 5:
    while True:
        try:
            idade = int(input('Digite sua idade: '))
            altura = float(input('Digite sua altura: '))
        except:
            print('Entrada Inválida!')
        
        controlador += 1
        
        lista_altura.append(altura)
        lista_idade.append(idade)
        
        print(f'Lista contendo altura: {lista_altura}')
        print(f'Lista contendo idade: {lista_idade}')
        
        if controlador == 5:
            lista_altura.sort(reverse=True)
            lista_idade.sort(reverse=True)
            print(f'Lista contendo altura ordem descrescente: {lista_altura}')
            print(f'Lista contendo idade decrescente: {lista_idade}')
            print('ENCERRANDO PROGRAMA')
            break
        elif controlador < 5:
            continue
        else:
            print('PROBLEMA AO FINALIZAR CONTROLADOR')
    else:
        print('FIM DO WHILE')
else:
    print('FIM DO PROGRAMA')