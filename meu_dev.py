# voos = {'01': cid}
# vooNumero = [cidadeOrigem, cidadeDestino, escala, preco, capacidadeDoAviao]
# voos = {"01": { "origem": "São Paulo", "destino": "Rio de Janeiro",  "escalas": 1,    "preco": 300.0,    "lugares_disponiveis": 5, "passageiros": [] }

# part 1

print('\n\t---------- MENU DO SISTEMA ----------')
print('\n\t[1] Cadastrar um Voo')
print('\t[2] Consultar um Voo')
print('\t[3] Verificar Voo com menor escala')
print('\t[4] Listar passageiros de um Voo')
print('\t[5] Compra de passagem')
print('\t[6] Cancelar uma passagem')
option = int(input('\n\tDigite uma opção: '))
while option not in [1, 2, 3, 4, 5, 6]:
    print("\n\tOpção inválida !")
    option = int(input('\n\tDigite uma opção: '))

# part 2      
      
if option == 1:
    print('\n------------------------------------------------------------------')
    print('\n\tOpção cadastrar Voo escolhida...')
    print('\n------------------------------------------------------------------')
    voos = {}
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
            "Preco": preco,
            "Lugares disponiveis": capacidade,
            "Passageiros": []
        } 
        print(f'\n\tVoo "{codigo}" cadastrado com sucesso!')

        cad = input('\n\tCadastrar mais voos? "S" para sim "N" para não: ').upper()
        while cad.upper() != "S" and cad.upper() != "N":
            print("\n\tOpção inválida !")
            cad = input('\n\tCadastrar mais voos? "S" para sim "N" para não: ').upper()

    # \n\t



