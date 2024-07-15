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
quantity = []

# lista os produtos, preços, estoque e quantidade
def listProducts():
    print()
    print('#' * 30, 'LIST PRODUCTS', '#' * 30)
    for i in range(len(products)):
        print('{0} | {1:52f} | {3:5.2f}'.format(products[i].ljust(10), prices[i], stock[i], quantity[i]))


#  Incluir Produto:** Permite adicionar um novo produto à lista de produtos, seu preço à lista de preços e quantidade de estoque.
def addProduct():
    listProducts()

    # entrada de dados do usuário
    productName = input('Type product name: ')
    productPrice = float(input('Type product price: '))
    productQuantity = int(input(' Quantity for {productName} to add: '))
    # adicionando em listas

    products.append(productName.upper())
    prices.append(productPrice)
    quantity.append(productQuantity)
    stock.append(productQuantity)

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
           print(f'Item: {productName}')
           print(f'Quantity: {removeItemQuantity}')
       else:
           print(f'{productName} not available desired quantity for this item.')
           

def stockManager():
    listProducts()
    print()
    productName = input('Type product name: ')
    

            