def get_book_text(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file '{filepath}' not found."

def main():
    frankenstein_path = "frankenstein.txt"
    book_text = get_book_text(frankenstein_path)
    print(book_text)

if __name__ == "__main__":
    main()

