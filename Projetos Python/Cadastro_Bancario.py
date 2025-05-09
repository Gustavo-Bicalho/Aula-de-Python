#Cadastro Bancario Simples
def main():
    nome_banco = ""
    nome = ""
    conta = ""
    opcao = 0

    while True:
        print("___________________________________")
        print("Bem Vindo(a) ao Banco", nome_banco)
        print("1-Cadastrar seu Banco")
        print("2-Cadastrar seu Nome")
        print("3-Ver dados cadastrados")
        print("4-Sair do Sistema")
        print("___________________________________")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            nome_banco = input("Digite o nome do seu Banco: ")
            print("Dados Cadastrados com Sucesso!")
        elif opcao == 2:
            nome = input("Digite o seu Nome: ")
            conta = input("Digite o tipo da sua conta (Corrente ou Poupança): ")
            print("Cadastro Confirmado")

        elif opcao == 3:
            if nome == "" or conta == "" or nome_banco == "":
                print("Nenhum dados cadastrado")
            else:
                print(f"Banco:{nome_banco}")
                print(f"Nome:{nome}")
                print(f"Conta:{conta}")

        elif opcao == 4:
            print("Encerrando o Sistema...")
            break
        else:
            print("Opção Inválida")


if __name__=="__main__":
    main()