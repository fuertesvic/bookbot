from stats import count_words, count_characters
import sys

def open_file(path):    
    with open(path,encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]  
    print(book)                     # Book to analyze
    print(f'---Begin Report of "{book}"---')
    contents = open_file(book)
    count_words(contents)
    count_characters(contents)
    print(f"End report")

if __name__ == "__main__":
    main()