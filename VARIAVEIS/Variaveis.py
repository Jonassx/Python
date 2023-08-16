nome="Humberto Delgado"
empresa='FIAP'
qtde_funcionarios=500
mediaMensalidade=865.50

nome=input("Digite um funcionário: ")
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a qtde de funcionários: "))
mediaMensalidade=float(input("Digite a média da mensalidade: "))

# Variavel + dado
# Nas linhas 1 e 2, criamos variáveis do tipo String, ou seja, o conteudo de uma variavel string deve estar entre aspas duplas (") ou entre aspas simples (').
# Na linha 3, criamos uma variável do tipo int
# Na linha 4, criamos uma variavel do tipo float. O caractere utilizado para casas decimais é o ponto(.), seguindo padrão americcano, ou seja, vírgula separa casas de milhar e ponto separa casas decimais.

print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, "funcionarios")
print("A média da mensalidade é de: " + str(mediaMensalidade))

# Na linha 11, exibimos o valor das duas primeiras variaveis, separadas por um texto; para unir o conteudo delas, utilizamos o operador "+", que representa concatenação/função para string's.
# Na linha 12, onde estamos exibindo a variavel inteira e dois textos, utilizamos a "virgula" para inidicar o final do primeiro texto, a variavel e o inicio do segundo texto, sem precisar converter a variavel numerica para string.
# Na linha 13, exibimos um texto e uma verivel do tipo "float", concatenadas atraves do operador "+". Para que o python nao tente realizar uma operação matemática, devemos utilizar a função str() para converter o conteudo da varivel "float" para string, por isso a varivavel mediaMensailidade está dentro da função str().

print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))

