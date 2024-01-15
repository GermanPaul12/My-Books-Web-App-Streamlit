from google.cloud import firestore
import csv

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("data/firestore-key.json")

# Create a reference to the Google post.
doc_ref = db.collection("books").document("43myg8VGlkEV7z0loyoC")

# Then get the data at that reference.
doc = doc_ref.get()
print("The id is: ", doc.id)
print("The contents are: ", doc.to_dict())



def upload_books_to_firestore(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            title, author, img_path, subject = row
            book_data = {
                'title': title,
                'author': author,
                'img_path': img_path,  # You'll need to update this if you switch to Firebase Storage
                'subject': subject
            }
            db.collection('books').add(book_data)

upload_books_to_firestore('data/data.csv')