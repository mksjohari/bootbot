def countCharacters(words):
    counter = {}
    for char in words:
        lower = char.lower()
        if lower.isalpha() == False:
           continue
        if lower in counter:
            counter[lower] += 1
        else:
            counter[lower] = 1
    return counter

def countWords(words):
    return len(words.split())

def sort_on(value):
    return value[1]

def main(): 
    with open("./books/frankenstein.txt") as f:
        contents = f.read()
        nWords = countWords(contents)
        nCharacters = countCharacters(contents)
        sortedCharacters = list(nCharacters.items())
        sortedCharacters.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{nWords} words found in the document\n")
        for char in sortedCharacters:
            print(f"The '{char[0]}' was found {char[1]} times")
        print("--- End report ---")
main()
