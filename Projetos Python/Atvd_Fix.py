#Atividade de Fixação
print('Cadastro de Cidades')
cidade_cheia = ""
populacao_maior = 0
soma = 0
contador = 0

while True:
    cidade = input('\nDigite o nome da sua cidade: ') .strip()
    populacao = input('Digite a população estimada da sua cidade: ') .strip()

    if populacao.isdigit():
        populacao = int(populacao)

    else:
        print('Informação Invalida, digite apenas numeros.')
        continue


    contador += 1
    soma += populacao
    
    if populacao > populacao_maior:
        populacao_maior = populacao
        cidade_cheia = cidade


    continuar = input("Deseja cadastrar outra pessoa? (S/N): ").strip().upper()
    if continuar != 'S':
        break

print("\n--- Resultados ---")
print(f"Total de cidades cadastradas: {contador}")
print(f"Média da população das cidades Cadastradas: {soma/contador:.1f}")
print(f"Cidade mais populosa cadastrada: {cidade_cheia} ({populacao_maior})")