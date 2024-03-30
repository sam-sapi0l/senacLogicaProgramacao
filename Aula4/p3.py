'''

3. Ler três valores numéricos e escrever a média aritmética.

'''

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite terceiro e ultimo valor: "))

media = (valor1 + valor2 + valor3) / 3

print(f"A média entre os valores informados é: {media:.2f}")
print(round((valor1 + valor2 + valor3)/3, 2))