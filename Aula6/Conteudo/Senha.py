senha = input('Digite a senha: ')
contador = 1
while senha != 'SenhaCorreta':
    print('Senha inválida!')
    if contador >= 3:
        print(f'Tentativa {contador} / 3')
        print('Programa Encerrado.')
        break
    print(f'Tentativa: {contador} / 3')
    contador += 1
    senha = input('Digite a senha: ')
else:
    print('Senha OK!')

