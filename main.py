def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        print(word_count(file_contents))

def word_count(text):
    return len(text.split())

main()
