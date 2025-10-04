import pandas as pd
import requests
from datetime import datetime

print("Iniciando o script de análise da Taxa Selic...")

# --- 1. CONFIGURAÇÃO DA REQUISIÇÃO ---
# A principal mudança: O código da série da Taxa Selic diária (anualizada) é 1178.
CODIGO_SELIC_BCB = 1178
DATA_INICIO = '2016-01-01'

# Formata as datas para o padrão que a API do BCB espera (dd/mm/YYYY)
data_inicio_formatada = datetime.strptime(DATA_INICIO, '%Y-%m-%d').strftime('%d/%m/%Y')
data_fim_formatada = datetime.now().strftime('%d/%m/%Y')

# Monta a URL da API para o indicador da Selic
url_api = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{CODIGO_SELIC_BCB}/dados?formato=json&dataInicial={data_inicio_formatada}&dataFinal={data_fim_formatada}"

print(f"Buscando dados da Taxa Selic de {data_inicio_formatada} até {data_fim_formatada}...")

try:
    # --- 2. BUSCA E CARREGAMENTO DOS DADOS ---
    response = requests.get(url_api, timeout=30)
    response.raise_for_status() # Garante que a requisição foi um sucesso
    
    dados_json = response.json()
    print("Sucesso! Dados JSON recebidos.")

    # Converte a resposta JSON em uma tabela (DataFrame) do pandas
    df_selic = pd.DataFrame(dados_json)
    
    # --- 3. LIMPEZA E PREPARAÇÃO DOS DADOS ---
    print("Preparando e limpando os dados...")
    # A coluna 'valor' vem como texto, precisamos convertê-la para número (float)
    df_selic['valor'] = pd.to_numeric(df_selic['valor'])
    
    # A coluna 'data' vem como texto, convertemos para o formato de data
    df_selic['data'] = pd.to_datetime(df_selic['data'], format='%d/%m/%Y')
    
    # Definimos a coluna 'data' como o índice da nossa tabela
    df_selic.set_index('data', inplace=True)

    # Renomeamos a coluna 'valor' para 'selic' para ficar mais claro
    df_selic.rename(columns={'valor': 'selic'}, inplace=True)
    
    # --- 4. VERIFICAÇÃO FINAL ---
    print("\nDados prontos para análise!")
    print("Amostra dos 5 dias mais recentes:")
    print(df_selic.tail())
    
except Exception as e:
    print(f"Ocorreu um erro: {e}")

print("\nScript finalizado.")