import random
import string
from words import words


def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    word = word.upper()
    return word


def hangman():
    word = get_valid_words(words)
    # letters in the word
    letters_word = set(word)
    total_alpha = set(string.ascii_uppercase)
    # what the user has guessed
    guessed_letters = set()
    lives = 6
    print("The word starts with " + word[0] + " and ends with " + word[-1])
    while len(letters_word) > 0:
        letter_list = [letter if letter in guessed_letters else '_' for letter in word]
        print('Current word:', ' '.join(letter_list))
        # user input
        entered_letter = input("Guess a letter: ").upper()
        if entered_letter in total_alpha - guessed_letters:
            guessed_letters.add(entered_letter)
            if entered_letter in letters_word:
                letters_word.remove(entered_letter)
            else:
                lives -= 1
                print("Wrong letter is given. Hence life is lost.")
        elif entered_letter in guessed_letters:
            print("You have already guessed the letter. Try again")
        else:
            print("The character input by you is not an alphabet")
        print("You have used these letters:", ','.join(guessed_letters))
        if lives == 0:
            print("Word could not be guessed")
            break
    print("Final word:", word)


hangman()
