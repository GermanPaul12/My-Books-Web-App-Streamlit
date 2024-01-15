import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
fb_credentials = st.secrets["firebase"]['my_project_settings'] # returns a dictionary
db = firestore.Client.from_service_account_info(fb_credentials)

# PageConfig
st.set_page_config(page_title='Books', page_icon='📖', layout="wide")
st.title("📖 Books that I read")

# Fetch book data from Firestore
books = db.collection('books').stream()

for book in books:
    book_data = book.to_dict()
    title = book_data['title']
    author = book_data['author']
    img_path = book_data['img_path']
    subject = book_data['subject']

    col1, col2, col3, col4 = st.columns(4)
    with st.container():
        with col1:
            st.markdown(f"### Title: {title}")
            st.markdown(f"##### Author: {author}")
            st.write("Subject: ", subject)
        with col2:
            # Update image path if using Firebase Storage
            st.image(img_path, width=200)
