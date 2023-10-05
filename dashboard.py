import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" +str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]


col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(df_filtered, x="Quantity", y="Product line", title="Faturamento por Produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(df_filtered, x="City", y="Total", title="Faturamento por filial",color="City")
col3.plotly_chart(fig_city, use_container_width=True)

fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por Pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, x="City", y="Rating", title="Avaliação",color="City")
col5.plotly_chart(fig_rating, use_container_width=True)

#visão mensal
#faturamento por unidade
#produto mais vendido, por filial
#desempenho das formas de pagamento
#avaliação das filiais




