import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as  pd
import pandas_datareader.data as web

#Definindo o estilo do gráfico
style.use('ggplot')

#Datas de inicio e final do gráfico
start = dt.datetime(2000,1,1)
end = dt.datetime(2020,6,1)

#Escolher  a fonte de dados e a ação/indice --> Stooq e Bovespa
df = web.DataReader('^BVP', 'stooq', start, end)
print(df.head())
print(df.tail())

#Plotar uma coluna especifica 
df['Close'].plot
plt.show()