def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    word_count = get_word_count(text)
    character_counts = get_character_counts(text)
    generate_report(book, word_count, character_counts)


def get_book_text(book):
    with open(book) as file:
        file_contents = file.read()

    return file_contents

def get_word_count(text):
    return len(text.split())

def get_character_counts(text):
    char_counts = {}
    for char in text:
        char_lower = char.lower()
        if not char_counts.get(char_lower):
            char_counts[char_lower] = 1
        else:
            char_counts[char_lower] += 1
    return char_counts

def sort_character_counts(character_counts):
    sorted_char_list = [i for i in character_counts.items() if i[0].isalpha()]
    sorted_char_list.sort(reverse=True, key=sort_on)
    return sorted_char_list

def generate_report(book, word_count, character_counts):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")
    print("")

    sorted_char_list = sort_character_counts(character_counts)
    for ch in sorted_char_list:
        print(f"The '{ch[0]}' character was found {ch[1]} times")

    print("--- End report ---")

def sort_on(item):
    return item[1]

main()
