import csv
import random
from pathlib import Path

# This makes file paths work even when the terminal is opened in another folder.
FOLDER = Path(__file__).resolve().parent
BOOKS_FILE = FOLDER / "books-en.csv"


def read_books():
    # This CSV file uses semicolons and Windows-1252 encoding.
    with open(BOOKS_FILE, encoding="cp1252", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)


def count_titles(books):
    count = 0

    for book in books:
        title = book["Book-Title"]
        if len(title) > 30:
            count += 1

    print("Number of books with titles longer than 30 characters:", count)


def search_author(books):
    author = input("Enter an author's name: ").strip().lower()

    if not author:
        print("Please enter an author's name.")
        return

    found = False

    for book in books:
        book_author = book["Book-Author"].strip()
        price_text = book["Price"].strip().replace(",", ".")

        try:
            price = float(price_text)
        except ValueError:
            continue

        # Variant 1: show books costing no more than 150 rubles.
        if author in book_author.lower() and price <= 150:
            print(f'{book["Book-Title"]} — {book_author} — {price:g} rubles')
            found = True

    if not found:
        print("No books by that author costing 150 rubles or less were found.")


def make_references(books):
    if not books:
        print("The books file is empty.")
        return

    selected = random.sample(books, min(20, len(books)))
    output_file = FOLDER / "result.txt"

    with open(output_file, "w", encoding="utf-8") as file:
        for number, book in enumerate(selected, start=1):
            author = book["Book-Author"].strip()
            title = book["Book-Title"].strip()
            year = book["Year-Of-Publication"].strip()
            file.write(f"{number}. {author}. {title} - {year}\n")

    print(f"Bibliographic references saved to: {output_file.name}")


def unique_tags(books):
    # For books-en.csv, the extra task asks for unique publishers.
    publishers = set()

    for book in books:
        publisher = book["Publisher"].strip()
        if publisher:
            publishers.add(publisher)

    for publisher in sorted(publishers, key=str.lower):
        print(publisher)

    print("Number of unique publishers:", len(publishers))


def popular_books(books):
    # Sum Downloads for rows with the same book title.
    popularity = {}

    for book in books:
        title = book["Book-Title"].strip()
        downloads_text = book["Downloads"].strip()

        try:
            downloads = int(downloads_text or 0)
        except ValueError:
            downloads = 0

        popularity[title] = popularity.get(title, 0) + downloads

    sorted_books = sorted(
        popularity.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("20 most popular books (by Downloads):")
    for number, (title, downloads) in enumerate(sorted_books[:20], start=1):
        print(f"{number}. {title} — {downloads} downloads")
