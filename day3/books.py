books = [
    {"title": "golestan", "author": "sadi"},
    {"title": "sayeha", "author": "debi"},
    {"title": "boostan", "author": "sadi"},
]

author_name=input("inter your author name:")

for book in books:
    if book["author"]==author_name:
        print(book["title"])
   

