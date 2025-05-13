#Cadastro Alunos
avs = []
for i in range(5):
    nome = input("Digite seu nome: ")

    av_um = float(input("Digite sua primeira nota: "))
    av_dois = float(input("Digite sua segunda nota: "))

    media = (av_um + av_dois) / 2
    avs.append({

        "nome": nome,
        "AV1": av_um,
        "AV2": av_dois,
        "média": media
    })
    
    print("\n--- Resultado Final ---")

    for av in avs:
        print(f"{av['nome']} - AV1: {av['AV1']} | AV2:{av['AV2']} | média: {av['média']:.2f}")