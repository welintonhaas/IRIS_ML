import streamlit as st

st.write("# Classificação de IRIS")
st.write('## Exemplo com comprimentos de pétala e sépala')

st.sidebar.write('### Parâmetros')
st.sidebar.slider('Comprimento da sépala', 4, 8, 5.8, 0.1)

st.sidebar.slider('Comprimento da pétala', 0.9, 7, 3.8, 0.1)
