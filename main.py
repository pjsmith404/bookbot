def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        print(word_count(file_contents))
        print(character_count(file_contents))

def word_count(text):
    return len(text.split())

def character_count(text):
    char_counts = {}
    for char in text:
        char_lower = char.lower()
        if not char_counts.get(char_lower):
            char_counts[char_lower] = 1
        else:
            char_counts[char_lower] += 1
    return char_counts

main()
