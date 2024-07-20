'''
## Gerenciamento de Estoque e Vendas em Python
**Descrição:**

Este programa em Python auxilia no gerenciamento de estoque e vendas de produtos, utilizando menus interativos para facilitar a navegação. O programa armazena informações em quatro listas:

* **Produtos:** Armazena os nomes dos produtos cadastrados.
* **Preços:** Armazena os preços correspondentes a cada produto.
* **Estoque: ** Armazena a quantidade de estoque em cada produto
* **Vendas:** Armazena os nomes dos produtos vendidos.
* **Quantidades:** Armazena as quantidades vendidas de cada produto.

**Funcionalidades:**

**Menu:**
* **Incluir Produto:** Permite adicionar um novo produto à lista de produtos, seu preço à lista de preços e quantidade de estoque.
* **Incluir Venda:** Permite registrar a venda de um produto, selecionando-o da lista de produtos e informando a quantidade vendida e deve abater da quantidade de estoque.
* **Relatório de Estoque:** Exibe a lista completa de produtos com seus respectivos preços e quantidades em estoque (quantidades cadastradas - quantidades vendidas).
* **Relatório de Vendas:** Exibe a lista completa de produtos vendidos com suas respectivas quantidades vendidas e valor total de venda.
* **Produto Mais Vendido:** Identifica e exibe o produto com maior quantidade vendida.
* **Média de Vendas:** Calcula e exibe a média de produtos vendidos.
* **Sair:** Encerra o programa.

**Observações:**

* O programa utiliza estruturas de decisão (if/else) e laços de repetição (for/while) para controlar o fluxo do programa e gerenciar as listas de dados.
* O programa não possui salvamento de dados persistente. As informações nas listas são armazenadas apenas durante a execução do programa.
* Este programa serve como base para aprimoramentos, como inclusão de funcionalidades para salvar dados em arquivos, gerar relatórios mais detalhados, implementar um sistema de autenticação de usuário, entre outras.

**Exemplos de Uso:**

* Cadastrar um novo produto: "mouse" e seu preço: R$ 25,00
* Registrar a venda de 2 unidades de "mouse"
* Gerar o relatório de estoque para verificar a quantidade restante de "mouse"
* Consultar o produto mais vendido e sua quantidade total vendida
* Calcular a média de produtos vendidos em todas as vendas registradas
**Este programa é ideal para alunos iniciantes em Python, pois permite praticar conceitos básicos da linguagem, como:**
* Variáveis e tipos de dados
* Listas e suas operações
* Estruturas de controle (if/else, for/while)
* Funções
* Entrada e saída de dados
**Além de auxiliar no aprendizado da linguagem Python, o programa também oferece uma ferramenta prática para gerenciar estoque e vendas de produtos de forma simples e organizada.**
'''

# incializando listas
products = []
prices = []
stock =  []
sales = []
quantitySold = []

# lista os produtos, preços, estoque e quantidade
def listProducts():
    print()
    print('#' * 30, 'LIST PRODUCTS', '#' * 30)
    for i in range(len(products)):
        print('{0} | {1:52f} | {3:5.2f}'.format(products[i].ljust(10), prices[i], stock[i], quantitySold[i]))

#  Incluir Produto:** Permite adicionar um novo produto à lista de produtos, seu preço à lista de preços e quantidade de estoque.
def addProduct():
    listProducts()

    # entrada de dados do usuário
    productName = input('Type product name: ')
    productPrice = float(input('Type product price: '))
    productQuantity = int(input('Quantity: '))

    # adicionando em listas
    products.append(productName.upper())
    prices.append(productPrice)
    # verificando se produto já possui quantidade em estoque e soma com quantidade existente
    if productName in products:
       for i in stock:
            quantitySum = productQuantity + stock.index(i)
            stock.append(quantitySum)
            quantitySold.append(quantitySum)
    else:
        stock.append(productQuantity)
        quantitySold.append(productQuantity)

# Incluir Venda:Permite registrar a venda de um produto, selecionando-o da lista de produtos e informando a quantidade vendida e deve abater da quantidade de estoque.

def addSale():
    listProducts()
    print()

    salesmanName = input('Salesman: ')
    productName = input('Type product name: ')
    productPrice = float(input('Price {productName} : '))
    productQuantity = int(input(' Quantity {productName}:  '))

    sales.append(salesmanName)
    sales.append(productName)
    sales.append(productPrice)
    sales.append(productQuantity)

    # ajustando quantidade em estoque
    for i in stock:
       if productName in products: 
           print(f'Product: {productName}')
           print(f'Quantity: {stock.index(i)}')
           print()
           print()
           removeItemQuantity = stock.index(i) - productQuantity
           stock.remove(i)
           stock.append(removeItemQuantity)
           productSold = productPrice * productQuantity
           print('{0} | {1:52f} | {3:5.2f}'.format(products[i].ljust(10), prices[i], stock[i], quantitySold[i], productSold))
       else:
           print(f'{productName} not available desired quantity for this item.')
           

def stockReport():
    listProducts()
    print()
    print('#' * 30, 'STOCK REPORT', '#' * 30)
    for i in range(len(stock)):
        print('{0} | {1:52f} | {3:5.2f}'.format(products[i].ljust(10), prices[i], stock[i]))

    

def salesReport():
    listProducts()
    print()
    print('#' * 30, 'SALES REPORT', '#' * 30)
    for i in range(len(products)):
        print('{0} | {1:52f} | {3:5.2f}'.format(products[i].ljust(10), prices[i], stock[i], max(quantitySold[i])))

def mostSold():
    listProducts()
    print()
    print('#' * 30, 'SALES REPORT', '#' * 30)
    for i in range(len(products)):
        print('{0} | {1:52f} | {3:5.2f}'.format(products[i].ljust(10), prices[i], max(quantitySold[i])))

def avg_sold():
    for i in products:
        avg = len(products) / quantitySold[i]
        print(f'Product Sales Average: {avg}')



while True:
    # while para entrada de opção
    while True:
        try:
            print('#' * 30, 'MENU', '#' * 30)
            print('        1. Add Prouct')
            print('        2. List all products ')
            print('        3. Stock Report ')
            print('        4. Sales Report ')
            print('        5. Average Sold ')
            print('        6. Most Sold Product')
            print('        7. END ')
            option = int(input('OPTION: '))
            break
        except:
            print('type only INTEGER numbers to select an option.')
    # se a opção for de 1 a 5 sai do while para o menu do programa
    if option == 7:
        break
    elif option == 1:
        addProduct()
        input('[Enter] to continue')
    elif option == 2:
        listProducts()
        input('[Enter] to continue')
    elif option == 3:
        stockReport()
        input('[Enter] to continue')
    elif option == 4:
        salesReport()
        input('[Enter] to continue')
    elif option == 5:
        avg_sold()
        input('[Enter] to continue') 
    elif option == 6:
        mostSold()
        input('[Enter] to continue')

    

            