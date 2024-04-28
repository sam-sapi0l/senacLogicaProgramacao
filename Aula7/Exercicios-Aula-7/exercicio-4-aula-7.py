'''
4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

'''
# lista vazia
lista = []

# lista de vogais
vogal = ['a', 'e', 'i', 'o', 'u']

# delimitador de caracteres a serem inseridos
contador = 1

# input do usuario
char = input('Digite um caracter: ')
lista.append(char)

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
           for i in lista:
            if i not in vogal:
                print(i)
        break
            
    else:
        print('FIM DO WHILE')
    
    # comparando listas
     
else:
    print('PROGRAMA ENCERRADO')


