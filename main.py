def main():
    words = 0
    letters = {}

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words += len(file_contents.split())
        letters = {}

        for c in file_contents.lower():
            if not c.isalpha():
                print(c)
                continue
            if not c in letters:
                letters[c] = 0
            letters[c] += 1
        
    letters = dict(sorted(letters.items(), key=lambda x: x[1], reverse=True))
    print(f"{words} comprise this document")
    for c in letters:
        print(f"The letter {c} appears {letters[c]} in this document")

main()
