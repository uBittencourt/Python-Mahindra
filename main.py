from data import season10, pilotos_season10

def calcular_pontuacao() -> None:
    """
    Esta função calcula a pontuação dos pilotos a partir de suas posições em cada corrida

    :return: None
    """
    # ESTE FOR SERVE PARA CONTABILIZAR OS PONTOS PARA CADA PILOTO
    for corrida in season10:

        # FOR PARA FAZER A CONTABILIZAÇÃO DOS PONTOS DENTRO DA CLASSIFICAÇÃO
        for i in range(len(corrida['podio'])):
            # O MATCH CASE VERIFICA A CLASSIFICACAO ENTRE 0 E 9 (1° ATÉ 10°)
            match i:
                case 0:
                    for piloto in pilotos_season10:
                        if piloto['nome'] == corrida['podio'][i]:
                            piloto['vitorias'] += 1
                            piloto['pontos'] += 25
                            piloto['podios'] += 1 

                case 1:
                    for piloto in pilotos_season10:
                        if piloto['nome'] == corrida['podio'][i]:
                            piloto['pontos'] += 18    
                            piloto['podios'] += 1    

                case 2:
                    for piloto in pilotos_season10:
                        if piloto['nome'] == corrida['podio'][i]:
                            piloto['pontos'] += 15 
                            piloto['podios'] += 1    
                            
                case 3:
                    for piloto in pilotos_season10:
                        if piloto['nome'] == corrida['podio'][i]:
                            piloto['pontos'] += 12
                
                case 4:
                    for piloto in pilotos_season10:
                        if piloto['nome'] == corrida['podio'][i]:
                            piloto['pontos'] += 10 

                case 5:
                    for piloto in pilotos_season10:
                        if piloto['nome'] == corrida['podio'][i]:
                            piloto['pontos'] += 8
                
                case 6:
                    for piloto in pilotos_season10:
                        if piloto['nome'] == corrida['podio'][i]:
                            piloto['pontos'] += 6
                            
                case 7:
                    for piloto in pilotos_season10:
                        if piloto['nome'] == corrida['podio'][i]:
                            piloto['pontos'] += 4
                
                case 8:
                    for piloto in pilotos_season10:
                        if piloto['nome'] == corrida['podio'][i]:
                            piloto['pontos'] += 2
                
                case 9:
                    for piloto in pilotos_season10:
                        if piloto['nome'] == corrida['podio'][i]:
                            piloto['pontos'] += 1

        # FOR PARA CAPTAR PONTOS DE POLE POSITION E MELHOR VOLTA
        for piloto in pilotos_season10:
            if piloto['nome'] == corrida['pole_position']:
                piloto['pontos'] += 3
            
            if piloto['nome'] == corrida['melhor_volta']:
                piloto['pontos'] += 1


def apresentar_pilotos() -> None:
    """
    Esta função apresenta um menu com todos os pilotos da Fórmula E

    :return: None
    """
    cont = 0
    # FOR PARA APRESENTAR TODOS OS PILOTOS
    print(f'-'*20, 'PILOTOS SEASON 10', '-'*20, end='\n\n')
    for i in range(len(pilotos_season10)):
        cont += 1
        if cont == 2:
            print(f'{i+1}) {pilotos_season10[i]['nome']}')
            cont = 0
        else:
            print(f'{i+1}) {pilotos_season10[i]['nome']:<25}', end='\t')
    print()


def apresentar_corridas() -> None:
    """
    Esta função apresenta um menu com todas as corridas da temporada da Fórmula E

    :return: None
    """
    cont = 0
    # FOR PARA APRESENTAR TODAS AS CORRIDAS
    print(f'-'*15, 'CORRIDAS SEASON 10', '-'*15, end='\n\n')
    for i in range(len(season10)):
        cont += 1
        if cont == 2:
            print(f'{i+1}) {season10[i]['nome']}')
            cont = 0
        else:
            print(f'{i+1}) {season10[i]['nome']:<25}', end='\t')
    print()


def dados_piloto(indice: int = 1) -> None:
    """
    Esta função apresenta todas as informações de um piloto, como 
    equipe, nascionalidade, vitórias, pódios e seus pontos

    :param indice: Índice para selecionar o piloto
    :type indice: int

    :return: None
    """
    # FOR PARA CAPTAR OS DADOS DO PILOTO ESCOLHIDO
    try:    
        for chave, valor in pilotos_season10[indice-1].items():
            # CONDICIONAL PARA PRINTAR CORRETAMENTE OS DADOS
            if chave == 'nome': 
                print('-'*15, f'{valor}', '-'*15) # PRINTANDO NOME COMO UM TÍTULO
                continue
            elif chave == 'nascionalidade':
                print(f'{chave.title()}: ', end='\t')
            else:
                print(f'{chave.title()}: ', end='\t\t')
            print(f'{valor:^20}') # O VALOR É PRINTADO CENTRALIZADO
    except IndexError:
        print('Informe um índice válido')


def dados_corrida(indice: int = 1) -> None: 
    """
    Esta função apresenta as informações de uma determinada corrida como,
    o seu pódio, quem foi o pole position e quem fez a melhor volta

    :param indice: Índice para selecionar a corrida
    :type indice: int

    :return: None
    """
    # FOR PARA SELECIONAR A CORRIDA A PARTIR DO INDICE INDICADO
    try:
        for chave, valor in season10[indice - 1].items():
            # CONDICIONAL PARA EXIBIR CORRETAMENE OS DADOS
            if chave == 'nome':
                print('-'*15, f'{valor}', '-'*15)
            elif chave == 'podio':
                print(f'{chave.title()}: ', end='\t\t\t')
                # FOR PARA EXIBIR O PÓDIO DA CORRIDA SELECIONADA
                for i in range(3):
                    print(f'{i+1}° {valor[i]}', end='\n\t\t\t')
                print()
            else:
                print(f'{chave}: ', end='\t\t')
                print(f'{valor:^15}')
    except IndexError:
        print('Informe um índice válido')


def mostrar_ranking() -> None:
    """
    Esta função apresenta o ranking dos pilotos na temporada atual,
    a partir de suas respectivas pontuações

    :return: None
    """
    print('-' * 10, 'RANKING FÓRMULA E - SEASON 10', '-' * 10, end='\n\n')
    cont = 0
    # FOR PARA APRESENTAR O RANKING DA TEMPORADA
    for i in range(len(ranking)):
        cont += 1
        if cont == 2:
            print(f'{i + 1}° {ranking[i]}')
            cont = 0
        else:
            print(f'{i + 1}° {ranking[i]:<25}', end='\t')


# CHAMANDO A FUNÇÃO PARA ASSIM CONTABILIZAR OS PONTOS NO INICIO DO PROGRAMA
calcular_pontuacao()

# BLOCO DE COMANDO PARA FAZER O RANKING
lista = [pilotos_season10[i]['pontos'] for i in range(len(pilotos_season10))]
lista.sort(reverse=True)
ranking = []
for numero in lista:
    for i in range(len(pilotos_season10)):
        if pilotos_season10[i]['pontos'] == numero:
            if pilotos_season10[i]['nome'] not in ranking:
                ranking.append(pilotos_season10[i]['nome'])

# WHILE PARA EXECUTAR MENU ATÉ SER SELECIONADA A OPÇÃO SAIR
while True:
    try:
        print('-' * 10, 'FÓRMULA E - SEASON 10', '-' * 10)
        print('[1] - Visualizar Pilotos \n[2] - Selecionar Piloto \n[3] - Visualizar Corridas \n[4] - Selecionar Corrida \n[5] - Mostrar Ranking \n[6] - Sair')
        opcao = int(input('\nSelecione uma opção: '))

        if opcao <= 0:
            raise TypeError('O valor informado deve ser positivo')
    except ValueError:
        print('\nO valor informado deve ser um número inteiro\n')
    except TypeError as msg:
        print(f'\n{msg}')

    else:
        print()
        match opcao:
            case 1:
                apresentar_pilotos()
            case 2:
                try:
                    indice_piloto = int(input('Digite o índice do piloto: '))

                    if indice_piloto <= 0:
                        raise TypeError('O índice informado deve ser positivo')
                except ValueError:
                    print('\nO índice informado deve ser um número inteiro')
                except TypeError as msg:
                    print(f'\n{msg}')
                else:
                    print()
                    dados_piloto(indice_piloto)
            case 3:
                apresentar_corridas()
            case 4:
                try:
                    indice_corrida = int(input('Digite o índice da corrida: '))

                    if indice_corrida <= 0:
                        raise TypeError('O índice informado deve ser positivo')
                except ValueError:
                    print('\nO índice informado deve ser um número inteiro')
                except TypeError as msg:
                    print(f'\n{msg}')
                else:
                    print()
                    dados_corrida(indice_corrida)
            case 5:
                mostrar_ranking()
            case 6:
                print('Encerrando programa...')
                break
            case _:
                print('Opção Inválida')
        
        print()
