import pandas

class Caixa:
    def __init__(self):
        self.tabela = pandas.read_excel('Mercado.xlsx')

    def procurar(self, nome):
        ''' Função para procurar produtos no estoque da loja '''
        produto = self.tabela.loc[self.tabela['Nome']==nome]
        return produto
    
    def exibe_todos_produtos(self):
        ''' Função para exibir todos os produtos '''
        return self.tabela
    
    def abastecer_estoque(self, produto, quantidade):
        ''' Função para abastecer o estoque '''
        produto = self.procurar(produto)
        produto = produto.values.tolist()
        produto = produto[0]
        estoque = produto[1]
        novo_estoque = estoque + quantidade
        self.tabela.loc[self.tabela['Nome']==produto[0], 'Quantidade'] = novo_estoque
        self.tabela.to_excel('Mercado.xlsx', index =False)
        return f'|Estoque abastecido. Estoque atual: {novo_estoque}|'

    def resetar_valor(self):
        ''' Função para resetar todos os valores vendidos'''
        produtos = self.tabela.values.tolist()
        for produto in produtos:
            self.tabela.loc[self.tabela['Nome']==produto[0], 'Valor vendido'] = 0.00
            self.tabela.to_excel('Mercado.xlsx', index =False)
    
    def vender(self, produto, quantidade):
        ''' Função para vender um produto '''
        produto = self.procurar(produto)
        produto = produto.values.tolist()
        produto = produto[0]
        if quantidade <= produto[1]:
            if quantidade >=10:
                valor_desconto = (produto[3] * quantidade) - (produto[4] * quantidade)
                self.tabela.loc[self.tabela['Nome']==produto[0], 'Quantidade'] = produto[1] - quantidade
                self.tabela.loc[self.tabela['Nome']==produto[0], 'Valor vendido'] = produto[5] + valor_desconto
                self.tabela.to_excel('Mercado.xlsx', index =False)
                return f'|R$ {valor_desconto:.2f}|'
            valor_real = produto[3] * quantidade
            self.tabela.loc[self.tabela['Nome']==produto[0], 'Quantidade'] = produto[1] - quantidade
            self.tabela.loc[self.tabela['Nome']==produto[0], 'Valor vendido'] = produto[5] + valor_real
            self.tabela.to_excel('Mercado.xlsx', index =False)
            return f'|R$ {valor_real:.2f}|'
        else:
            return f'Venda negada! Há apenas {produto[1]} em estoque'
        