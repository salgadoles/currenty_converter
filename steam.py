import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

dic_conversoes_disponiveis = conversoes_disponiveis()  
moedasDisponiveis = nomes_moedas() 

titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=('', 20))

textoMoedaInicio = customtkinter.CTkLabel(janela, text="Selecione sua moeda de origem")
textoMoedaFinal = customtkinter.CTkLabel(janela, text="Selecione sua moeda de destino")

def carregar_moeda_destino(moeda_selecionada):
    lista_moeda_destino = dic_conversoes_disponiveis[moeda_selecionada] 
    selecionadorMoedaFinal.configure(values=lista_moeda_destino)
    selecionadorMoedaFinal.set(lista_moeda_destino[0])

selecionadorMoedaInicio = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moeda_destino)
selecionadorMoedaFinal = customtkinter.CTkOptionMenu(janela, values=["Selecionar moeda de destino"])

def conversor():
    moeda_origem = selecionadorMoedaInicio.get()
    moeda_destino = selecionadorMoedaFinal.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} = {cotacao} {moeda_destino}")

botaoConversor = customtkinter.CTkButton(janela, text='Converter', command=conversor)

listaMoedas = customtkinter.CTkScrollableFrame(janela)
texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")

for codigo_moeda in moedasDisponiveis:
    nomeMoeda = moedasDisponiveis[codigo_moeda]  
    textoMoeda = customtkinter.CTkLabel(listaMoedas, text=f"{codigo_moeda}: {nomeMoeda}")
    textoMoeda.pack()

titulo.pack(padx=10, pady=10)
textoMoedaInicio.pack(padx=10, pady=10)
selecionadorMoedaInicio.pack(padx=10)
textoMoedaFinal.pack(padx=10, pady=10)
selecionadorMoedaFinal.pack(padx=10)
texto_cotacao_moeda.pack(padx=10, pady=10)
botaoConversor.pack(padx=10, pady=10)
listaMoedas.pack(padx=10, pady=10)

janela.mainloop()
