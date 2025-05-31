import streamlit as st

st.set_page_config(page_title="SIP + Lump Sum Calculator", layout="centered")

st.title("📈 SIP + Lump Sum Calculator")

# User inputs
lumpsum = st.number_input("Lump Sum Investment (₹)", min_value=0, value=100000, step=1000)
sip = st.number_input("Monthly SIP Amount (₹)", min_value=0, value=5000, step=500)
rate = st.number_input("Annual Return Rate (%)", min_value=0.0, value=12.0, step=0.1)
years = st.number_input("Investment Duration (Years)", min_value=1, value=10, step=1)

# Calculate button
if st.button("Calculate"):
    r = rate / 12 / 100
    n = years * 12

    # Lump sum future value
    fv_lumpsum = lumpsum * ((1 + r) ** n)

    # SIP future value
    fv_sip = sip * (((1 + r) ** n - 1) / r) * (1 + r)

    # Total
    total = fv_lumpsum + fv_sip

    # Display results
    st.subheader("📊 Results:")
    st.success(f"Lump Sum Future Value: ₹{fv_lumpsum:,.2f}")
    st.success(f"SIP Future Value: ₹{fv_sip:,.2f}")
    st.markdown(f"### 🟩 Total Future Value: ₹{total:,.2f}")
