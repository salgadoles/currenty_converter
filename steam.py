import customtkinter

janela = customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
janela = customtkinter.CTk()

janela.geometry("500x500")
titulo = customtkinter.CTkLabel(janela, text="conversor de moedas")
selecionador = customtkinter.CTkLabel(janela, text="selecione sua moeda")

titulo.pack(padx=10, pady=10)
selecionador(padx=10, pady=10)

janela.mainloop()

