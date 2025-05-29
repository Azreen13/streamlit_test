import streamlit as st
import requests

# Tajuk aplikasi
st.title('MY FIRST PROJECK !!')

# Mesej alu-aluan
st.write('Welcome to my Streamlit app!')

# Input mesej pengguna
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('Customized Message:', widgetuser_input)

# Panggilan API untuk kadar tukaran MYR
response = requests.get('https://api.vatcomply.com/rates?base=MYR')

if response.status_code == 200:
    data = response.json()

    # Senarai mata wang tersedia
    currencies = list(data['rates'].keys())

    # Dropdown untuk pilih mata wang
    selected_currency = st.selectbox('Pilih mata wang untuk tukaran:', currencies)

    # Papar kadar tukaran
    exchange_rate = data['rates'][selected_currency]
    st.success(f"1 MYR = {exchange_rate:.4f} {selected_currency}")

    # Input amaun
    amount = st.number_input("Masukkan amaun dalam MYR:", min_value=0.0, value=1.0)
    converted = amount * exchange_rate
    st.write(f"{amount:.2f} MYR = {converted:.2f} {selected_currency}")

    # Papar semua data JSON
    with st.expander("Lihat semua kadar tukaran (JSON penuh)"):
        st.json(data)

else:
    st.error(f"API call failed with status code: {response.status_code}")
