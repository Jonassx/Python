nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_contagiosa=input("Suspeita de doenca contagiosa?: ").upper()

if idade >= 65:
    print("Paciente COM PRIORIDADE")
    if doenca_contagiosa=="SIM":
        print("Encaminhe o paciente para a ZONA AMARELA")
    elif doenca_contagiosa=="NÃO":
        print("Encaminhe o paciente pra a ZONA BRANCA")
    else:
        print("Responda a suspeita de doneça contagiosa com SIM ou NÃO")

else:
    print("Paciente SEM PRIORIDADE")
    if doenca_contagiosa=="SIM":
        print("Encaminhe o paciente para a zona AMARELA")
    elif doenca_contagiosa=="NÃO":
        print("Encaminhe o paciente para a zona BRANCA")
    else:
        print("Responda a suspeita de doneça contagiosa com SIM ou NÃO")