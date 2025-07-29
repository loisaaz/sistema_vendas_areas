
# dicionarios e listas que serão usados ao decorrer do programa

voos = {} # voos cadastrados no sistema entrarão aqui
passageiros= {}

# Voos: contendo o número do voo (chave), cidade origem, cidade destino, número de escalas, preço da passagem, quantidade de lugares disponíveis
#• Passageiros: contendo informações como CPF (chave), nome, telefone. Cada cliente pode comprar mais de uma passagem
#• Utilizar listas para armazenar:
#• Listas de voos disponíveis, quando a quantidade de lugares disponíveis de um voo chega a zero o voo fica indisponível para venda
#• Listas de passageiros que compraram passagens para um determinado voo

# part 1

option = 0

while option != 7:
    print('\n\t---------- MENU DO SISTEMA ----------')
    print('\n\t[1] Cadastrar um Voo')
    print('\t[2] Consultar um Voo')
    print('\t[3] Verificar Voo com menor escala')
    print('\t[4] Listar passageiros de um Voo')
    print('\t[5] Compra de passagem')
    print('\t[6] Cancelar uma passagem')
    print('\t[7] Sair')

    option = int(input('\n\tDigite uma opção: '))

    while option not in [1, 2, 3, 4, 5, 6, 7]:
        print("\n\tOpção inválida !")
        option = int(input('\n\tDigite uma opção: '))

    # part 2      
        
    if option == 1:
        print('\n------------------------------------------------------------------')
        print('\n\tOpção cadastrar Voo escolhida...')
        print('\n------------------------------------------------------------------')

        codigo =  int(input("\n\tDigite o código do Voo: "))

        if codigo in voos:
            print('\n\tHá um voo cadastrado com esse código!')
            codigo =  int(input("\n\tDigite o código do Voo: "))
        else:
            origem = input("\n\tDigite a cidade de origem: ").strip().upper()
            destino = input("\n\tDigite a cidade de destino: ").strip().upper()
            escala = int(input("\n\tQuantas escalas têm o voo: "))
            preco = float(input("\n\tPreço da passagem: "))
            capacidade = int(input("\n\tQuantidade de lugares disponíveis: "))
            
            voos[codigo] = {
                "Origem": origem,
                "Destino": destino,
                "Escalas": escala,
                "Preço": preco,
                "Lugares disponiveis": [capacidade],
                "Passageiros": passageiros
            } 
            print(f'\n\tVoo "{codigo}" cadastrado com sucesso!')
            #print(f"\tInformações: {codigo}:{voos[codigo]}")
    elif option == 2:
        print('\n------------------------------------------------------------------')
        print('\n\tOpção consultar um Voo escolhida...')
        print('\n------------------------------------------------------------------')
        print('\n\tComo deseja realizar a consulta?')
        print('\t[1] Pelo código do Voo')
        print('\t[2] Cidade Origem')
        print('\t[3] Cidade Destino')

        d = int(input('\n\tDigite uma opção: '))
        while d not in [1, 2, 3]:
            print("\n\tOpção inválida !")
            d = int(input('\n\tDigite uma opção: '))

        if d == 1:
            c = int(input('\n\tInforme o código: '))
            for codigo in voos.keys():
                if codigo == c:
                    print(f"\n\tVoo {codigo} Informações: {voos[codigo]}")
            else:
                print('\n\tNenhum voo encontrado')

        elif d == 2:
        # Cidade Origem:  imprimir o Código do Voo, cidade  Destino, preço de todos os voos 
            d_o = input('\n\tDigite a cidade origem: ').strip().upper()
            for codigo, dados in voos.items():
                if dados["Origem"] == d_o:
                    print(f'\n\tCódigo: {codigo} Destino: {dados["Destino"]} Preço: R${dados["Preço"]:.2f}')
                    #print(f'\n\t{voos[codigo]}')
            else:
                print('\n\tNenhum voo encontrado')

        elif d == 3:
        # Cidade Destino: imprimir o Código do Voo, cidade  Origem, preço de todos os voos
            d_d = input('\n\tDigite a cidade destino: ').strip().upper()
            for codigo, dados in voos.items():
                if dados["Destino"] == d_d:
                    print(f'\n\tCódigo: {codigo} Origem: {dados["Origem"]} Preço: R${dados["Preço"]:.2f}')
                    #print(f'\n\t{voos[codigo]}')
                else:
                    print('\n\tNenhum voo encontrado')

    elif option == 3:
        #  Informar o Voo com menor Escala, dado a cidade Origem e Destino
        print()
        print('\n------------------------------------------------------------------')
        print('\n\tOpção consultar Voo com menor escala escolhida...')
        print('\n------------------------------------------------------------------')
        origem = input("\n\tDigite a cidade de origem: ").strip().upper()
        destino = input("\n\tDigite a cidade de destino: ").strip().upper()
        
        menor_escala = 999
        voo_menor_escala = '-' 
        
        for codigo, dados in voos.items():
            if dados["Origem"] == origem and dados["Destino"] == destino:
                if dados["Escalas"] < menor_escala:
                    menor_escala = dados["Escalas"]
                    voo_menor_escala = codigo
        if voo_menor_escala:
            print(f'\n\tVoo com menor escala: \n[Código:{voo_menor_escala} Escala: {menor_escala}]')
        else:
            print("\n\tNenhum voo encontrado para essa origem e destino.")
    elif option == 4:
        print('\n------------------------------------------------------------------')
        print('\n\tOpção passageiros de um Voo escolhida...')
        print('\n------------------------------------------------------------------')
        c_c = int(input('\n\tInforme o código do Voo: '))
        
        # nao fiz parte de compra

    elif option == 5:
        print('\n------------------------------------------------------------------')
        print('\n\tOpção venda de passagem escolhida...')
        print('\n------------------------------------------------------------------')
        print()
        cod_voo = int(input('\n\tInforme o código do Voo: '))

        if cod_voo in voos:
            #if codigo == cod_voo:
            passagem = int(input('\n\tQuantidade de passagens: '))
            if passagem > voos[codigo]['Lugares disponiveis'][0]:
                print('\n\tNão há esse números de passagens disponíveis.')
            else:
                 
                nome = input('\n\tInforme o nome do comprador: ').strip().upper()
                cpf = input('\n\tInforme o CPF do comprador: ').strip()
                telefone = input('\n\tInforme o telefone do comprador: ').strip()
                
                passageiros[cpf] = [passagem, nome, telefone]
                voos[cod_voo]['Lugares disponiveis'][0] -= passagem
                #print(passageiros)
                print('\n\tPassagens compradas!') 
                print('\n\tCapacidade restante no voo:', voos[cod_voo]['Lugares disponiveis'][0])   

               # comprar = input('\nDeseja fazer outra compra de passagens?').strip().upper()
               # if comprar == 'SIM' and 'S':
               #     cod_voo = int(input('\n\tInforme o código do Voo: '))
               
        else: # essa parte está aparecendo msm com o voo sendo encontrado
            print('\n\tNenhum voo encontrado')

 
                # atualizar quantidade de lugares no voo e atualizar a lista de passageiros
        
        # Venda de passagem : permitir que um cliente compre uma passagem para um voo disponível, 
        # solicitando suas informações. As informações da lista de passageiro e da capacidade disponível devem ser atualizadas. 
        # digite o código do voo que deseja comprar
        # se pessoas com nomes diferentes estão apresentando o mesmo CPF etc
        # COMPRA POR CPF, nome, idade, quantidadesde lugares que quer comprar

    elif option == 7:
        print('\n\tSaindo do sistema...')
        # \n\t



