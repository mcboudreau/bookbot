import sys

from stats import get_num_words, get_char_count, sort_char

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def main():
    file = sys.argv[1]
    book = get_book_text(file)
    num_words = get_num_words(book)
    char_dict = get_char_count(book)
    sorted_char_dict = sort_char(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for count in sorted_char_dict:
        print (f"{count["char"]}: {count["count"]}")
    print("============= END ===============")

main()
