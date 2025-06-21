# Análise:
# criar um programa para gerenciar os itens e as suas quantidades
# em um carrinho de compras.
#
# O sistema deve ter um menu para o usuário realizar as seguintes ações:
# - Adicionar item: insere um novo produto no carrinho. Se o item já existir,
# apenas atualiza a sua quantidade;
# - Remover item: exclui um produto do carrinho;
# - Atualizar quantidade: modifica a quantidade de um item existente.
# Se a quantidade for atualizada para um valor >= 0, o item deve ser removido;
# - Visualizar carrinho: mostra todos os itens do carrinho;
# - Limpar carrinho: remove todos os itens do carrinho;
# - Sair: encerra o programa.
#
# Além disso, o programa deve:
# - Bloquear a remoção ou atualização de um item que não se encontra no carrinho;
# - Constantemente exibir a quantidade total de itens no carrinho.
#
# Tipos de dados:
# - produtos: str
# - quantidades: int
# - carrinho: dic

def adiciona(carrinho: dict) -> None:
    print('Digite o nome do produto que você deseja adicionar.')
    nome = input()
    print()
    print('Digite a quantidade do produto que você deseja adicionar.')
    quantidade = int(input())
    print()
    if quantidade <= 0:
        print('Quantidade inválida.')
            
    else:
        carrinho.update({nome: quantidade})
        print('Sucesso!')

def remove(carrinho: dict) -> None:
    print('Digite o nome do produto que você deseja remover.')
    nome = input()
    print()

    if nome in carrinho:
        del carrinho[nome]
        print('Sucesso!')
    else:
        print('Produto não encontrado.')

def atualiza(carrinho) -> None:
    print('Digite o nome do produto cuja quantidade')
    print('você deseja atualizar.')
    nome = input()

    if nome in carrinho:
        print('Digite a nova quantidade do produto.')
        quantidade = int(input())
        if quantidade <= 0:
            del carrinho[nome]
            print('Produto removido. Sucesso!')

        else:
            carrinho.update({nome: quantidade})
            print('Sucesso!')
                
    else:
        print('Produto não encontrado.')

def limpa(carrinho) -> None:
    if len(carrinho) != 0:
        print('Você tem certeza que deseja limpar o carrinho?')
        print('Digite 1 para confirmar e 0 para cancelar.')
        confirma = int(input())
        if confirma:
            carrinho.clear()
            
    else:
        print('Não há produtos no seu carrinho.')
        
def qnt_total(carrinho: dict) -> None:
    '''Exibe a quantidade total de produtos em *carrinho*
    de uma forma agradável ao usuário.
    '''

    total = 0
    for valor in carrinho.values():
        total += valor
        
    if total == 1:
        print('Há 1 item no seu carrinho.')
    else:
        print(f'Há {total} itens no seu carrinho.')


def exibe_carrinho(carrinho: dict) -> None:
    '''Exibe cada item de *carrinho* com sua respectiva quantidade
    de uma forma agradável ao usuário.
    '''

    if len(carrinho) == 0:
        print('[VAZIO]')
        
    else:
        for chave, valor in carrinho.items():
            print(f'{chave}: {valor}')        
    print()

def sair() -> bool:
    print('Você tem certeza que deseja encerrar o programa e sair?')
    print('Digite 1 para confirmar e 0 para cancelar')
    confirma = int(input())

    if confirma:
        print('Obrigado por usar nossos serviços.')
        print('Até a próxima!')
        
        ligado = False
    else:
        ligado = True

    return ligado

def carrinho() -> None:
    '''Gerencia os itens em um carrinho de compras e as suas quantidades.

    Possibilita as seguintes ações:
    - Adicionar item: insere um novo produto no carrinho. Se o item já existir,
    apenas atualiza a sua quantidade, porém não permite que quantidade <= 0.
    - Remover item: exclui um produto do carrinho;
    - Atualizar quantidade: modifica a quantidade de um item existente.
    Se a quantidade for atualizada para um valor >= 0, o item deve ser removido;
    - Visualizar carrinho: mostra todos os itens do carrinho;
    - Limpar carrinho: remove todos os itens do carrinho;
    - Sair: encerra o programa.

    Além disso:
    - É bloqueada a remoção e atualização de itens
    que não se encontram no carrinho;
    - A quantidade total de itens no carrinho é constantemente exibida.
    '''

    carrinho = {}
    ligado = True
    print('Bem-vindo!')
    while ligado:

        qnt_total(carrinho)
        print('Para adicionar um produto, digite 0')

        if len(carrinho) == 0:
            print('Para sair e encerrar o programa, digite 5')
            print()
        else:
            print('Para remover um produto, digite 1')
            print('Para atualizar a quantidade de um item, digite 2')
            print('Para visualizar os itens no carrinho, digite 3')
            print('Para limpar o carrinho, digite 4')
            print('Para sair e encerrar o programa, digite 5')
            print()

        acao = int(input())

        if acao == 0:
            adiciona(carrinho)

        elif acao == 1:
            remove(carrinho)

        elif acao == 2:
            atualiza(carrinho)

        elif acao == 3:
            exibe_carrinho(carrinho)
            
        elif acao == 4:
            limpa(carrinho)

        elif acao == 5:
            ligado = sair()











            
            

    
                


































    
