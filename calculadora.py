import requests

API_KEY = "005a8e405a0f4eba80671e4c1715b306"
BASE_URL = f"https://api.currencyfreaks.com/latest?apikey={API_KEY}"

def converter_moeda(moeda_origem, moeda_destino, valor):
    resposta = requests.get(BASE_URL)
    
    if resposta.status_code != 200:
        print("Erro ao obter dados da API. Verifique sua chave de API.")
        return None

    dados = resposta.json()
    taxas = dados.get("rates", {})

# Obtem a taxa de cambio das moedas
    taxa_origem = float(taxas.get(moeda_origem, 0))
    taxa_destino = float(taxas.get(moeda_destino, 0))

# Verifica as moedas fornecidas se ainda são validas
    if taxa_origem == 0 or taxa_destino == 0:
        print("Moeda inválida ou não suportada pela API.")
        return None

# Realiza a conversão do valor 
    valor_convertido = (valor / taxa_origem) * taxa_destino
    return valor_convertido

# Captura os dados de entrada do usuario 
moeda_origem = input("Digite a moeda de origem : ").upper() # Precisa saber as siglas das moedas 
moeda_destino = input("Digite a moeda de destino : ").upper() 

try:
    valor = float(input("Digite o valor a ser convertido: "))
except ValueError:
    print("Erro: Digite um número válido.")
    exit()

resultado = converter_moeda(moeda_origem, moeda_destino, valor)

# Chama a função de conversão e exibe o resultado
if resultado is not None:
    print(f"{valor:.2f} {moeda_origem} equivale a {resultado:.2f} {moeda_destino}")
# As pessoas que estão lendo kkk, era para ser uma calculadora mas no meio do caminho acebei mudando de ideia ;)

