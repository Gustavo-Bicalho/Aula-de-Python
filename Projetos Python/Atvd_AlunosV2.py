#Cadastro Alunos
avs = []
for i in range(5):
    nome = input("Digite seu nome: ")

    av_um = float(input("Digite sua primeira nota: "))
    av_dois = float(input("Digite sua segunda nota: "))

    media = (av_um + av_dois) / 2
    avs.append([nome, av_um, av_dois, media])

    
    print("\n--- Resultado Final ---")

    for av in avs:
        print(f"{av[0]} - AV1: {av[1]} | AV2:{av[2]} | média: {av[3]:.2f}")