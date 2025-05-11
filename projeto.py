dicioCadastro = {}
x=0
while x > 0 :
    dadoscadastro = []
    cpf = input('Digite o CPF : ')
    if cpf in dicioCadastro.keys() :
        print('CPF jรก existe')
    else:
        nome = input('Digite o nome : ')
        idade = input('Digite a idade : ')
        telefone = input('Digite o telefone : ')
        dadoscadastro.append(nome)
        dadoscadastro.append(idade)
        dadoscadastro.append(telefone)
        dicioCadastro.setdefault(cpf,dadoscadastro)
        
        
        x+=1
print(dadoscadastro)
print(dicioCadastro)