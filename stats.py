def count_words(book_text):
    words = book_text.split()
    num_words = 0
    for word in words:
        num_words += 1
    return num_words

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
    return letters

def sort_on(items):
    return items["num"]

def sort_letters(letters):
    letter_dict = {"char": "", "num": 0}
    letters_dicts = []
    for k, v in letters.items():
        if k.isalpha():
            letter_dict = {"char": k, "num": v}
            letters_dicts.append(letter_dict)
    letters_dicts.sort(reverse=True, key=sort_on)
    return letters_dicts