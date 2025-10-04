# Análise da Taxa Selic com Dados do Banco Central do Brasil

## Descrição

Este projeto realiza uma análise da série histórica da Taxa Selic, a taxa básica de juros da economia brasileira, utilizando dados públicos e oficiais disponibilizados pela API do Banco Central do Brasil (BCB).

O script em Python automatiza todo o processo de **coleta, limpeza, análise e visualização** dos dados, permitindo extrair insights relevantes sobre a política monetária e o cenário econômico do país ao longo do tempo.

O objetivo é demonstrar um fluxo completo de análise de dados de séries temporais: desde a aquisição via API até a geração de visualizações e estatísticas conclusivas.

---

## Funcionalidades

- **Coleta Automática de Dados:** Consulta diretamente a API do SGS (Sistema Gerenciador de Séries Temporais) do Banco Central para obter os dados da Selic.
- **Limpeza e Preparação:** Uso da biblioteca `pandas` para tratamento dos dados, conversão de tipos e preparação da série temporal.
- **Análise de Extremos:** Identificação das maiores e menores taxas de juros do período, com valores e datas correspondentes.
- **Tendências da Política Monetária:** Cálculo e visualização de médias móveis de 90 e 180 dias para suavizar as variações e destacar as tendências de longo prazo.
- **Visualizações Claras:** Geração de gráficos com `matplotlib` e `seaborn` para facilitar a interpretação dos resultados.

---

## Tecnologias Utilizadas

- Python 3.x
- Pandas
- Requests
- Matplotlib
- Seaborn

---

## Como Executar o Projeto

Siga os passos abaixo para rodar o projeto em sua máquina local:

### 1\. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2\. Crie um Ambiente Virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3\. Instale as Dependências

Crie um arquivo `requirements.txt` na raiz do projeto com o seguinte conteúdo:

```
pandas
requests
matplotlib
seaborn
```

E instale com:

```bash
pip install -r requirements.txt
```

### 4\. Execute o Script de Análise

```bash
python analise_selic.py
```

O script irá:

- Buscar os dados mais recentes na API.
- Imprimir a análise de picos no terminal.
- Exibir dois gráficos em janelas sequenciais.

---

## Resultados

A execução gera as seguintes saídas:

### 1\. Análise de Picos (Terminal)

_(Nota: Os valores abaixo são exemplos. O script irá gerar os dados mais recentes.)_

```
--- Análise de Picos da Selic ---
A Selic atingiu sua MAIOR taxa de 14.25% ao ano no dia 29/07/2016.
A Selic atingiu sua MENOR taxa de 2.00% ao ano no dia 06/08/2020.
```

### 2\. Gráfico 1: Taxa Selic Histórica

Evolução diária da Taxa Selic (anualizada) no período configurado.

`grafico_selic_historico.png`

### 3\. Gráfico 2: Tendências com Médias Móveis

Taxa Selic diária sobreposta pelas médias móveis de 90 e 180 dias, destacando as tendências da política de juros.

`grafico_selic_tendencias.png`

---

## Licença

Este projeto está licenciado sob a **MIT License**.
