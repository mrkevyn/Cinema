# Defina a lista de filmes e suas respectivas classificações indicativas e preços de ingresso
filmes = {
    'Godzilla Vs. Kong': {'classificacao': 12, 'preco': 26},
    'Mortal Kombat': {'classificacao': 16, 'preco': 26},
    'Cruella': {'classificacao': 10, 'preco': 26},
    'Invocação do Mal 3 – A Ordem do Demônio': {'classificacao': 14, 'preco': 26}
}

# Listas para armazenar os dados dos clientes
clientes = []
idades = []
cartoes = []
precos = []

# Opções do menu principal
opcoes_menu = [
    '-----Comprar ingresso',
    '-----Consultar lista de filmes',
    '-----Verificar quantos ingressos foram vendidos',
    '-----Fechar cinema'
]

# Função para lidar com o menu principal
def menu():
    print('Cinema')
    for i, opcao in enumerate(opcoes_menu, start=1):
        print(f"{i}-{opcao}")
    opcao = int(input('Escolha uma opção: '))
    return opcao

# Função para lidar com a compra de ingressos
def comprar_ingresso():
    print('Compra de ingresso(s)')
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    
    for i, (filme, info_filme) in enumerate(filmes.items(), start=1):
        classificacao = info_filme['classificacao']
        preco = info_filme['preco']
        print(f'{i} - {filme}, classificação indicativa: {classificacao}, valor do ingresso: R$ {preco}')
    
    escolha_filme = int(input('Escolha o número do filme que deseja assistir: '))
    filme_escolhido = list(filmes.keys())[escolha_filme - 1]
    if filme_escolhido not in filmes:
        print('Filme não encontrado!')
        return
    
    info_filme = filmes[filme_escolhido]
    classificacao = info_filme['classificacao']
    preco = info_filme['preco']
    
    if idade < classificacao:
        print(f'Desculpe, você precisa ter pelo menos {classificacao} anos para assistir "{filme_escolhido}".')
        return
    
    cartao = int(input('Digite o número do cartão: '))
    print(f'Compra realizada com sucesso. Aproveite o filme "{filme_escolhido}"!')
    clientes.append(nome)
    idades.append(idade)
    precos.append(preco)
    cartoes.append(cartao)

# Função para lidar com a compra de múltiplos ingressos
def comprar_ingressos(num_ingressos):
    for _ in range(num_ingressos):
        comprar_ingresso()

# Loop principal para executar o programa do cinema
while True:
    opcao = menu()
    if opcao == 1:
        num_ingressos = int(input('Quantos ingressos você quer comprar? '))
        comprar_ingressos(num_ingressos)
    elif opcao == 2:
        print('Lista de filmes:')
        for i, (filme, info_filme) in enumerate(filmes.items(), start=1):
            classificacao = info_filme['classificacao']
            preco = info_filme['preco']
            print(f'{i} - {filme}, classificação indicativa: {classificacao}, valor do ingresso: R$ {preco}')
    elif opcao == 3:
        print('Total de ingressos vendidos:', len(clientes))
    elif opcao == 4:
        print('Fechando cinema')
        break
    else:
        print('Opção inválida')
