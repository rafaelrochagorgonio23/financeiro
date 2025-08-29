Previsão de Faturamento com Prophet
Este repositório demonstra uma simulação de previsão de faturamento utilizando a biblioteca Prophet do Facebook, com visualização interativa via Plotly. O projeto é ideal para quem deseja entender como aplicar modelos de séries temporais em dados financeiros.

Aviso importante: Os dados utilizados neste projeto são puramente fictícios e gerados aleatoriamente para fins educacionais. Para uma análise real, substitua os dados simulados por informações reais e confiáveis.

Arquivos do Projeto
faturamento_historico.xlsx
Contém os dados simulados de faturamento diário ao longo de 90 dias.

previsao_faturamento.py
Script Python que:

Gera dados fictícios de faturamento.
Salva os dados em Excel.
Treina um modelo Prophet.
Realiza previsões para os próximos 30 dias.
Salva os resultados em Excel.
Gera um gráfico interativo em HTML.
previsao_faturamento.xlsx
Resultado da previsão com os valores estimados (yhat) e seus limites inferior (yhat_lower) e superior (yhat_upper).

grafico_previsao.html (gerado pelo script)
Gráfico interativo da previsão de faturamento.

Como Executar
Instale as dependências:

Shell
pip install pandas numpy prophet plotly openpyxl
Execute o script:

Shell
python previsao_faturamento.py
Verifique os arquivos gerados:

faturamento_historico.xlsx
previsao_faturamento.xlsx
grafico_previsao.html
Observações
Este projeto é uma base de estudo e pode ser adaptado para diferentes contextos de previsão.
Para uso profissional, recomenda-se:
Limpeza e validação dos dados reais.
Ajuste de hiperparâmetros do modelo.
Avaliação de métricas de desempenho.
