def get_book_text(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file '{filepath}' not found."
    
def count_words(text):
    
    if text is None: # Handle cases where get_book_text might have returned None
        return 0
    words = text.split() # Splits the string by whitespace into a list of words
    return len(words)

def main():
    frankenstein_path = "frankenstein.txt"
    book_content = get_book_text(frankenstein_path)

    if book_content is not None:
        word_count = count_words(book_content)
        # Print the specified message
        print(f"{word_count} words found in the document.")
    else:
        print(f"Could not process the book: '{frankenstein_path}' not found or an error occurred.")


if __name__ == "__main__":
    main()