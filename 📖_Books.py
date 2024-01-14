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
        col1, col2, col3, col4 = st.columns(4)
        with st.container():
            with col1:
                st.markdown(f"### Title: {title}")
                st.markdown(f"##### Author: {author}")
                st.write("Subject: ", subject)
            with col2:
                st.image(f"data/img/{img_path}", width=200)    
    