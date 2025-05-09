#Sistema Bancario
def main():
    nome_banco = ""
    nome = ""
    opcao = 0

    while True:
        print("___________________________________")
        print("Bem Vindo(a) ao Banco", nome_banco)
        print("1-Cadastrar seu Banco")
        print("2-Cadastrar seu Nome")
        print("3-Sair do Sistema")
        print("___________________________________")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            nome_banco = input("Digite o nome do seu Banco: ")
            print("Dados Cadastrados com Sucesso!")
        elif opcao == 2:
            nome = input("Digite o seu Nome: ")
            print("Cadastro Confirmado")
          
        elif opcao == 3:
            print("Encerrando o Sistema...")
            break
        else:
            print("Opção Inválida")


if __name__=="__main__":
    main()