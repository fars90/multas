def localidade():
    velocidade = int(input("Introduza a Velocidade do Veículo (em km/h): "))
    print()
    if velocidade >= 120:
        print("A multa é de 320€ !\n")
    elif velocidade >= 90:
        print("A multa é de 120€ !\n")
    elif velocidade > 50:
        print("A multa é de 60€ !\n")
    else:
        print("Não estava em excesso de velocidade!\n")

def fora_localidade():
    velocidade = int(input("Introduza a Velocidade do Veículo (em km/h): "))
    print()
    if velocidade >= 120:
        print("A multa é de 120€ !\n")
    elif velocidade > 90:
        print("A multa é de 60€ !\n")
    else:
        print("Não estava em excesso de velocidade!\n")

def autoestrada():
    velocidade = int(input("Introduza a Velocidade do Veículo (em km/h): "))
    print()
    if velocidade > 175:
        print("A multa é de 360€ !\n")
    elif velocidade > 150:
        print("A multa é de 120€ !\n")
    elif velocidade > 120:
        print("A multa é de 60€ !\n")
    else:
        print("Não estava em excesso de velocidade!\n")
    
while True:
    print(" ---------- ")
    print("|Bem Vindo!|")
    print(" ---------- ")
    print("Onde circulava o veículo?")
    print("Escolha uma opção: ")
    print("1 - Localidade")
    print("2 - Fora da Localidade")
    print("3 - Autoestrada")
    print("0 - Sair")
    print()
   
    opcao = input("Opção: ")
    print()
    
    if opcao == "1":
        localidade()
    elif opcao == "2":
        fora_localidade()
    elif opcao == "3":
        autoestrada()
    elif opcao == "0":
        print("Obrigado!")
        break
    else:
        print("Opção invalida!")