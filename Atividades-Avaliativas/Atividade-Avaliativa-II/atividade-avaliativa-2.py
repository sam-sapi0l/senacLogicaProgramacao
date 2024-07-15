'''
Avaliação II
13/06/2024 
Faça um programa que  cadastra os nomes dos alunos,seu peso e altura em 4 listas. ALUNOS, PESOS,  ALTURAS e IMCs
faça um menu:
1-cadastra alunos, pesos,  alturas e calcula IMC
   colocar valores de cada aluno em cada uma das listas  respectivas

2-lista todos alunos,   pesos,  altura e imc
3-busca um aluno e seu peso e altura e mostra o  IMC
4-calcula as média da turma de peso,  altura  e  imc
5-fim
Obs: calculo IMC = round(Peso / altura ** 2, 2)
'''

students = []
weight = []
height = []
imcs = []

#def imc_calc(weight, height):
#    imc = round(weight/(height*height), 2)
#    imcs.append(imc)
#    return imcs

# cadastra aluno
def sign_up():
    print()
    print('#' * 30, 'SIGN-UP', '#' * 30 )

    # entrada de dados pelo usuároio para entrar nas listas

    studentName = input('Type the name: ')
    studentWeight = float(input(f'Student weight {studentName}:'))
    studentHeight = float(input(f'Student Height {studentName}:'))
    studentIMC = round(studentWeight / (studentHeight ** 2))
    
    #adicionando nas listas

    students.append(studentName.upper())
    weight.append(studentWeight)
    height.append(studentHeight)
    imcs.append(studentIMC)

#definição da função listStudents()

def listStudents():
    print()
    print('#' * 30, 'LIST STUDENTS', '#' * 30 )
    for i in range(len(students)):
        print('{0} | {1:5.2f} | {3:5.2f}'.format(students[i].ljust(10), weight[i], height[i], imcs[i]))

# define função searchStudent() para buscar aluno
def searchStudent():
    listStudents()
    while True:
        name = input('Type the name of the student you want to search: ')
        if name == '':
            return
        if name in students:
            i = students.index(name.upper())
            print(i)
            break
        else:
            print(f'{name} is not ins the student list')
    print('{0} | {1:5.2f} | {3:5.2f}'.format(students[i], weight[i], height[i], imcs[i]))
# calcula a media total de IMC 
def avg_calc():
    listStudents()
    avg_height = sum(height) / len(height)
    avg_weight = sum(weight) / len(weight)
    avg_imc = sum(imcs) / len(imcs)
    print('-' * 60)
    print('{0} | {1:5.2f} | {3:5.2f}'.format('Averages: '.ljust(10), avg_height, avg_weight, avg_imc))

# função de remover um aluno
def deleteStudent():
    listStudents()
    while True:
        name = input('Type the name of the student you want to delete: ')
        if name == '':
            return
        if name.upper() in students:
            i = students.index(name.upper())
            print(i)
            break
        else:
            print(f'{name} is NOT in student list')
        
    print('{0} ==> Deleted | {1:5.2f} | {2:5.2f} | {3:5.2f}'.format(name.ljust(10), height[i], weight[i], imcs[i]))

    del (students[i])
    del (weight[i])
    del (height[i])
    del (imcs[i])
# while para MENU e INICIO do programa
while True:
    # while para entrada de opção
    while True:
        try:
            print('#' * 30, 'MENU', '#' * 30)
            print('        1. Sign-up Students, Weights, Heights and IMCs')
            print('        2. List all students ')
            print('        3. Find a student ')
            print('        4. Calculate Class Average ')
            print('        5. Remove a student ')
            print('        6. END ')
            option = int(input('OPTION: '))
            break
        except:
            print('type only INTEGER numbers to select an option.')
    # se a opção for de 1 a 5 sai do while para o menu do programa
    if option == 6:
        break
    elif option == 1:
        sign_up()
        input('[Enter] to continue')
    elif option == 2:
        listStudents()
        input('[Enter] to continue')
    elif option == 3:
        searchStudent()
        input('[Enter] to continue')
    elif option == 4:
        avg_calc()
        input('[Enter] to continue')
    elif option == 5:
        deleteStudent()
        input('[Enter] to continue') 

    


