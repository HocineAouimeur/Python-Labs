from resources import (
    read_books,
    count_titles,
    search_author,
    make_references,
    unique_tags,
    popular_books,
)
from xml_reader import read_currencies


def main():
    try:
        books = read_books()
    except FileNotFoundError:
        print("Error: books-en.csv must be in the same folder as lab2.py.")
        return
    except (KeyError, UnicodeError, ValueError) as error:
        print("Could not read books-en.csv:", error)
        return

    while True:
        print("\\n--- LAB-2: VARIANT 1 ---")
        print("1. Count titles longer than 30 characters")
        print("2. Search books by author (price up to 150 rubles)")
        print("3. Generate 20 random bibliographic references")
        print('4. Read currencies from XML ("Name - Value")')
        print("5. Show unique publishers (extra task)")
        print("6. Show 20 most popular books (extra task)")
        print("0. Exit")

        choice = input("Choose a task: ").strip()

        if choice == "1":
            count_titles(books)
        elif choice == "2":
            search_author(books)
        elif choice == "3":
            make_references(books)
        elif choice == "4":
            try:
                read_currencies()
            except FileNotFoundError:
                print("Error: currency.xml must be in the same folder as lab2.py.")
            except (ValueError, IndexError) as error:
                print("Could not parse currency.xml:", error)
        elif choice == "5":
            unique_tags(books)
        elif choice == "6":
            popular_books(books)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 0–6.")


if __name__ == "__main__":
    main()
