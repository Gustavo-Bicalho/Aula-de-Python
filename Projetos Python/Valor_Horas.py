#Chamando a função
def pagamento():


    for i in range(1):
        print("______________________________________________________________")
        print("Sistema de Pagamento")
        print("                                                              ")
        horas = float(input("Digite o numero de horas trabalhadas por dia: "))
        valor = float(input("Digite o valor pago por hora trabalhada: "))
        dias = int(input("Digite o numero de dias trabalhados: "))
        resultado = (horas*valor)* dias
        print("O valor a ser pago sera: ",resultado, "R$")
        print("                                                              ")
        print("______________________________________________________________")





   
#Fechando a função
pagamento()
    