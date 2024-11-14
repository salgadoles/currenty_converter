import requests

def pegar_cotacao_moeda(moeda_origem, moeda_destino):   
link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
requisicao = requests.get()

cotacao = requisicao.json()[f"{moeda_origem}{moeda_destino}"]["bid"]
return cotacao