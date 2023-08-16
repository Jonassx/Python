inventario=[]
resposta = "S"

#Adicionar item no inventario
while resposta == "S":
  equipamento=[
            input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            input("Departamento: ")]
  inventario.append(equipamento)
  resposta = input("Digite 'S' para continuar: ").upper()

#Exibir dados do inventário

for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

#Localizar um item no inventario

busca=input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
  if busca==elemento[0]:
    print("Valor..: ", elemento[1])
    print("Serial.:", elemento[2])

# Excluir um item do inventario

depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
  if depreciacao==elemento[0]:
    print("Valor antigo: ", elemento[1])
    elemento[1] = elemento[1] * 0.9
    print("Novo valor: ", elemento[1])

#exibir dados do inventario

serial=int(input("Digite o serial do equipamento que será excluído: "))
for elemento in inventario:
  if elemento[2]==serial:
    inventario.remove(elemento)

for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

  #resumo de valores do inventário

  valores = []
  for elemento in inventario:
      valores.append(elemento[1])
  if len(valores) > 0:
      print("O equipamento mais caro custa: ", max(valores)) # max() Retorna o maior valor numérico dentre os elementos da lista;
      print("O equipamento mais barato custa: ", min(valores)) # min() Retorna o menor valor numérico dentre os elementos da lista;
      print("O total de equipamentos é de: ", sum(valores)) # sum() Retorna o valor totatl entre os elementos da lista.



