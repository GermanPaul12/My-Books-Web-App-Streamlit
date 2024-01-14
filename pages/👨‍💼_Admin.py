import streamlit as st

# PageConfig
st.set_page_config(page_title='Admin',page_icon='👨‍💼', layout="wide")
st.title("Login to add and delete books")

pwd = st.text_input("type in your password", type="password")
if pwd == st.secrets.PW:
    st.write("You are logged in")