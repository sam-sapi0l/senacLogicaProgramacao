'''
10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

'''

# inicializando listas vazias
vetorA = []
vetorB = []
vetorC = []

# controlador de elementos
controlador = 0

while True:
    while controlador < 10:
        try:
            elementoVetorA = int(input('Digite um elemento a inserir no Vetor A: '))
            elementoVetorB = int(input('Digite outro elemento a inserir no Vetor B: '))
        except:
            print('Entrada Inválida!')
        if elementoVetorA not in vetorA and elementoVetorB not in vetorB:    
            vetorA.append(elementoVetorA)
            vetorB.append(elementoVetorB)
            vetorA.sort()
            vetorB.sort()
            print(f'Vetor A: {vetorA}')
            print(f'Vetor B: {vetorB}')
            controlador += 1
            print(f'Números inseridos em cada lista: {controlador} / 10')
        else:
            print('Elemento já inserido!')
        
        if controlador == 10:
            for elemento in vetorA:
                if elemento in vetorB:
                    vetorC.append(elemento)    
                    vetorC.sort()
                elif elemento not in vetorB:
                    continue
                else:    
                    print('Erro ao iterar sobre elemento!')    
        elif controlador != 10:
            continue
        else:
            print('Erro ao comparar!')
    else:
        print(f'Vetor A: {vetorA}')
        print(f'Vetor B: {vetorB}')
        print(f'Vetor C: {vetorC}')
        print('FIM DO WHILE')
        break
else:
    print('PROGRAMA ENCERRADO')