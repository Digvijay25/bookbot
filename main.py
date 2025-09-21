import sys 
from stats import get_num_words, get_character_count, sorted_dictionary

def get_book_text(PATH):
    with open(PATH) as f:
        file_contents = f.read()
        
    return file_contents
  

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(sys.argv)
    PATH = sys.argv[1]
    contents = get_book_text(PATH)
    d = get_character_count(contents)
    sorted_dict = sorted_dictionary(d)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(contents)} total words")
    print("--------- Character Count -------")
    for i in sorted_dict: 
        print(f"{i['char']}: {i['num']}")
        
    print("============= END ===============")
    
main()

    