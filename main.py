from stats import count_words, count_letters, sort_letters
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    letter_dict = sort_letters(count_letters(text))
    # count_words(get_book_text("books/frankenstein.txt"))
    # print(count_letters(get_book_text("books/frankenstein.txt")))
    # print(sort_letters(count_letters(get_book_text("books/frankenstein.txt"))))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for letter in letter_dict:
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")
main()