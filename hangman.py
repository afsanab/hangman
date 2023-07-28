import random
from words import word_bank

#chooses random word from word_bank and returns word in all caps 
def choose_word():
    word = random.choice(word_bank)
    return word.upper()

def game(word):
    word_completion = "_" * len(word)
    won = False
    guessed_letters = []
    guessed_words = []
    tries_left = 6
    print("Let's play Hangman!")
    print(hangman_display(tries_left))
    print(word_completion)
    print("You have", tries_left, "tries\n")
    while not won and tries_left > 0:
        guess = input("Guess a letter or word:").upper()
        #letter guessed
        if len(guess) == 1 and guess.isalpha():
            #already guessed
            if guess in guessed_letters:
                print("The letter ", guess," was already guessed")
            #incorrect try
            elif guess not in word:
                print(guess, "is not in the word")
                tries_left -=1
                guessed_letters.append(guess)
            #correct letter guessed
            else:
                print("Good job", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for j in indices:
                    word_as_list[j] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    won = True
        #word guessed
        elif len(guess) == len(word) and guess.isalpha():
            #already guessed
            if guess in guessed_words:
                print("The word ", guess," was already guessed")
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                won = True
                word_completion  = word
        else:
            print("Sorry, this is not a valid guess.")
        print(hangman_display(tries_left))
        print (word_completion)
        print(" You have", tries_left, "tries left\n")
    if won:
        print("Congrats! You guessed the word, you win!")
    else:
        print("Sorry, you ran out of tries, the word was", word,".")

#list of different stages of hangman depending on number of failed tries
def hangman_display(tries_left):
    stages = [
    # Try 1
    """
          +---+
          |   |
              |
              |
              |
              |
        =========
    """,
    # Try 2
    """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
    """,
    # Try 3
    """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
    """,
    # Try 4
    """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
    """,
    # Try 5
    """
          +---+
          |   |
          O   |
        /|\\  |
              |
              |
        =========
    """,
    # Try 6
    """
          +---+
          |   |
          O   |
        /|\\  |
         /    |
              |
        =========
    """
    ]
    return stages[tries_left-5]
def main():
    word = choose_word()
    game(word)
    while input("Play Again? (Y/N) ").upper == "Y":
        word = choose_word()
        game(word)

if __name__ == "__main__":
    main()