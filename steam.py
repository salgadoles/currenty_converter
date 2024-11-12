import customtkinter

# Configurações da aparência
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Configurações da janela
janela = customtkinter.CTk()
janela.geometry("500x500")

# Título
titulo = customtkinter.CTkLabel(janela, text="conversor de moedas", font=('', 20))

# Textos e menus de seleção
textoMoedaInicio = customtkinter.CTkLabel(janela, text="selecione sua moeda de origem")
textoMoedaFinal = customtkinter.CTkLabel(janela, text="selecione sua moeda de destino")

selecionadorMoedaInicio = customtkinter.CTkOptionMenu(janela, values=['BTC', 'USD', 'BRL', 'EUR'])
selecionadorMoedaFinal = customtkinter.CTkOptionMenu(janela, values=['BTC', 'USD', 'BRL', 'EUR'])

# Função de conversão
def conversor():
    print('Converte moeda')

# Botão de conversão
botaoConversor = customtkinter.CTkButton(janela, text='Converter', command=conversor)

# Frame de rolagem para exibir a lista de moedas
listaMoedas = customtkinter.CTkScrollableFrame(janela)
moedasDisponiveis = ['BTC: Bitcoin', 'BRL: Real brasileiro', 'USD: Dólar americano', 'EUR: Euro espanhol']

# Adicionando as moedas ao frame
for moeda in moedasDisponiveis:
    textoMoeda = customtkinter.CTkLabel(listaMoedas, text=moeda)
    textoMoeda.pack(padx=10, pady=10)

# Posicionando os elementos na janela
titulo.pack(padx=10, pady=10)
textoMoedaInicio.pack(padx=10, pady=10)
selecionadorMoedaInicio.pack(padx=10)
textoMoedaFinal.pack(padx=10, pady=10)
selecionadorMoedaFinal.pack(padx=10)
botaoConversor.pack(padx=10, pady=10)
listaMoedas.pack(padx=10, pady=10)

# Loop principal da janela
janela.mainloop()
