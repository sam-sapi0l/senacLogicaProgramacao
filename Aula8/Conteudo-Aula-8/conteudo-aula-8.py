# inicializa Listas e Variáveis
alunos=['ÉRICK', 'ANA']
pesos=[70,54.4]
alturas=[1.80, 1.74]
imcs=[]
imc = round(70/(1.80*1.80),2)
imcs.append(imc)
imcs.append(round(54.4/(1.74**2),2))
#print(alunos)
#print(pesos)
#print(alturas)
#print (imcs)


def cadastrar():
    print()
    print('*'*30, ' CADASTRAR ALUNOS ','*'*30 )

    #entrada de dados pelo usuário para colocar nas listas

    nomeAluno=input('Digite nome do aluno: ')

    pesoAluno=float(input(f'Peso de { nomeAluno}:'))

    alturaAluno=float(input(f'Altura  de { nomeAluno}:'))

    imcAluno = round(pesoAluno / (alturaAluno**2))

    #adicionar nas listas

    alunos.append(nomeAluno.upper())

    pesos.append(pesoAluno)

    alturas.append(alturaAluno)

    imcs.append(imcAluno)

#definicáo da função listarAlunos()

def listarAlunos():

    print()

    print('*' * 30, ' LISTAR ALUNOS ', '*' * 30)
    for i in range (len(alunos)):
        print( '{0} | {1:5.2f} | {2:5.2f} | {3:5.2f}'.format(alunos[i].ljust(10),  pesos[i],  alturas[i], imcs[i]))


def buscarAluno():
    listarAlunos()
    '''
    while True:
        try:
            nome=input('Digite Nome do aluno para buscar dados:')
            i = alunos.index(nome.upper())
            break
        except:
            print(f'{nome} NÃO está na lista alunos')
    '''
    while True:
        nome = input('Digite Nome do aluno para buscar dados:')
        if nome =='':
            return
        if nome in alunos:
            i = alunos.index(nome.upper())
            break
        else:
            print(f'{nome} NÃO está na lista alunos')

    print('{0} | {1:5.2f} | {2:5.2f} | {3:5.2f}'.format(alunos[i].ljust(10), pesos[i], alturas[i], imcs[i]))


def calcMedia():
    listarAlunos()
    altura_media=sum(alturas)/len(alturas)
    peso_medio=sum(pesos)/len(pesos)
    imcs_medio=sum(imcs)/len(imcs)
    print('-'*60)
    print('{0} | {1:5.2f} | {2:5.2f} | {3:5.2f}'.format('Medias'.ljust(10), peso_medio, altura_media, imcs_medio))
def excluirAluno():
    listarAlunos()
    while True:
        nome = input('Digite Nome do aluno para Excluir dados:')
        if nome =='':
            return
        if nome.upper() in alunos:
            i = alunos.index(nome.upper())
            print(i)
            break
        else:
            print(f'{nome} NÃO está na lista alunos')

    print('{0} ==> Excluído | {1:5.2f} | {2:5.2f} | {3:5.2f}'.format(nome.ljust(10), pesos[i], alturas[i], imcs[i]))

    del (alunos[i])
    del (pesos[i])
    del (alturas[i])
    del (imcs[i])

#while para MENU e INÍCIO DO programa
while True:
    # while para entrada da Opcao
    while True:
        try:
            print("*"*30, " MENU ", "*"*30)
            print('     1) Cadastrar Alunos, pesos, alturas e IMC')
            print('     2) lista todos os alunos ')
            print('     3) Busca um aluno')
            print('     4) Calcula média da turma')
            print('     5) Excluir Aluno ')
            print('     6) FIM')
            opcao=int(input("OPÇÃO:"))
            break
        except:
            print ("digite números INTEIROS  para opcão")
    # se opcao == 5 sai do While para o MENU encerra programa
    if opcao == 6:
        break
    elif opcao==1:
        cadastrar()
    elif opcao==2:
        listarAlunos()
        input('[Enter] para continuar')
    elif opcao==3:
        buscarAluno()
        input('[Enter] para continuar')
    elif opcao==4:
        calcMedia()
        input('[Enter] para continuar')
    elif opcao==5:
        excluirAluno()
        input('[Enter] para continuar')
