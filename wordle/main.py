import wordsFetcher
import random

words = wordsFetcher.fetch_words(min_letters=5, max_letters=5)
# choose a random word from the list;
word = words[random.randrange(0, len(words))]
counter = 0
while counter < 6:
    userInput = input("Enter a word, 5 letters: ")
    output = ""
    for j in range(5):
        if userInput[j] == word[j]:
            output += userInput[j].upper() + " "
        elif userInput[j] in word and userInput[j] != word[j]:
            # if there's only one such letter within userInput;
            if userInput[j+1:].find(userInput[j]) == -1:
                output += userInput[j] + "*" + " "
            # the letter occurs within userInput more than once;
            else:
                doubleInput = userInput[j+1:]
                doubleIndex = doubleInput.find(userInput[j])
                slicedWord = word[j+1:]
                while doubleIndex != -1:
                    # the 2nd occurrence was not guessed right;
                    if slicedWord.find(userInput[j]) != doubleIndex:
                        output += userInput[j] + "*" + " "
                        break
                    doubleInput = doubleInput[doubleIndex+1:]
                    slicedWord = slicedWord[doubleIndex+1:]
                    doubleIndex = doubleInput.find(userInput[j])
                if doubleIndex == -1:
                    output += userInput[j] + " "
        # the letter is not within the word;
        else:
            output += userInput[j] + " "
    print(output)
    if output.isupper():
        print("Congrats!")
        break
    counter += 1

if userInput != word:
    print("Loss, word:", word)
