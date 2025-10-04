import pandas as pd
import requests
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

print("Iniciando o script de análise da Taxa Selic...")

# --- 1. CONFIGURAÇÃO E BUSCA DE DADOS ---
CODIGO_SELIC_BCB = 1178
DATA_INICIO = '2016-01-01'

data_inicio_formatada = datetime.strptime(DATA_INICIO, '%Y-%m-%d').strftime('%d/%m/%Y')
data_fim_formatada = datetime.now().strftime('%d/%m/%Y')

url_api = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{CODIGO_SELIC_BCB}/dados?formato=json&dataInicial={data_inicio_formatada}&dataFinal={data_fim_formatada}"

print(f"Buscando dados da Taxa Selic de {data_inicio_formatada} até {data_fim_formatada}...")

try:
    response = requests.get(url_api, timeout=30)
    response.raise_for_status()
    
    dados_json = response.json()
    df_selic = pd.DataFrame(dados_json)
    
    # --- 2. LIMPEZA E PREPARAÇÃO DOS DADOS ---
    print("Preparando e limpando os dados...")
    df_selic['valor'] = pd.to_numeric(df_selic['valor'])
    df_selic['data'] = pd.to_datetime(df_selic['data'], format='%d/%m/%Y')
    df_selic.set_index('data', inplace=True)
    df_selic.rename(columns={'valor': 'selic'}, inplace=True)
    
    print("\nDados prontos para análise!")
    
    # --- 3. VISUALIZAÇÃO HISTÓRICA ---
    print("\nGerando gráfico da Taxa Selic histórica...")
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=df_selic, x=df_selic.index, y='selic', color='purple', linewidth=2)
    plt.title(f'Taxa Selic Diária (Anualizada) desde {DATA_INICIO}', fontsize=16, weight='bold')
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Taxa de Juros Anual (%)', fontsize=12)
    plt.show()

    # --- 4. NOVA SEÇÃO: ANÁLISE DE PICOS (EXTREMOS) ---
    print("\nCalculando os valores extremos do período...")

    # Encontra o valor máximo e a data em que ocorreu
    pico_maximo = df_selic['selic'].max()
    data_pico_maximo = df_selic['selic'].idxmax()

    # Encontra o valor mínimo e a data em que ocorreu
    pico_minimo = df_selic['selic'].min()
    data_pico_minimo = df_selic['selic'].idxmin()

    # Imprime os resultados formatados
    print("\n--- Análise de Picos da Selic ---")
    print(f"A Selic atingiu sua MAIOR taxa de {pico_maximo:.2f}% ao ano no dia {data_pico_maximo.strftime('%d/%m/%Y')}.")
    print(f"A Selic atingiu sua MENOR taxa de {pico_minimo:.2f}% ao ano no dia {data_pico_minimo.strftime('%d/%m/%Y')}.")
    # ---------------------------------------------------

except Exception as e:
    print(f"Ocorreu um erro: {e}")

print("\nScript finalizado.")