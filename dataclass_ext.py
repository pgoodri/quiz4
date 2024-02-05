from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    price: float
    quantity: int = 0

    def calculate_total_price(self) -> float:
        return self.price * self.quantity
    
def main():
    # Creating instances of Book
    book1 = Book("Python Programming", "Guido van Rossum", 29.99, 2)
    book2 = Book("Java Programming", "James Gosling", 34.99, 3)

    # Displaying book details
    print("Book 1:")
    print("Title:", book1.title)
    print("Author:", book1.author)
    print("Price:", book1.price)
    print("Quantity:", book1.quantity)
    print("Total Price:", book1.calculate_total_price())

    print("\nBook 2:")
    print("Title:", book2.title)
    print("Author:", book2.author)
    print("Price:", book2.price)
    print("Quantity:", book2.quantity)
    print("Total Price:", book2.calculate_total_price())

if __name__ == "__main__":
    main()