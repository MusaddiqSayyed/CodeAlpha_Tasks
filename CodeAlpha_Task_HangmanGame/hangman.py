import random

words = ["python", "apple", "banana", "computer", "hangman"]
secret_word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_guesses:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)

    if "_" not in display_word:
        print("Congratulations! You won 🎉")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in secret_word:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        guessed_letters.append(guess)
        incorrect_guesses += 1
        print("Wrong guess!")

if incorrect_guesses == max_guesses:
    print("\nYou lost 😢")
    print("The correct word was:", secret_word)