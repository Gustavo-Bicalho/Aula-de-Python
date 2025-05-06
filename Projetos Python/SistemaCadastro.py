#Desafio
def main():
    nome = ""
    idade = 0
    opção = 0
    while True:
        print("_____________________")
        print("Bem vindo(a) ao Guz OS")
        print("1.Cadastrar usuário")
        print("2.Ver dados cadastrados")
        print("3.Sair do Sistema")
        print("_____________________")
        opção = int(input("Escolha uma opção: "))
        if opção == 1:
            nome = input("Digite o seu nome: ")
            idade = int(input("Digite sua idade: "))
            print("Dados Cadastrados com Sucesso!")
        elif opção == 2:
            if nome == "" or idade == 0:
                print("Nenhum dados cadastrados.")
            else:
                print("Dados Cadastrados com Sucesso!")
                print(f"Nome:{nome}")
                print(f"Idade:{idade}")
        elif opção == 3:
            print("Encerrando o Sistema...")
            break
        else:
            print("Opção Inválida")


if __name__=="__main__":
    main()
