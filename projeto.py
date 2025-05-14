#primeiro dicionario (DEVE TER)
dicioVoo = {} 
#segundo dicionario (DEVE TER)
dicioCadastro = {}

#lista de cada voos (TESTE)
voo1 = ["Campinas", "São Paulo", 2, "1.000.00", "24"]
voo2 = ["São Paulo", "Campinas", 1, "1.200.00", "30"]
voo3 = ["São Paulo", "Ilhéus", 0, "1.400.00", "27"]
voo4 = ["Ilhéus", "São Paulo", 0, "1.400.00", "23"]
voo5 = ["Campinas", "Inglaterra", 2, "5.000.00", "6"]
voo6 = ["Campinas", "França", 0, "7.000.00", "15"]
voo7 = ["Campinas", "Alemanha", 1, "6.000.00", "13"]
voo8 = ["Campinas", "Russia", 2, "9.000.00", "26"]
voo9 = ["Campinas", "Japão", 3, "9.000.00", "9"]
voo10 = ["Inglaterra", "São Paulo", 0, "7.000.00", "25"]
voo11 = ["França", "São Paulo", 0, "7.000.00", "35"]
voo12 = ["Alemanha", "São Paulo", 1, "6.000.00", "2"]
voo13 = ["Russia", "São Paulo", 2, "9.000.00", "28"]
voo14 = ["Japão", "São Paulo", 3, "9.000.00", "14"]
voo15 = ["Campinas", "Brasília", 0, "1.300.00", "27"]
voo16 = ["Brasília", "Campinas", 1, "1.100.00", "12"]
voo17 = ["Campinas", "Belo Horizonte", 1, "1.000.00", "24"]
voo18 = ["Belo Horizonte", "Campinas", 0, "1.000.00", "11"]
voo19 = ["Campinas", "Estados Unidos", 0, "4.000.00", "1"]
voo20 = ["Estados Unidos", "Campinas", 0, "4.000.00", "34"]

#Lista com a lista de cada voo
listaVoo = [voo1, voo2, voo3, voo4, voo5, voo6, voo7, voo8, voo9, voo10, voo11, voo12, voo13, voo14, voo15, voo16, voo17, voo18, voo19, voo20]

#dicionario com cada voo
dicioVoo = {1: voo1, 2: voo2, 3: voo3, 4: voo4, 5: voo5, 6: voo6, 7: voo7, 8: voo8, 9: voo9, 10: voo10, 11: voo11, 12: voo12, 13: voo13, 14: voo14, 15: voo15, 16: voo16, 17: voo17, 18: voo18, 19: voo19, 20: voo20 }

#conta quantos voos tem e acrescenta 1
vooNumero = len(dicioVoo)
numeroPassageiros = len(dicioCadastro)

#lista de passageiros em cada voo (Nao confirmado se vai ter ainda)
dicioPassageiro = {}

i = len(dicioVoo)
while i > 0:
    print(i , dicioVoo.get(i))
    print("--------------------------------------------------------")
    i -= 1

#deseja cadastrar um voo? (FEITO)


#vooCriar = int(input("Deseja adicionar um voo? 1 para sim e 2 para nao"))
#if vooCriar == 1:
#    cidadeOrigem = input("Digite a cidade de origem: ")
#    cidadeDestino = input("Digite a cidade de destino: ")
#    escala = input("digite a escala: ")
#    preco = int(input("digite o preco: "))
#    capacidadeDoAviao = int(input("digite quantos lugares tem disponivel: "))

#    numerodovoo = vooNumero + 1
#    print(numerodovoo)
#    vooNumero = [cidadeOrigem, cidadeDestino, escala, preco, capacidadeDoAviao]
#    listaVoo.append(vooNumero)
#    dicioVoo.setdefault(numerodovoo, vooNumero)
#    print(dicioVoo)

#deseja consultar um voo? (FEITO)

#consultarVoo = input("Deseja consultar um voo? 1 para sim e 2 para nao: ")

#consultarCodigo = input("Deseja consultar um voo pelo codigo? 1 para sim e 2 para nao: ")
#if consultarCodigo == "1":
#   codigoVoo = int(input("Deseja consultar um voo? Digite o codigo do voo: "))
#   print(dicioVoo.get(codigoVoo))

#consultarOrigem = input("Deseja consultar um voo pela cidade de origem? 1 para sim e 2 para nao: ")
#if consultarOrigem == "1":
#   cidadeOrigem = input("Deseja consultar um voo? Digite a cidade de origem: ")
#   i = len(dicioVoo)
#   while i > 0:
#      if dicioVoo.get(i)[0].lower() == cidadeOrigem.lower():
#         print(dicioVoo.get(i))
#      i -= 1

#consultarDestino = input("Deseja consultar um voo pela cidade de destino? 1 para sim e 2 para nao: ")
#if consultarDestino == "1":
#   cidadeDestino = input("Deseja consultar um voo? Digite a cidade de destino: ")
#   i = len(dicioVoo)
#   while i > 0:
#      if dicioVoo.get(i)[1].lower() == cidadeDestino.lower():
#         print(dicioVoo.get(i))
#      i -= 1

#Deseja saber o voo com menor escala? (FEITO)

#origemProcurar = input("qual cidade de origem deseja procurar? ")
#destinoProcurar = input("qual cidade de destino deseja procurar? ")

#i = len(dicioVoo)
#guardar = 9999
#while i > 0:
#   if dicioVoo.get(i)[0].lower() == origemProcurar.lower() and dicioVoo.get(i)[1].lower() == destinoProcurar.lower():
#      if dicioVoo.get(i)[2] < guardar:
#         guardar = dicioVoo.get(i)
#      print(guardar)
#   i = i - 1
      
#Deseja saber os passageiros de um voo?

numeroVoo = input("Deseja consultar os passageiros de um voo? Digite o numero do voo: ")
print(dicioPassageiro.get(numeroVoo))

#Deseja comprar uma passagem? (FEITO)


comprarPassagem = input("Deseja comprar uma passagem? 1 para sim e 2 para não: ")
if comprarPassagem == '1':
    dadoscadastro = []
    cpf = input('Digite o CPF : ')
    if cpf in dicioCadastro.keys():
        while cpf in dicioCadastro.keys():
            print('CPF já existe')
            cpf = input('Digite outro CPF : ')
    else:
        nome = input('Digite o nome : ')
        idade = input('Digite a idade : ')
        telefone = input('Digite o telefone : ')
        dadoscadastro.append(nome)
        dadoscadastro.append(idade)
        dadoscadastro.append(telefone)
        dicioCadastro.setdefault(cpf,dadoscadastro)

    numPassageiros = numeroPassageiros - 1

    comprarPassagem = input("Qual passagem deseja comprar? Digite o codigo que aparece na frente da passagem: ")
    dicioPassageiro.setdefault(cpf, listaVoo[int(comprarPassagem) - 1])
    print(dicioPassageiro)


#Deseja cancelar uma passagem?