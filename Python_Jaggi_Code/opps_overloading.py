class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

def main():
    book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
    book2 = Book("harry potter and the Philosopher's stone", "j.k. Rowling", 223)

    print(book1 != book2)

if __name__ == '__main__':
    main()