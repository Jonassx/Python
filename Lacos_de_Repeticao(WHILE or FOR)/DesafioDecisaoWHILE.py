reposta="SIM"
while reposta=="SIM":
    nivel=input("Qual o seu Nível?").upper()
    if nivel=="USR" or nivel=="ADM":
        genero=input("Qual o genero? ").upper()
        if nivel=="USR":
            if genero=="FEMININO":
                print("Olá Usuária")
            else:
                print("Olá Usuário")
        else:
            if genero=="FEMININO":
                print("Olá Administradora")
            else:
                print("Olá Administrador")
    elif nivel=="GUEST":
        print("Olá visitante")
    else:
        print("Olá desconhecido(a)")