import pandas as pd
import numpy as np
from prophet import Prophet
import plotly.graph_objects as go

# 1. Simular dados de faturamento diário (90 dias)
np.random.seed(42)
datas = pd.date_range(start="2025-08-01", periods=90)
valores = np.random.normal(loc=10000, scale=1500, size=90).round(2)
df = pd.DataFrame({"Data": datas, "Valor": valores})

# 2. Salvar histórico em Excel
df.to_excel("faturamento_historico.xlsx", index=False, engine="openpyxl")

# 3. Preparar dados para o Prophet
df_prophet = df.rename(columns={"Data": "ds", "Valor": "y"})

# 4. Criar e treinar o modelo
modelo = Prophet()
modelo.fit(df_prophet)

# 5. Gerar datas futuras (30 dias)
futuro = modelo.make_future_dataframe(periods=30)
previsao = modelo.predict(futuro)

# 6. Salvar previsões em Excel
previsao[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_excel("previsao_faturamento.xlsx", index=False, engine="openpyxl")

# 7. Gerar gráfico interativo
fig = go.Figure()
fig.add_trace(go.Scatter(x=previsao['ds'], y=previsao['yhat'], mode='lines', name='Previsão'))
fig.add_trace(go.Scatter(x=previsao['ds'], y=previsao['yhat_lower'], mode='lines', name='Limite Inferior', line=dict(dash='dot')))
fig.add_trace(go.Scatter(x=previsao['ds'], y=previsao['yhat_upper'], mode='lines', name='Limite Superior', line=dict(dash='dot')))
fig.update_layout(title="Previsão de Faturamento - Leasing de Equipamentos",
                  xaxis_title="Data", yaxis_title="Faturamento (R$)")
fig.write_html("grafico_previsao.html")

print("✅ Simulação concluída!")
print("Arquivos gerados:")
print("- faturamento_historico.xlsx")
print("- previsao_faturamento.xlsx")
print("- grafico_previsao.html")
