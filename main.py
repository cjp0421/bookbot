def read_and_print_file (file):
    with open(file) as f:
        file_contents = f.read()
        print(file_contents)
    return file_contents

def word_count (book):
    words = book.split()
    return len(words)

def main ():
    file_contents = read_and_print_file("books/frankenstein.txt")
    num_words = word_count(file_contents)
    print("Number of words: ", num_words)


main()