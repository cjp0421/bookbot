def read_and_print_file (file):
    with open(file) as f:
        file_contents = f.read()
        print(file_contents)
    return file_contents

def word_count (book):
    words = book.split()
    return len(words)

def character_count (book):
    characters_string = book.lower()
    print(characters_string)
    characters_count = {}
    for character in characters_string:
        if character in characters_count:
            characters_count[character]+=1
        else:
            characters_count[character] = 1
    return characters_count


def main ():
    file_contents = read_and_print_file("books/frankenstein.txt")
    num_words = word_count(file_contents)
    print("Number of words: ", num_words)
    print(character_count(file_contents))


main()