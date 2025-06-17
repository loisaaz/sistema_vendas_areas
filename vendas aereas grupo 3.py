def cadastrarVoo(dicioVoo, listaVoo, proximaLista):
        
    cidadeOrigem = input("Digite a cidade de origem: ")
    cidadeDestino = input("Digite a cidade de destino: ")
    escala = int(input("Digite quantas escalas têm o voo: "))
    preco = int(input("Digite o preço do voo: "))
    capacidadeDoAviao = int(input("Digite quantos lugares têm disponível: "))

    vooNumero = len(dicioVoo)
    if vooNumero != 0:
        proximaLista = vooNumero

    vooNumero = [cidadeOrigem, cidadeDestino, escala, preco, capacidadeDoAviao]
    listaVoo.append(vooNumero)
    dicioVoo.setdefault(proximaLista, vooNumero)

    i = len(dicioVoo)
    while i > 0:
        print(i - 1, dicioVoo.get(i - 1))
        print("--------------------------------------------------------")
        i -= 1


def consultarVoo(dicioVoo):
    if len(dicioVoo) == 0:
        print("Não há voos cadastrados")

    consultarCodigo = "n"
    consultarOrigem = "n"
    consultarDestino = "n"

    consultarDestino = 0
    consultarDestino = 0
    consultarOrigem = 0

    consultarCodigo = input("Deseja consultar um voo pelo código? Digite S ou N: ")
    while consultarCodigo.lower() != "n":
        if consultarCodigo.lower() != "s" and consultarCodigo.lower() != "n":
            while consultarCodigo.lower() != "s" and consultarCodigo.lower() != "n":
                print("Opcão inválida")
                consultarCodigo = input("Deseja consultar um voo pelo código? Digite S ou N: ")


        if consultarCodigo.lower() == "s":
            codigoVoo = int(input("Digite o código do voo: "))
            if codigoVoo in dicioVoo.keys():
                print(dicioVoo.get(codigoVoo))
                consultarCodigo = "n"
                consultarOrigem = "n"
                consultarDestino = "n"
            else:
                print("Código de voo não encontrado")
        

    if consultarDestino != "n":

        consultarOrigem = input("Deseja consultar um voo pela cidade de origem? Digite S ou N: ")
        while consultarOrigem.lower() != "n":
            if consultarOrigem.lower() != "s" and consultarOrigem.lower() != "n":
                while consultarOrigem.lower() != "s" and consultarOrigem.lower() != "n":
                    print("Opcão inválida")
                    consultarOrigem = input("Deseja consultar um voo pela cidade de origem? Digite S ou N: ")

            if consultarOrigem == "s":
                cidadeOrigem = input("Digite a cidade de origem: ")

                i = len(dicioVoo)
                aux = 0
                achou = 0
                while i > aux:
                    if dicioVoo.get(aux)[0].lower() == cidadeOrigem.lower():
                        print(dicioVoo.get(aux))
                        consultarCodigo = "n"
                        consultarOrigem = "n"
                        consultarDestino = "n"
                        achou += 1
                    aux += 1

                if aux == i and achou == 0:
                    print("Cidade de origem não encontrada")
                else:
                    consultarOrigem = "n"


        if consultarDestino != "n":
            consultarDestino = input("Deseja consultar um voo pela cidade de destino? Digite S ou N: ")
            while consultarDestino.lower() != "n":
                if consultarDestino.lower() != "s" and consultarDestino.lower() != "n":
                    while consultarDestino.lower() != "s" and consultarDestino.lower() != "n":
                        print("Opcão inválida")
                        consultarDestino = input("Deseja consultar um voo pela cidade de destino? Digite S ou N: ")

                if consultarDestino == "s":
                    cidadeDestino = input("Digite a cidade de destino: ")

                i = len(dicioVoo)
                aux = 0
                achou = 0
                while i > aux:
                    if dicioVoo.get(aux)[1].lower() == cidadeDestino.lower():
                        print(dicioVoo.get(aux))
                        achou += 1
                    aux += 1
                if aux == i and achou == 0:
                    print("Cidade de destino não encontrada")
                else:
                    consultarDestino = "n"


def menorEscala(dicioVoo):
    origemProcurar = 0
    destinoProcurar = 0

    menorEscala = 9999
    i = len(dicioVoo)
    aux = 0
    if i == 0:
        print(f"Não há voos cadastrados")
        menorEscala = "n"

    if i != 0:
        origemProcurar = input("Qual cidade de origem deseja procurar? ")
        destinoProcurar = input("Qual cidade de destino deseja procurar? ")
    
    while i > aux:
        if dicioVoo.get(aux)[0].lower() == origemProcurar.lower() and dicioVoo.get(aux)[1].lower() == destinoProcurar.lower():
            if dicioVoo.get(aux)[2] < menorEscala:
                menorEscala = dicioVoo.get(aux)
                print(menorEscala)
        else:
            print(f"Não há voos cadastrados que sai de {origemProcurar} para {destinoProcurar}")
        aux += 1


def comprarPassagem(dicioVoo, dicioPassageiro, dicioCadastro):
    dadoscadastro = []
    cpf = input('Digite o CPF : ').replace(".","").replace("-","")
    if cpf in dicioCadastro.keys():
        listaCpfVoo = []
        listaCpfVoo.append(dicioPassageiro.get(cpf))
        pgt1 = 'n'
        while cpf in dicioCadastro.keys() and pgt1.lower() != 's':
            print('CPF já existe')
            pgt1 = input('Deseja comprar uma passagem com este CPF? Digite S ou N: ')
            if pgt1.lower() == 's':
                qualPassagemComprar = int(input("Qual passagem deseja comprar? Digite o código que aparece na frente da passagem: "))


                dicioPassageiro[cpf].append(qualPassagemComprar)
                print(dicioPassageiro)
            else:
                print("Passagem não comprada")
    else:
        nome = input('Digite o nome : ')
        idade = int(input('Digite a idade : '))
        telefone = int(input('Digite o telefone : '))

        qualPassagemComprar = int(input("Qual passagem deseja comprar? Digite o código que aparece na frente da passagem: "))
        if qualPassagemComprar > len(dicioVoo) or qualPassagemComprar not in dicioVoo.keys():
            print("Essa passagem não existe")
        else:

            listaCpfVoo = []
            listaCpfVoo.append(qualPassagemComprar)
            dicioPassageiro.setdefault(cpf, listaCpfVoo)
            dadoscadastro.append(nome)
            dadoscadastro.append(idade)
            dadoscadastro.append(telefone)
            dicioCadastro.setdefault(cpf,dadoscadastro)
            print(dicioCadastro)
            print(dicioPassageiro)
            print("Passagem comprada com sucesso!")

            listaCpfVoo = []


def passageirosVoo(dicioVoo, dicioPassageiro, dicioCadastro):
    numeroVoo = int(input("Digite o número do voo: "))
    comparar = dicioVoo.get(numeroVoo)
    print("--------------------------------------------------------")
    print("")
    print("Passageiros inclusos no voo: ")
    for key, value in dicioPassageiro.items():
        i = len(value)
        aux = 0
        x = 0
        while i > aux:
            if comparar == dicioVoo.get(value[aux]):
                print("Passageiro ", dicioCadastro.get(key)[0],"está abordo, possui", dicioCadastro.get(key)[1], "ano(s) de idade e seu telefone é", dicioCadastro.get(key)[2])
                x = 1
            aux += 1
        
        aux = 0

    if x == 0:
        print("Não há passageiros para esse voo")


def cancelarPassagem(dicioPassageiro, dicioVoo):
    negativo = 0
    while negativo == 0:
        cpf = input('Digite o CPF : ').replace(".","").replace("-","")
        if cpf not in dicioPassageiro.keys():
            print("CPF não encontrado")
            negativo = 1
            continue

        i = len(dicioPassageiro[cpf])
        aux = 0
        print("Passagens que você tem: ")
        while i > aux:
            print("Passagem de código", dicioPassageiro[cpf][aux])
            aux += 1
        if cpf in dicioPassageiro.keys():
            print('Qual o código da passagem que deseja cancelar? ')
            codigodapassagem = int(input('Digite o código: '))
            if codigodapassagem in dicioPassageiro[cpf]:
                print('Passagem encontrada:')
            else:
                print('Passagem não encontrada!')
                continue
            i = len(dicioPassageiro)
            while i > 0:  
                if codigodapassagem in dicioPassageiro[cpf]:
                    dicioPassageiro[cpf].pop(codigodapassagem)
                i -= 1

            print(dicioVoo.get(codigodapassagem))
            print("")
            print(dicioCadastro.get(cpf)[0], "sua passagem foi cancelada com sucesso!")

            negativo = 1


dicioVoo = {} 
dicioCadastro = {}
dicioPassageiro = {}

listaVoo = []
listaCpfVoo = []

proximaLista = 0


Sistema_funcionando = 10
while Sistema_funcionando > 0:
    print("\n\n\n-------------------Sistema de Passagens Aéreas-------------------\n")
    print("O que deseja fazer?")
    print("\tDigite 1 para cadastrar um voo")
    print("\tDigite 2 para consultar um voo")
    print("\tDigite 3 para saber o voo com menor escala")
    print("\tDigite 4 para comprar uma passagem")
    print("\tDigite 5 para saber quantos passageiros tem um voo")
    print("\tDigite 6 para cancelar uma passagem")
    print("\tDigite 7 para sair do sistema")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        cadastrarVoo(dicioVoo, listaVoo, proximaLista)
    elif opcao == 2:
        consultarVoo(dicioVoo)
    elif opcao == 3:
        menorEscala(dicioVoo)
    elif opcao == 4:
        comprarPassagem(dicioVoo, dicioPassageiro, dicioCadastro)
    elif opcao == 5:
        passageirosVoo(dicioVoo, dicioPassageiro, dicioCadastro)
    elif opcao == 6:
        cancelarPassagem(dicioPassageiro, dicioVoo)
    elif opcao == 7:
        print("-------------------Sistema de Passagens Aéreas Fechando-------------------")
        Sistema_funcionando = -1
        dicioVoo.clear()
        dicioCadastro.clear()
        listaVoo.clear()
    else:
        print("Número inválido!")
