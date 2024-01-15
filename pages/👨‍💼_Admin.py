import streamlit as st
from google.cloud import firestore

# Initialize Firestore
fb_credentials = st.secrets["firebase"]['my_project_settings'] # returns a dictionary
db = firestore.Client.from_service_account_info(fb_credentials)

# PageConfig
st.set_page_config(page_title='Admin', page_icon='👨‍💼', layout="wide")
st.title("Login to add, delete, and update books")

pwd = st.text_input("type in your password", type="password")

if pwd == st.secrets["PW"]:
    st.header("Welcome to the Admin Dashboard")

    # Add Book Section
    with st.expander("Add books", expanded=True):
        title = st.text_input("Title")
        author = st.text_input("Author")
        img_url = st.text_input("Image URL")
        subject = st.text_input("Subject")

        if st.button("Add Book"):
            book_data = {
                'title': title,
                'author': author,
                'img_path': img_url,
                'subject': subject
            }
            db.collection('books').add(book_data)
            st.success("Book added successfully")

    # Delete Book Section
    with st.expander("Delete books"):
        col1, col2 = st.columns([3, 1])  # Adjust column width ratios as needed

        with col1:
            books = db.collection('books').stream()
            book_options = {f"{book.to_dict()['title']} by {book.to_dict()['author']}": book.id for book in books}
            selected_book = st.selectbox("Select a book to delete", options=list(book_options.keys()))

            if st.button("Delete Book"):
                db.collection('books').document(book_options[selected_book]).delete()
                st.success("Book deleted successfully")

        with col2:
            if selected_book:
                book_doc = db.collection('books').document(book_options[selected_book]).get()
                if book_doc.exists:
                    st.image(book_doc.to_dict()['img_path'], width=200)

    # Update Book Section
    with st.expander("Update books"):
        col1, col2 = st.columns([3, 1])  # Adjust column width ratios as needed

        with col1:
            books = db.collection('books').stream()
            book_options = {f"{book.to_dict()['title']} by {book.to_dict()['author']}": book.id for book in books}
            selected_book_for_update = st.selectbox("Select a book to update", options=list(book_options.keys()), key="update_select")

            # Fields for updating book data
            new_title = st.text_input("New Title", key="new_title")
            new_author = st.text_input("New Author", key="new_author")
            new_img_url = st.text_input("New Image URL", key="new_img_url")
            new_subject = st.text_input("New Subject", key="new_subject")

            if st.button("Update Book"):
                updated_data = {}
                if new_title:
                    updated_data['title'] = new_title
                if new_author:
                    updated_data['author'] = new_author
                if new_img_url:
                    updated_data['img_path'] = new_img_url
                if new_subject:
                    updated_data['subject'] = new_subject

                db.collection('books').document(book_options[selected_book_for_update]).update(updated_data)
                st.success("Book updated successfully")

        with col2:
            if selected_book_for_update:
                book_doc = db.collection('books').document(book_options[selected_book_for_update]).get()
                if book_doc.exists:
                    st.image(book_doc.to_dict()['img_path'], width=200)


elif pwd != "":
    st.warning("Wrong password")