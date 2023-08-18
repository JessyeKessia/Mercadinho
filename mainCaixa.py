from Caixa import Caixa

Caixa = Caixa()

while True:
    print('+--------------+')
    print(f'|Bem-vindo|')
    print('+--------------+')

    print('(P)rocurar')
    print('(V)ender')
    print('(E)xibir Produtos')
    print('(A)bastecer estoque')
    print('(R)esertar o Caixa')
    print('(S)air')
    print('---------------')

    funcao = input('Digite a sua escolha: ').lower()
    
    if funcao == 'p':
        nome = input('Insira o nome: ').lower()
        print(Caixa.procura_prod(nome))
    elif funcao == 'v':
         nome = input('Digite o nome do produto: ').lower()
         quantidade = int(input('Digite a quantidade de produtos: '))
         print(Caixa.vender(nome, quantidade))
    elif funcao == 'e':
        print(Caixa.exibe_todos_produtos())
    if funcao == 'a':
        produto = input('Insira o nome do produto: ').lower()
        quantidade = int(input('Insira a quantidade de produtos: '))
        print(Caixa.abastecer_estoque(produto, quantidade))
    elif funcao == 'r':
        Caixa.resetar_valor()
    elif funcao == 's':
        op = input('Você deseja resetar o caixa?[s/n]: ').lower()
        if op == 's':
            Caixa.resetar_valor()
            break
        elif op == 'n':
            break
        else:
            print('Digite uma opção válida.')
            continue
    else:
        print('Digite uma opção válida')