from hashlib import new
import random

with open("words.txt") as words_txt:
    word_options = words_txt.read()

def gamePrompt():
    split_words = list(map(str, word_options.split()))
    randomize_word = (random.choice(split_words))
    # random_word = "carrot"
    print(randomize_word)
    split_letters = list(randomize_word)
    word_length = (len(split_letters))
    print(word_length)
    # word_selection = "_" * len(randomize_word)
    # print (word_selection)
    # input_letter = input("Make a guess: ")
    # print(input_letter)
    # dict = {}
    # dict["c"] = 1
    # print(dict)

    # for letter of words:
        # print(randomword)
        #input("Your Guess " )
        # word_selection = "_" * len(words)

gamePrompt()