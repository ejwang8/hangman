from curses.ascii import isalpha
import random

def generalScraper(): # have not implemented yet
    return None

def movieScraper():
    return None

def musicScraper():
    return None

def findIndexes(guess, choice):
    if guess not in choice:
        return None
    return [i for i in range(len(choice)) if choice[i]==guess]

print("\n\t\t~ ~ ~ ~ ~ ~ ~ Welcome to Hangman ~ ~ ~ ~ ~ ~ ~\n")
response = input("Would you like to play (y/anything else = no)? ")
if response != 'y':
    quit()

category = input("Would you like to pick a category (general, movies, music)? ")
words = None
if category == 'general':
    print("\nYou have selected General.\n")
    words = generalScraper()
elif category == 'movies':
    print("\nYou have selected Movies.\n")
    words = movieScraper()
elif category == 'music':
    print("\nYou have selected Music.\n")
    words = musicScraper()
else:
    print("Not a valid answer. Picking general by default.")
    words = generalScraper()

words = ["bear", "adieu", "wordle", "hello", "wordle", "fear the tree", "ella"]
randomIndex = random.randint(1, len(words)) - 1
choice = words[randomIndex]
phrase = choice.split(" ")
wordProgress = []
for word in phrase:
    wordProgress += ["_"] * len(word)
    wordProgress += [" "]
guesses = set()
hangman = "\n"
limbs = ["\t\t  O\n", "\t\t  |\n", "\t\t---", "--\n", "\t\t  |\n\t\t /", " \x5c"]

win = False
wrongGuesses = 0
while "_" in wordProgress and wrongGuesses < 6:
    print()
    print(" ".join(wordProgress))
    guess = input("\nPick your next letter or type 'quit' to quit: ")
    print("You guessed " + guess + ".")

    if guess == 'quit':
        quit()
    elif not guess.isalpha() or len(guess)!=1:
        print("\nPlease guess a valid single letter.")
        continue
    
    indices = findIndexes(guess, choice)
    print("indices", indices)

    if guess in guesses:
        print("You have already guessed this letter.")
        continue
    guesses.add(guess.lower()) # track guessed letters
    if indices is None: # wrong
        hangman += limbs[wrongGuesses]
        print(hangman)
        wrongGuesses += 1
    else: # correct
        for i in indices:
            wordProgress[i] = guess.lower()

if wrongGuesses < 6:
    print("\n\t\t~ ~ ~ ~ ~ ~ ~ You win! The word was", word, "~ ~ ~ ~ ~ ~ ~\n")
else:
    print("\n\t\tYou lose.\n")