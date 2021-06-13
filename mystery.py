import random

''' Read and open wordlist, divide words into easy, normal, and hard for player to select.'''

with open("wordlist.txt") as words_txt:
    word_options = words_txt.read().lower().split()
    easy_words = []
    normal_words = []
    hard_words = []
    for word in word_options:
        if 4 <= len(word) <= 6:
            easy_words.append(word)
        elif 6 <= len(word) <= 8:
            normal_words.append(word)
        elif len(word) > 8:
            hard_words.append(word)

''' Instructions for user to choose level of difficulty at beginning of the program. 
Call on word from new lists based on difficulty selection '''

def set_up():
    print("\nMystery Word Game\n")
    print("Pick a level to start a new game \nEnter (1) for Easy, (2) for Normal, or (3) for Hard")
    level = input("Select a level: ")
    return level

def grab_word(level):
    if level == "1":
        word_Choice = random.choice(easy_words)
    elif level == "2":
        word_Choice = random.choice(normal_words)
    elif level == "3":
        word_Choice = random.choice(hard_words)
    return word_Choice

def begin_game():
    level = (set_up())
    word = (grab_word(level))
    word_length = (len(word))
    guesses = []
    actual_guesses = []
    number_of_guesses = 0
    print("Your word length is ", word_length, " letters long." )
    print(word)
    # input_letter = str(input("Make a guess: ").lower())
    while number_of_guesses != 8:
        for letter in word:
            guesses.append('_')
            actual_guesses.append('_')
        input_letter = str(input("Make a guess: "))
        if input_letter in word:
            print("Correct")
            for letter in range(word_length):
                if input_letter == word[letter]:
                    guesses[letter] = word[letter]
                    actual_guesses[letter] = word[letter]
                    print(" ".join(guesses))
                    print(" ".join(actual_guesses))
    

begin_game()
