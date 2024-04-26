'''
3. Faça um programa que receba uma senha formada de quatro números inteiros, verifique se a senha está
correta e, caso não esteja, solicite novamente a senha. Se a senha entrada for a correta, deverá ser
apresentada a mensagem “Senha Correta”, caso contrário, “Senha Incorreta”.

'''

senhaSecreta = 1234

while True:
    while True:
        try:
            print('Insira uma senha de até [4] dígitos')
            senha = int(input('Digite a senha: '))
            break 
        except:
            print('Somente números.')
        if senha < 0 or senha > 9999:
            print('máximo de [4] dígitos positivos')
        elif senha == senhaSecreta:
            print('Senha Correta')
            break
        else:
            print('Senha incorreta')
print('Login OK')        