'''
14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    1. "Telefonou para a vítima?"
    2. "Esteve no local do crime?"
    3. "Mora perto da vítima?"
    4. "Devia para a vítima?"
    5. "Já trabalhou com a vítima?" 
    
    
    O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


'''

# inicializando listas vazias
suspeitos = []
cumplice = []
assassino = []

# While Loop
contador = 0

while True:
  while contador < 3:
     try:
          nome = input('Digite seu nome: ')
          print()
          print('Responda Perguntas com [1]Sim e [0]Não: ')
          p1 = int(input("Telefonou para a vítima? "))
          p2 = int(input("Esteve no local do crime? "))
          p3 = int(input("Mora perto da vítima? "))
          p4 = int(input("Devia para a vítima? "))
          p5 = int(input("Já trabalhou com a vítima? " ))
          
          
          contador += 1
          
          soma_resposta = p1 + p2 + p3 + p4 + p5            
          
          if soma_resposta > 1 or soma_resposta < 3:
              suspeitos.append(nome)
          elif soma_resposta >= 3 or soma_resposta > 5:
              cumplice.append(nome)
          elif soma_resposta >= 4 or soma_resposta <=5:
              assassino.append(nome)
          else:
               pass

     except:
         print('Entrada Inválida!')
      
        
     if contador == 3:
      break

     else:
         print('FIM DO WHILE INTERNO')

  break 
else:
    print('FIM DO WHILE')

        
print(f'Suspeitos: {suspeitos}')
print(f'Cúmplices: {cumplice}')
print(f'Assassinos: {assassino}')
