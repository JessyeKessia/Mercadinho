from Caixa import Caixa

Caixa = Caixa()

while True:
    print('+--------------+')
    print(f'|Bem-vindo|')
    print('+--------------+')

    print('(P)rocurar')
    print('(V)ender')
    print('(E)xibir Produtos')
    print('(S)air')
    print('---------------')

    funcao = input('Digite a sua escolha: ').lower()
    
    if funcao == 'p':
        nome = input('Insira o nome: ')
        print(Caixa.procura_prod(nome))
    elif funcao == 'v':
         nome = input('Digite o nome do produto: ')
         quantidade = int(input('Digite a quantidade de produtos: '))
         print(Caixa.vender(nome, quantidade))
    elif funcao == 'e':
        print(Caixa.exibe_todos_produtos())
    elif funcao == 's':
        break
    else:
        print('Digite uma opção válida')