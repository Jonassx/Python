inventario=[]
resposta="S"
while resposta=="S":
  inventario.append(input("Equipamento: "))
  inventario.append(float(input("Valor: ")))
  inventario.append(int(input("Número Serial: ")))
  inventario.append(input("Departamento: "))
  resposta=input("Digite 'S' para continuar: ").upper()

  for elemento in inventario:
      print(elemento)

  # No codigo acima, utilizamos o "while", que será responsável por seguir adicionando dados para a noss lista "inventario" enquanto o usuário digitar "S".
  # Perceba no código que utilizamos o método append() para adicionar novos itens em nossa lista. podemos afirmar que a cada passagem dentro do "while", quatro novos dados serão adiiconados na lista.
  # Utilizamos o "for" por que ele é o mais indicado para percorrermos a lista e exibirmos tudo o que estpa armazenado nela.

