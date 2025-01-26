

def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        num_words = word_count(file_contents)
        print("Number of words: ", num_words)
def word_count (book):
    words = book.split()
    return len(words)

main()