'''
4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

'''
# lista vazia
lista = []

# lista de vogais
vogal = ['a', 'e', 'i', 'o', 'u']

# delimitador de caracteres a serem inseridos
contador = 0

while  contador < 10:
    while True:
        try:
            char = input('Digite um caracter: ')
        except:
            print('Apenas caracteres!')   
            
        lista.append(char)
        print(lista)      
        contador += 1
        print(f'Caracteres inseridos: {contador} / 10')
        
        if contador == 10:
           print(lista)
           quantidade = 0
           for i in lista:
                if i not in vogal:
                    quantidade += 1
                    print(f'Consoantes:{i}', end=' ')
                elif i in vogal:
                    print(f'Vogais: {i}')
                else:
                    print('Erro!')
        else:
            print('Erro ao imprimir letras!')                     
        break
    else:
        print('FIM DO WHILE')
else:
    print(f'Quantidade de Consoantes: {quantidade}')
    print('PROGRAMA ENCERRADO')


