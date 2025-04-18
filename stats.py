def get_book_word_count(book):
    return len(book.split())


def sort_on(dict):
    return dict["count"]

def sort_character_count(characters):
    sorted_list = []
    for key, value in characters.items():
        sorted_list.append({"character": key, "count": value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

def count_characters(book):
    characters = {}
    lower_book = book.lower()
    for word in lower_book.split():
        for letter in word:
            if letter not in characters:
                characters[letter] = 1
            else:
                characters[letter] += 1
    return sort_character_count(characters)
            