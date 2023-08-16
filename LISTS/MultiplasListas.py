equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
  equipamentos.append(input("Equipamento: ").upper())
  valores.append(float(input("Valor: ").upper()))
  seriais.append(int(input("Número Serial: ").upper()))
  departamentos.append(input("Departamento: ").upper())
  resposta = input("Digite 'S' para continuar: ").upper()

for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])

busca=input("Digite o nome do equipamento que deseja buscar: ").upper()
for indice in range (0, len(equipamentos)):
  if busca==equipamentos[indice]:
    print("Valor..: ", valores[indice])
    print("Serial..: ", seriais[indice])
# Será atribuido o valor de 0 até a quantidade de elementos que existirem dentro da nossa lista "equipamentos" (função "len()").
