import xmltodict

with open ('coins.xml','rb') as arquivos_moedas:
    dic.moedas = xmltodict.parse(arquivos_moedas)