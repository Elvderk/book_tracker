import json
from collections import Counter

BOOKS_FILE = "books.json"


# Загрузка книг

def load_books():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Сохранение книг

def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

# Добавление книги

def add_book(books):
    author = input("Введите автора: ").strip()
    title = input("Введите название книги: ").strip()

    # Проверка дубликатов
    for book in books:
        if (
            book["author"].lower() == author.lower()
            and book["title"].lower() == title.lower()
        ):
            print("Такая книга уже существует.")
            return

    while True:
        try:
            rating = int(input("Введите оценку (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Оценка должна быть от 1 до 5")
        except ValueError:
            print("Введите число")

    read_date = input("Введите дату прочтения: ").strip()

    new_book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date": read_date,
    }

    books.append(new_book)
    save_books(books)

    print("Книга успешно добавлена")



if __name__ == "__main__":
    main()