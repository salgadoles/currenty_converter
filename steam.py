import customtkinter

janela = customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
janela = customtkinter.CTk()

janela.geometry("500x500")
titulo = customtkinter.CTkLabel(janela, text="conversor de moedas")
textoMoedaInicio = customtkinter.CTkLabel(janela, text="selecione sua moeda")
textoMoedaFinal = customtkinter.CTkLabel(janela, text="selecione sua moeda")

selecionadorMoedaInicio = customtkinter.CTkOptionMenu(janela, values=['BTC','USD','BRL','EUR'])
selecionadorMoedaFinal = customtkinter.CTkOptionMenu(janela, values=['BTC','USD','BRL','EUR'])


titulo.pack(padx=10, pady=10)
textoMoedaInicio.pack(padx = 10, pady = 10)
textoMoedaFinal.pack(padx=10, pady=10)
selecionadorMoedaInicio.pack(padx=10, pady=10)
selecionadorMoedaFinal.pack(padx=10, pady=10)

janela.mainloop()

