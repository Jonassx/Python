#def <identificador da funcao> (<parametro(s)>):
	#<código que será executado>
	#return <Dado que será retornado, caso seja necessário>

# O <identificador da função> deve seguir as mesmas regras e padronizações dos identificadores das variáveis e listas.
# O <parametro> é um dado que será fornecido para que a função possa executar o seu bloco de código.
# O código a ser executado representa o conjunto de códigos que possuem uma mesma finalidade dentro da aplicação.
# O "return" é opcional e deve ser usada somente quando voce desejar que a função retorne um valor para o módulo principal.

def preencherInventario(lista ):
  resposta="S"
  while resposta == "S":
    equipamento=[input("Equipamento: "),
              float(input("Valor: ")),
              int(input("Número Serial: ")),
              input("Departamento: ")]
    lista.append(equipamento)
    resposta = input("Digite 'S' para continuar: ").upper()

    # Esta função preenche um inventário com as informações inseridas pelo usuário.
    # A função começa pedindo ao usuário para inserir o nome do equipamento.
    # Em seguida, a função pede ao usuário para inserir o valor do equipamento.
    # Em seguida, a função pede ao usuário para inserir o número serial do equipamento.
    # Em seguida, a função pede ao usuário para inserir o departamento do equipamento.
    # A função então adiciona as informações inseridas pelo usuário à lista `lista`.
    # Finalmente, a função pede ao usuário para digitar `S` para continuar preenchendo o inventário, ou `N` para parar.

def exibirInventario(lista):
  for elemento in lista:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

    # Esta função exibe o inventário para o usuário.
    # A função itera sobre a lista `lista` e imprime as informações de cada equipamento.

def localizarPorNome(lista):
  busca=input("Digite o nome do equipamento que deseja buscar: ")
  for elemento in lista:
    if busca==elemento[0]:
      print("Valor..: ", elemento[1])
      print("Serial.:", elemento[2])

    # Esta função localiza um equipamento no inventário pelo seu nome.
    # A função pede ao usuário para inserir o nome do equipamento que deseja localizar.
    # A função itera então sobre a lista `lista` e verifica se o nome do equipamento inserido está na lista.
    # Se o nome do equipamento estiver na lista, a função imprime as informações do equipamento.

def depreciarPorNome(lista, porc):
  depreciacao=input("Digite o nome do equipamento que será depreciado: ")
  for elemento in lista:
    if depreciacao==elemento[0]:
      print("Valor antigo: ", elemento[1])
      elemento[1] = elemento[1] * (1-porc/100)
      print("Novo valor: ", elemento[1])

    # Esta função deprecia um equipamento no inventário pelo seu nome.
    # A função pede ao usuário para inserir o nome do equipamento que será depreciado.
    # A função itera então sobre a lista `lista` e verifica se o nome do equipamento inserido está na lista.
    # Se o nome do equipamento estiver na lista, a função imprime o valor antigo do equipamento e o novo valor do equipamento, que é calculado depreciando o valor antigo do equipamento pela porcentagem inserida pelo usuário.
