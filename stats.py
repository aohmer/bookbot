def count_words(book_text):
    words = book_text.split()
    num_words = 0
    for word in words:
        num_words += 1
    print(f"{num_words} words found in the document")

def count_letters(book_text):
    letters = {}
    words = book_text.split()
    for word in words:
        for letter in word:
            letter = letter.lower()
            if not letter in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
    print(letters)