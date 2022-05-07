import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

st.write("# Classificação de IRIS")
st.write('## Exemplo com comprimentos de pétala e sépala')

st.sidebar.write('### Parâmetros')
comp_sepala = st.sidebar.slider('Comprimento da sépala', 4.0, 8.0, 5.8, 0.1)
comp_petala = st.sidebar.slider('Comprimento da pétala', 0.9, 7.0, 3.8, 0.1)

with open("objetos.pkl", 'rb') as arquivo:
  ss, dtc = pickle.load(arquivo)

estrutura = { 'comp_sepala' : comp_sepala, 
              'comp_petala' : comp_petala }

df = pd.DataFrame(estrutura, index=[0])

st.write('### Parâmetros de entrada')
st.write(df)

#normaliza os dados
df = ss.transform(df)
st.write(df)

# predição
predicao = dtc.predict(df)
st.write(f'A classe dessa flor é: **{predicao[0]}**')

predicao = dtc.predict_proba(df)
st.write('Probabilidades')
st.write(predicao)
