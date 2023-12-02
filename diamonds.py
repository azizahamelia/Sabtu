import streamlit as st
import pandas as pd
import plotly.express as px

st.title("visualisasi data diamond")
st.write("oleh: Azizah")

df = pd.read_csv('diamonds.csv')

st.write("### 5 data pertama")
st.write( df.head() )

st.write("## histogram data diamonds")
plot = px.histogram(
    df,
    x = 'price',
    title = "Histogram harga diamonds"
)
plot.update_layout(
    xaxis_title = 'harga',
    yaxis_title = 'jumlah'
)
st.plotly_chart(plot)

st.write("## Historam color")
plot_color = px.histogram(
    df,
    x = 'color',
    title = "Histogram warna diamonds"
)
plot_color.update_layout(
    xaxis_title = 'warna',
    yaxis_title = 'jumlah'
)
st.plotly_chart(plot_color)

st.write('## line chart dimensi x, y, dan z')
plot_dimensi = px.line(
    df,
    y =['x', 'y', 'z'],
    title = 'dimensi x, y, dan z'
)
st.plotly_chart(plot_dimensi )