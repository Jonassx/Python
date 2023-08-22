import customtkinter as ctk

janela = ctk.CTk() 
janela.title("Automação Diretórios")
janela.geometry("600x400")
janela._set_appearance_mode("dark")

def button_new_pressed():
    window_button_new_query = ctk.CTk()
    window_button_new_query.geometry("350x160")
    window_button_new_query.title("Selecione o tipo de preparação")

    #Criação dos botões para o usuário selecionar o tipo de preparação

    btn_conversao = ctk.CTkButton(master=window_button_new_query, text="1 - CONVERSÃO DE DADOS")
    btn_expimp = ctk.CTkButton(master=window_button_new_query, text="2 - EXPORTA/IMPORTA")
    btn_conversaoxml = ctk.CTkButton(master=window_button_new_query, text="3 - CONVERSÃO DE XML")

    btn_conversao.grid(row=0, column=0, padx=10, pady=10)
    btn_expimp.grid(row=1, column=0, padx=10, pady=10)
    btn_conversaoxml.grid(row=2, column=0, pady=10)

    window_button_new_query.mainloop()

button_new = ctk.CTkButton(master=janela, text="SELECIONAR TIPO", command=button_new_pressed)
button_new.pack()



janela.mainloop()