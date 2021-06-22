word = "Avengers"
user_word = ""
count = 0
no_of_guess = 3
out_of_guess = False
while word != user_word and out_of_guess == False:
    if count != no_of_guess:
        user_word = input("Enter a word:")
        if word == user_word:
            print("You win !!")
            break
        print("Try again !!")
        count += 1
    else:
        out_of_guess = True
        print("Out of guesses. You Lost")