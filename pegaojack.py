import xmltodict

# Função para carregar os nomes das moedas
def nomes_moedas():
    with open('coins.xml', 'rb') as arquivos_moedas:
        dic_moedas = xmltodict.parse(arquivos_moedas)
        moedas = dic_moedas['xml']
        return moedas

# Função para carregar as conversões disponíveis
def conversoes_disponiveis():
    with open('conversoes.xml', 'rb') as arquivos_conversoes:
        dic_conversoes = xmltodict.parse(arquivos_conversoes)
        

        dic_conversoes_disponiveis = {}

        # Processa as conversões
        for par_conversao in conversoes:
            moedas_origem, moedas_destino = par_conversao.split("-")

            if par_conversao in dic_conversoes_disponiveis:
                dic_conversoes_disponiveis[moedas_origem].append(moedas_destino)
            else:
                dic_conversoes_disponiveis[moedas_origem] = [moedas_destino]

        return dic_conversoes_disponiveis
 