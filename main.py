import sys
from stats import *

def args():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    path = sys.argv[1]
    contents = get_book_text(path)
    word_count = get_word_count(contents)
    char_freq = get_char_freq(contents)
    sorted = sort_freq(char_freq)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for symbol in sorted:
        if symbol["char"].isalpha():
            key = symbol["char"]
            val = symbol["freq"]
            print(f"{key}: {val}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

args()
main()