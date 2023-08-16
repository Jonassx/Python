nome=input("Digite o nome: ")
idade= int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?").upper()

if idade>=65:
    print("O paciente " + nome + "POSSUI prioridade no atendimento")
elif doenca_infectocontagiosa=="SIM":
    print("O paciente " + nome + "deve ser transferido para a sala reservada")
else:
    print("O pacinete " + nome + "NÃO POSSUI prioridade no atendimento e deve aguardar na sala comum!")

# .upper() = é uma função que tem por finalidade converter o conteúdo de uma string para letras maiusculas.
# Um "=" representa atribuição, dois "==" representam comparação.
# Dessa forma, o "else" somente será executado se a primeira e a segunda condição forem falsas.
