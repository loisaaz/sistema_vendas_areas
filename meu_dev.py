# voos = {'01': cid}
# vooNumero = [cidadeOrigem, cidadeDestino, escala, preco, capacidadeDoAviao]
# voos = {"01": { "origem": "São Paulo", "destino": "Rio de Janeiro",  "escalas": 1,    "preco": 300.0,    "lugares_disponiveis": 5, "passageiros": [] }

voos = {}


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

        #cad = "S"
        #while cad == "S":
        codigo =  input("\n\tDigite o código do Voo: ")

        if codigo in voos:
            print('\n\tHá um voo cadastrado com esse código!')
            codigo =  input("\n\tDigite o código do Voo: ")
        else:
            origem = input("\n\tDigite a cidade de origem: ").upper()
            destino = input("\n\tDigite a cidade de destino: ").upper()
            escala = int(input("\n\tQuantas escalas têm o voo: "))
            preco = float(input("\n\tPreço da passagem: "))
            capacidade = int(input("\n\tQuantidade de lugares disponíveis: "))
            
            voos[codigo] = {
                "Origem": origem,
                "Destino": destino,
                "Escalas": escala,
                "Preço": preco,
                "Lugares disponiveis": capacidade,
                "Passageiros": []
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
            for c in voos:
                print(f"\n\tVoo {codigo} Informações: {voos[codigo]}")

    elif option == 7:
        print('\n\tSaindo do sistema...')
        # \n\t



