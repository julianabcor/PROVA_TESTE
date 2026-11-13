import streamlit as st
from consumidor_api import obter_dados

st.set_page_config(
    page_title="Monitoramento Meteorológico",
    page_icon="🌦️",
    layout="wide"
)

st.title("🌦️ Monitoramento Meteorológico")
st.caption("Estação meteorológica — Jaraguá do Sul/SC")
st.divider()

if st.button("🔄 Atualizar dados"):
    st.rerun()

try:
    with st.spinner("Consultando a API meteorológica..."):
        dados = obter_dados()

    st.success("Dados meteorológicos carregados.")
    st.subheader("Condições atuais")

    col1, col2, col3, col4 = st.columns(4)

    # Ajuste as chaves do dicionário 'dados' conforme o retorno da sua função
    col1.metric(
        "Temperatura:",
        f"{dados['current']['temperature_2m']} °C"
    )
    col2.metric(
        "Umidade:",
        f"{dados['current']['relative_humidity_2m']}%"
    )
    col3.metric(
        "Sensação térmica:",
        f"{dados['current']['apparent_temperature']}°C"
    )
    col4.metric(
        "Data/Hora:",
        f"{dados['current']['time']}"
    )
    
except Exception as e:
    st.error(f"Erro ao carregar os dados meteorológicos: {e}")