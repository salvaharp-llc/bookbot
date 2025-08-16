import sys
from stats import (
    count_words,
    count_characters,
    dict_to_sorted_list,
)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    
    text = get_book_text(path)
    num_words = count_words(text)
    ch_count = count_characters(text)
    ch_list = dict_to_sorted_list(ch_count)
    print_report(path, num_words, ch_list)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(path, num_words, ch_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for ch in ch_list:
        if ch["char"].isalpha():
            print(f"{ch["char"]}: {ch["num"]}")
    print("============= END ===============")


main()