'''
4. Faça um programa que simule a urna eletrônica.
A tela a ser apresentada deverá ser da seguinte forma:
As opcoes sao:
1. Candidato Jair Rodrigues
2. Candidato Carlos Luz
3. Candidato Neves Rocha
4. Nulo
5. Branco
Entre com o seu voto:
O programa deverá ler os votos dos eleitores e, quando for entrado o número 6, apresentar as seguintes
informações:
a) O número de votos de cada candidato;
b) A porcentagem de votos nulos;
c) A porcentagem de votos brancos;
d) O candidato venc
'''

cand1 = 0
cand2 = 0
cand3 = 0
nulos = 0
brancos = 0

print()

while True:
    print('\n1. Candidato: Jair Rodrigues\n2. Candidato: Carlos Luz\n3. Candidato: Neves Rocha\n4. Nulo\n5. Branco')
    while True:
        try:
            voto = int(input('Digite seu voto: '))
            break
        except:
           print('Somente números inteiros de 1 a 6')
    if voto == 6:
        break
    elif voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    elif voto == 4:
        nulos += 1
    elif voto == 5:
        brancos += 1
    else:
        print('Somente números inteiros de 1 a 6')

total = cand1 + cand2 + cand3 + nulos + brancos
if total == 0:
    print('Não houve votação')
else:
    print(f'Candidato Jair Rodrigues =  {cand1} votos')
    print(f'Candidato Carlos Luz     =  {cand2} votos')
    print(f'Candidato Neves Rocha   =  {cand3} votos')
    percNulos = (nulos * 100) / total
    percBrancos = (brancos * 100) / total
    print(f'Porcentagem Nulos: {percNulos:.2f}%')
    print(f'Porcentagem Brancos: {percBrancos:.2f}%')

    if cand1 > cand2 and cand1 > cand3:
        print(f'Vencedor foi candidato Jair Rodrigues com {cand1}')
    elif cand2 > cand1 and cand2 > cand3:
        print(f'Vencedor foi candidato Carlos Luz com {cand2}')
    elif cand3 > cand1 and cand3 > cand2:
        print(f'Vencedor foi candidato Neves Rocha com {cand3}')
        
        