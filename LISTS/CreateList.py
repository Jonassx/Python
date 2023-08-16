#lista preenchida estaticamente
lista_estatica = ["xpto", True]

#lista preenchida dinamicamente
lista_dinamica = [input("Digite o usuário: "), bool(int(input("Está logado? ")))]

#lista vazia
lista_vazia=[]

# Para utilizar "Listas", os valores devem estar entre colchetes "[ ]", mesmo quando a lista for declarada vazia.
#1. No exemplo da lista dinamica, o segundo item está passando por duas conversões. Isso ocorre porque desejamos um dado do tipo "boolean", ou seja, um dado booleano que pode possuir apenas os valores "True" ou "False".
#1.1 Como o input retorna uma string, devemos converter o dados para int(inteiro) para então, converte-lo para bool(booleano).
#1.2 Não podemos fazer a conversão direta de string para o bool.
