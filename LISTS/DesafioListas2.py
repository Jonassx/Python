departamentos=[]
equipamentos=[]
seriais=[]
valores=[]
resposta="S"

while resposta=="S":
  departamentos.append(input("Departamento: "))
  equipamentos.append(input("Equipamento: "))
  seriais.append(int(input("Serial: ")))
  valores.append(float(input("Valor: ")))
  resposta = input("Digite 'S' para continuar...")

serial=int(input("Digite o serial do equipamento que será excluido: "))
for indice in range(0, len(departamentos)):
  if seriais[indice]==serial:
    del departamentos[indice]
    del equipamentos[indice]
    del seriais[indice]
    del valores[indice]
    break

for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])

