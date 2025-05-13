comissoes = []

for i in range(1):
    nome = input("Digite o nome do funcionario: ")
    comissaoum = float(input("Digite a sua comissão no primeiro mês: "))
    comissaodois = float(input("Digite a sua comissão no segundo mês: "))

    media = (comissaoum + comissaodois) / 2
    comissoes.append({
        "nome": nome,
        "Comissão 1": comissaoum,
        "Comissão 2": comissaodois,
        "média": media
    })
    print("\n--- Resultado Final ---")

    for comissao in comissoes:
        print(f"{comissao['nome']} - Comissão 1: {comissao['Comissão 1']} | Comissão 2:{comissao['Comissão 2']} | Média: {comissao['média']:.2f}")