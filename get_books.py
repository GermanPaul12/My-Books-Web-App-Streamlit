import requests
from PIL import Image
import matplotlib.pyplot as plt

def clean_str(text): return "".join([i for i in text if i.isalpha()])

Queries = [
           "The Obstacle Is the Way: The Timeless Art of Turning Trials into Triumph Holiday, Ryan",
           "Stillness Is the Key Holiday, Ryan",
           "The Daily Stoic: 366 Meditations on Wisdom, Perseverance, and the Art of Living Holiday, Ryan",
           "On the Shortness of Life: Life Is Long if You Know How to Use It Seneca",
           "What Every Body is Saying: An Ex-FBI Agent's Guide to Speed-Reading People Navarro, Joe",
           "How to Talk to Anyone Leil Lowndes",
           "Discipline Is Destiny: The Power of Self-Control Holiday, Ryan",
           "Ikigai: The Japanese Secret to a Long and Happy Life Garcia Puigcerver, Hector",
           "The Art of Statistics: How to Learn from Data Spiegelhalter, David",
           "The Monk Who Sold His Ferrari: A Fable About Fulfilling Your Dreams and Reaching Your Destiny Sharma, Robin S.",
           "The Almanack of Naval Ravikant: A Guide to Wealth and Happiness Jorgenson, Eric",
           "When Nietzsche Wept Yalom, Irvin D.",
           "Schachnovelle Zweig, Stefan",
           "Animal Farm Orwell, George",
           "One Hundred Years of Solitude García Márquez, Gabriel"
           ]
url = "https://openlibrary.org/search.json"
for query in Queries:
    params = {"q":query, "limit": 1, "language": "eng"}

    response = requests.get(url, params=params)
    data = response.json()["docs"]
    title = data[0]["title"]
    author = data[0]["author_name"][0]
    isbn = data[0]["isbn"][0]
    if data[0].get("subject"): subject = data[0]["subject"][0]
    else: subject = "No subject"
    print(title,author, subject)
    img_url = f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg" 
    img = Image.open(requests.get(img_url, stream=True).raw)
    if img.mode != 'RGB': img = img.convert('RGB')
    print(clean_str(title))
    img.save(f"data/img/{clean_str(title)}.jpg") 
    with open("data/data.csv", "a", encoding="utf8") as f:
        f.write(f"{title},{author},{clean_str(title)}.jpg,{subject}\n")