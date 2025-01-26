def read_and_print_file (file):
    with open(file) as f:
        file_contents = f.read()
        # print(file_contents)
    return file_contents

def word_count (book):
    words = book.split()
    return len(words)

def character_count (book):
    characters_string = book.lower()
    # print(characters_string)
    characters_count = {}
    for character in characters_string:
        if character in characters_count:
            characters_count[character]+=1
        else:
            characters_count[character] = 1
    return characters_count

def create_report (file, file_path):
    num_words = word_count(file)
    characters_count = character_count(file)
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    print(f"Begin Report on {file_path}:\nNumber of words: {num_words}\n",
          )
    for character in characters_count:    
        if character in alphabet:
            print(f"{character} is in the book {characters_count[character]} times." )

def main ():
    file_contents = read_and_print_file("books/frankenstein.txt")
    create_report(file_contents, "books/frankenstein.txt")

main()