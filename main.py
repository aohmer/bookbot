from stats import count_words, count_letters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    count_words(get_book_text("books/frankenstein.txt"))
    count_letters(get_book_text("books/frankenstein.txt"))
main()