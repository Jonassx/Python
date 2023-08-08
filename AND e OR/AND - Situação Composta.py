paciente=input("Digite o nome do paciente: ")
idade=int(input("Digite a idade: "))
doenca_contagiosa=input("Suspeita de doença contagiosa? SIM ou NÃO: ").upper()

if idade >= 65 and doenca_contagiosa=="SIM":
    print("O paciente " + paciente + " será encaminhado para a zona AMARELA - COM PRIORIDADE")
elif idade <65 and doenca_contagiosa=="SIM":
    print("O paciente " + paciente + " será encaminhado para a zona AMARELA - SEM PRIORIDADE")
elif idade <65 and doenca_contagiosa=="NÃO":
    print("O paciente " + paciente + " será encaminhado para a zona BRANCA - SEM PRIORIDADE")
elif idade >= 65 and doenca_contagiosa == "NÃO":
    print("O paciente " + paciente + " será encaminhado para a zona BRANCA - COM PRIORIDADE")
else:
    print("Responda a suspeita de doneça contagiosa com SIM ou NÃO")


## Quando utilizamos o operador "AND", queremos dizer que a condição que estiver a direita do operador devem ser verdadeiras para que o "if" seja considerado Verdadeiro. Se uma das condições retornarem Falso, o "if" irá reotrnar Falso.
## Já o operador "OR" determina que se uma das condições for verdadeira, o "if" já deverá retornar "Verdadeiro".

##Da forma como está o código acima, fechamos todas as possibilidade e o "else:" será executado somente se o usuário final digital algo diferente de "SIM" ou "NÃO", uma vez que a idade. pelo fato de ser numérica, está cercada e não ha precisão de uma udade inválida.
