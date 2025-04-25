import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Calculadora de ROI", layout="centered")

st.title("📊 Calculadora de Retorno de Inversión (ROI)")
st.markdown("Calcula tus ingresos por renta y plusvalía en un plazo definido.")

# Entradas del usuario
monto_inicial = st.number_input("💰 Monto Inicial ($)", value=100000, step=1000)
plazo_meses = st.slider("📅 Plazo (meses)", min_value=6, max_value=120, value=24)
renta_mensual = st.number_input("🏠 Renta Mensual ($)", value=5000, step=100)

# Cálculos
ganancia_total = renta_mensual * plazo_meses
plusvalia_estimada = monto_inicial * 0.05 * (plazo_meses / 12)

meses = np.arange(1, plazo_meses + 1)
ganancia_acumulada = renta_mensual * meses
plusvalia_acumulada = np.linspace(0, plusvalia_estimada, plazo_meses)

# Resultados
st.subheader("🔍 Resultados:")
st.write(f"**Ganancia total por renta:** ${ganancia_total:,.2f}")
st.write(f"**Plusvalía estimada:** ${plusvalia_estimada:,.2f}")
st.write(f"**Ganancia total estimada:** ${ganancia_total + plusvalia_estimada:,.2f}")

# Gráfico
st.subheader("📈 Gráfica de ROI")

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(meses, ganancia_acumulada, label="Ganancia por Renta", color="green")
ax.plot(meses, plusvalia_acumulada, label="Plusvalía Estimada", linestyle="--", color="blue")
ax.set_xlabel("Meses")
ax.set_ylabel("Monto ($)")
ax.set_title("ROI a lo largo del tiempo")
ax.legend()
ax.grid(True)
st.pyplot(fig)
