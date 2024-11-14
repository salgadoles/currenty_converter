import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

# Configurações da aparência
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Configurações da janela
janela = customtkinter.CTk()
janela.geometry("500x500")

# Carrega os dados
dic_conversoes_disponiveis = conversoes_disponiveis()  # Chama a função para obter o dicionário
moedasDisponiveis = nomes_moedas()  # Chama a função para obter as moedas

# Título
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=('', 20))

# Textos e menus de seleção
textoMoedaInicio = customtkinter.CTkLabel(janela, text="Selecione sua moeda de origem")
textoMoedaFinal = customtkinter.CTkLabel(janela, text="Selecione sua moeda de destino")

# Função para atualizar o menu de destino com base na seleção
def carregar_moeda_destino(moeda_selecionada):
    lista_moeda_destino = dic_conversoes_disponiveis [moeda_selecionada] 
    selecionadorMoedaFinal.configure(values=lista_moeda_destino)
    selecionadorMoedaFinal.set(lista_moeda_destino[0])

# Menus de seleção
selecionadorMoedaInicio = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()),command=carregar_moeda_destino)

selecionadorMoedaFinal = customtkinter.CTkOptionMenu(janela, values=["Selecionar moeda de origem"])

# Função de conversão
def conversor():
         moeda_origem = campo_moeda_origem.get()
      moeda_destino = campo_moeda_destino.get()
      if moeda_origem and moeda_destino:
    
  cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
    texto_cotacao_moeda.configure(text=f"1 {moeda_origem} ={cotacao} {moeda_destino}")

# Botão de conversão
botaoConversor = customtkinter.CTkButton(janela, text='Converter', command=conversor)

# Frame de rolagem para exibir a lista de moedas disponíveis
listaMoedas = customtkinter.CTkScrollableFrame(janela)
texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="" )
# Adicionando as moedas ao frame
for codigo_moeda in moedasDisponiveis:
    textoMoeda = customtkinter.CTkLabel(listaMoedas, text=f"{codigo_moedamoeda}: {nomeMoeda}")
    textoMoeda.pack()

# Posicionando os elementos na janela
titulo.pack(padx=10, pady=10)
textoMoedaInicio.pack(padx=10, pady=10)
selecionadorMoedaInicio.pack(padx=10)
textoMoedaFinal.pack(padx=10, pady=10)
selecionadorMoedaFinal.pack(padx=10)
texto_cotacao_moeda.pack(padx=10, pady=10)
botaoConversor.pack(padx=10, pady=10)
listaMoedas.pack(padx=10, pady=10)

# Loop principal da janela
janela.mainloop()
