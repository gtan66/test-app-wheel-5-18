import streamlit as st

st.write("Hello!")

x = st.slider("X:", 0, 100, 5)
st.write(x**2)
