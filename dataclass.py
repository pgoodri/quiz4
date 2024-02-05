from dataclasses import dataclass

@dataclass 
class Book:
    title: str
    author: str
    price: float

def main():
    # Creating instances of Book
    book1 = Book("Python Programming", "Guido van Rossum", 29.99)
    book2 = Book("Java Programming", "James Gosling", 34.99)

    # Displaying book details
    print("Book 1:")
    print("Title:", book1.title)
    print("Author:", book1.author)
    print("Price:", book1.price)

    print("\nBook 2:")
    print("Title:", book2.title)
    print("Author:", book2.author)
    print("Price:", book2.price) 

if __name__ == "__main__":
    main()  