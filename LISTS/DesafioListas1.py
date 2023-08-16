#Todos os equipamentos "impressora" receberão uma depreciação (desvalorização após certo período) de 10%. Monte o código que seria responsável por alterar o valor de todos os equipmentos "impressora".

depreciacao = input("Digite o nome do equipamento que será depreciado: ")

for indice in range(0, len(equipamentos)):
  if depreciacao == equipamentos[indice]:
    print("Valor antigo: ", valores[indice])
    valores[indice] = valores[indice] * 0.9
    print("Novo valor: ", valores[indice])


