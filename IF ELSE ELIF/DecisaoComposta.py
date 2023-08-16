nome=input("Digite o seu nome: ")
idade= int(input("Digite a sua idade: "))
prioridade= "NÃO"

if idade >= 65:
    print("O paciente " + nome + " POSSUI PRIORIDADE NO ATENDIMENTO")

else:
    print("O paciente " + nome + " NÃO POSSUI PRIORIDADE NO ATENDIMENTO")

# if <condicao>:
#   <o que voce quer que aconteça caso a condição seja verdadeira>
# A linha 5 do if deve ser encerrada com  dois ponto (:).
# As linhas a ser executada, caso a condição seja verdadeita, deverá estar com recuo de espaço 