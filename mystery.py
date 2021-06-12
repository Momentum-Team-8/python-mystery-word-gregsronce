import random

with open("words.txt") as words_txt:
    word_options = words_txt.read()

def gamePrompt():
    # split_words = list(map(str, word_options.split()))
    # split_letters = list(random_word)
    # print(split_letters)
    # tries = 0
    # while tries > 10:
    # word_selection = "_" * word_length
    # split_words = random_words.split(' ')
    number_of_guesses = 8
    random_words = ["carrot", "goal"]
    random_word = random.choice(random_words)
    word_length = (len(random_word))
    guesses = []
   
        for letter in random_word:
            guesses.append('_')
        input_letter = str(input("Make a guess: "))
        if input_letter in random_word:
            print("Correct")
            for letter in range(word_length):
                if input_letter == random_word[letter]:
                    guesses[letter] = random_word[letter]
                    print(guesses)
        else: 
            print("Sorry, guess again")
            number_of_guesses -= 1 
        input_letter = input_letter.strip()


    
    # guesses += input_letter 
    # print(guesses)
    # print(type(input_letter))

    # if the input letter number corresponds to the space number, then replace space with input letter. 
        
    # letter_list[0].replace("_", input_letter)
    # # word_selection[0] += input_letter
    # print(letter_list)


    # for letter of words:
        # print(randomword)
        #input("Your Guess " )
        # word_selection = "_" * len(words)

gamePrompt()