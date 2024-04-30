'''
11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

'''
# inicializando listas vazias
vetorA = []
vetorB = []
vetorC = []
vetorD = []
# controlador de elementos
controlador = 0

while True:
    while controlador < 10:
        try:
            elementoVetorA = int(input('Digite um elemento a inserir no Vetor A: '))
            elementoVetorB = int(input('Digite outro elemento a inserir no Vetor B: '))
            elementoVetorC = int(input('Digite outro elemento a inserir no Vetor C: '))            
        except:
            print('Entrada Inválida!')
        if elementoVetorA not in vetorA and elementoVetorB not in vetorB and elementoVetorC not in vetorC:    
            vetorA.append(elementoVetorA)
            vetorB.append(elementoVetorB)
            vetorC.append(elementoVetorC)
            
            vetorA.sort()
            vetorB.sort()
            vetorC.sort()
            
            print(f'Vetor A: {vetorA}')
            print(f'Vetor B: {vetorB}')
            print(f'Vetor C: {vetorC}')
            
            controlador += 1
            print(f'Números inseridos em cada lista: {controlador} / 10')
        else:
            print('Elemento já inserido!')
        
        if controlador == 10:
            for elemento in vetorA:
                if elemento in vetorB and elemento in vetorC:
                    vetorD.append(elemento)    
                    vetorD.sort()
                elif elemento not in vetorB and vetorC:
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
        print(f'Vetor D: {vetorD}')
        print('FIM DO WHILE')
        break
else:
    print('PROGRAMA ENCERRADO')
