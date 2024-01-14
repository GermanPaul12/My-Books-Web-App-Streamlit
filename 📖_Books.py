import streamlit as st

# PageConfig
st.set_page_config(page_title='Books',page_icon='📖', layout="wide")
st.title("📖 Books that I read")

with open("data/data.csv", "r", encoding="utf8") as f:
    data = f.readlines()
    for line in data[1:]:
        line = line.replace("\n", "")
        title,author,img_path,subject = line.split(",")
        print(title,author, img_path, subject)
        with st.container():
            col1, col2 = st.columns(2)
            
    