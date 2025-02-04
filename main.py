def open_file(path):    
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(contents):
    """Receives a string (a book) and prints the amount of words in it"""
    words = contents.split()
    print(f"Amount of words: {len(words)}")

def count_characters(contents):
    """Receives a string (a book) and prints how many letters are found in the book"""
    characters = {}
    contents = contents.lower() # Case-insensitive is needed
     
    for char in contents:
        if char.isalpha():      # Checks that character is a letter: we don't want to count other chars.
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1 
    
    # Sort by number of ocurrences
    sorted_chars = {k:v for k,v in sorted(characters.items(), reverse=True,key = lambda item:item[1])}
    [print(f"The '{char}' character was found {sorted_chars[char]} times") for char in sorted_chars]


def main():
    book = 'frankenstein'                       # Book to analyze
    print(f'---Begin Report of "{book}"---')
    path_to_file = "books/" + book +".txt"
    contents = open_file(path_to_file)
    count_words(contents)
    count_characters(contents)
    print(f"End report")

if __name__ == "__main__":
    main()