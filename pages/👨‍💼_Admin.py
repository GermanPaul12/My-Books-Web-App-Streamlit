import streamlit as st
from PIL import Image
import os

def save_uploadedfile(uploadedfile):
     with open(os.path.join("data/img/",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to data/img/".format(uploadedfile.name))


# PageConfig
st.set_page_config(page_title='Admin',page_icon='👨‍💼', layout="wide")
st.title("Login to add and delete books")

pwd = st.text_input("type in your password", type="password")
if pwd == st.secrets["PW"]:
    st.header("Welcome to the Admin Dashboard")
    with st.expander("Add books", expanded=True):
        title = st.text_input("Title")
        author = st.text_input("Author")
        subject = st.text_input("Subject")
        img_file =  st.file_uploader("Upload book cover", type=['png','jpeg','jpg'])
        if img_file is not None:
            file_details = {"FileName":img_file.name,"FileType":img_file.type}
            save_uploadedfile(img_file)
        if st.button("Add"):
            with open("data/data.csv", "a", encoding="utf8") as f:
                f.write(f"\n{title},{author},{img_file.name},{subject}\n")
            st.success("Book added successfully")
    with st.expander("Delete books"):
        with open("data/data.csv", "r", encoding="utf8") as f:
            data = f.readlines()
            books = [line.split(",")[0] for line in data[1:]]
            book = st.selectbox("Select book to delete", books)
            if st.button("Delete"):
                with open("data/data.csv", "w", encoding="utf8") as f:
                    f.write("title,author,img_path,subject")
                    for line in data[1:]:
                        if line.split(",")[0] != book:
                            f.write(line)
                st.success("Book deleted successfully")        
elif pwd != "": st.warning("Wrong password")    