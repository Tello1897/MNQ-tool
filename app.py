
import streamlit as st

st.set_page_config(page_title="Calcolatore Contratti MNQ", layout="centered")

st.title("📊 Calcolatore di Contratti per MNQ")
st.markdown("Calcola quanti contratti MNQ puoi aprire in base a capitale, stop loss e rischio.")

# Input utente
capitale = st.number_input("💰 Fondi del conto ($)", min_value=1000.0, value=50000.0, step=1000.0)
percentuale_rischio = st.slider("⚠️ Percentuale di rischio per trade (%)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
stop_loss_punti = st.number_input("📉 Stop Loss (punti)", min_value=1.0, value=30.0, step=1.0)
valore_punto = st.number_input("💵 Valore per punto ($)", min_value=0.1, value=2.0, step=0.1)

# Calcoli
rischio_totale = capitale * (percentuale_rischio / 100)
rischio_per_contratto = stop_loss_punti * valore_punto
contratti_massimi = int(rischio_totale // rischio_per_contratto)

# Risultati
st.subheader("📈 Risultati")
st.write(f"**Rischio massimo per trade:** ${rischio_totale:,.2f}")
st.write(f"**Rischio per contratto MNQ:** ${rischio_per_contratto:,.2f}")
st.write(f"**Contratti massimi consigliati:** {contratti_massimi}")
