import streamlit as st

st.title("kuliah praktikum big data Pertemuan 09")
st.write("azizah amelia")
st.write("# Heading 1")

pilih1 = st.checkbox('ya')
pilih2 = st.checkbox('tidak')

st.write(pilih1)
st.write(pilih2)

st.radio('Daftar Menu', ['Soto', 'Capcai', 'Sayur Sop', 'Ayam Goreng'])

minuman = st.selectbox('pilih minuman',
            ['es teh', 'teh hangat', 'jus jeruk', 'jus mangga'])
st.write(minuman)

bayar = st.multiselect('metode pembayaran:',
                      ['Cash/Tunai', 'OVO', 'GoPay', 'Debit'])
st.write(bayar)
