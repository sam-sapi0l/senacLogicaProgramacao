'''
12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

'''

# criando listas vazias
listaIdade = []
listaAltura = []

# loop for controlando como vai ocorrer verificação
for aluno in range(1, 31):
        try:
            idade = int(input('Digite idade do aluno: '))
            altura = float(input('Digite altura do aluno: '))
        except:
            print('Entrada Inválida!')
            
        listaIdade.append(idade)
        listaAltura.append(altura)
    
        print(f'Lista de Idade: {listaIdade}')
        print(f'Lista de Altura: {listaAltura}')


# soma itens da lista
media_altura = 0        
for i in listaAltura:
    media_altura += i

# determina media de altura com base no tamanho da lista
calculaMedia = media_altura / len(listaAltura)

# Contabiliza alunos com idade superior a 13 e altura abaixo da media no controlador
for i in listaIdade:
    controladorIdade = 0
    for a in listaAltura:
        if a < calculaMedia:
          controladorIdade += 1
        elif a >= calculaMedia:
            controladorIdade += 0
        else:
            print('Problema comparando altura!')

print(f'A média de altura é: {calculaMedia:.2f}') 
print(f'O número de alunos com idade superior a 13 e altura abaixo da média é: {controladorIdade}')
