def count_words(contents):
    """Receives a string (a book) and prints the amount of words in it"""
    words = contents.split()
    print(f"{len(words)} words found in the document")

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
    for char in sorted_chars:
        print(f"{char}: {sorted_chars[char]}")