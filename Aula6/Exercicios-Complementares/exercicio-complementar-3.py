'''
3. Fa�a um programa que receba uma senha formada de quatro n�meros inteiros, verifique se a senha est�
correta e, caso n�o esteja, solicite novamente a senha. Se a senha entrada for a correta, dever� ser
apresentada a mensagem �Senha Correta�, caso contr�rio, �Senha Incorreta�.

'''

senhaSecreta = 1234

while True:
    while True:
        try:
            print('Insira uma senha de at� [4] d�gitos')
            senha = int(input('Digite a senha: '))
            break 
        except:
            print('Somente n�meros.')
        if senha < 0 or senha > 9999:
            print('m�ximo de [4] d�gitos positivos')
        elif senha == senhaSecreta:
            print('Senha Correta')
            break
        else:
            print('Senha incorreta')
print('Login OK')        