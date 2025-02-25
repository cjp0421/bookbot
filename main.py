from stats import word_count
import sys

def read_and_print_file (file):
    with open(file) as f:
        file_contents = f.read()
        # print(file_contents)
    return file_contents

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

def sort_on(dict):
    return dict["num"]

def create_report (file, file_path):
    num_words = word_count(file)
    characters_count = character_count(file)
    letter_count_only = list()
    print(f"--- Begin Report on {file_path} ---\n{num_words} words found in the document\n",
          )
    for character in characters_count:
        letter_combo = {}
        if character not in letter_count_only:
            if character.isalpha():
                letter_combo["name"] = character
                letter_combo["num"] = characters_count[character]
                letter_count_only.append(letter_combo)
    letter_count_only.sort(reverse=True, key=sort_on)
    for letter_count in letter_count_only:
        # print(f"The '{letter_count['name']}' character was found {letter_count['num']} times")
        print(f"{letter_count['name']}: {letter_count['num']}")

def main ():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = read_and_print_file(sys.argv[1])
    create_report(file_contents, sys.argv[1])

main()