from stats import get_book_word_count
from stats import count_characters
import sys

def get_book_text(file_path):
    file_contents = None
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(word_count, character_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count -----")

    for entry in character_list:
        if entry["character"].isalpha():
            print(f"{entry["character"]}: {entry["count"]}")
    
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    word_count = get_book_word_count(book_text)
    character_list = count_characters(book_text)
    
    print_report(word_count, character_list)

main()