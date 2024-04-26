# criar lista vazia
lista = []
#criar lista com conteúdo
lista1 = [7, 10, 5, 12, 5]
print(lista1[1])
# modificar item da lista
lista1[2] = lista1[2] * 5
print(lista1[2])
print(lista1)
# percorrer a lista
for i in range(5):
    print(lista1[i])
    
#                   0       1          2
lista_compras = ['banana','laranja','maçã']
#                 -3        -2        -1
print(lista_compras[2])
print(lista_compras[-1])
for i in range(3):
    print(f'{i} {lista_compras[i]}')

print()
for i in range (-1,-4,-1):
    print(f'{i} {lista_compras[i]}')

lista_compras.append('Arroz')
lista_compras.append('Feijão')
lista_compras.append('Alface e tomate')


#inserir um elemento em uma posição
lista_compras.insert(0,'Morango')
for i in range(len(lista_compras)):
     print(f'{i} {lista_compras[i]}')