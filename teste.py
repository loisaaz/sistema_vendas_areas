# Dicionário de Voos
voos = {
    "01": {
        "origem": "São Paulo",
        "destino": "Rio de Janeiro",
        "escalas": 1,
        "preco": 300.0,
        "lugares_disponiveis": 5,
        "passageiros": []
    },
    "02": {
        "origem": "Belo Horizonte",
        "destino": "Salvador",
        "escalas": 0,
        "preco": 450.0,
        "lugares_disponiveis": 3,
        "passageiros": []
    }
}

# Dicionário de Passageiros
passageiros = {
    "12345678900": {
        "nome": "Maria Oliveira",
        "telefone": "11999999999",
        "passagens": ["01"]
    },
    "98765432100": {
        "nome": "João Silva",
        "telefone": "21988888888",
        "passagens": ["02"]
    }
}

# Visualização simples (só para testar)
print("Voos cadastrados:")
for codigo, dados in voos.items():
    print(f"\nVoo {codigo}:")
    for chave, valor in dados.items():
        print(f"  {chave}: {valor}")

print("\nPassageiros cadastrados:")
for cpf, dados in passageiros.items():
    print(f"\nCPF {cpf}:")
    for chave, valor in dados.items():
        print(f"  {chave}: {valor}")
