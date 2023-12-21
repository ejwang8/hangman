from curses.ascii import isalpha
import random
import requests
from bs4 import BeautifulSoup

def generalScraper(): # have not implemented yet
    return ['Pink Birthday']

def movieScraper(): # have not implemented
    r2 = requests.get('https://www.imdb.com/list/ls055592025/')
    soup = BeautifulSoup(r2.content, 'html.parser')
    results = soup.find_all('h3', class_='lister-item-header')
    movieList = []
    for result in results:
        movieList += [' '.join(result.text.split()[1:-1])]
    return movieList

def musicScraper():
    r = requests.get('https://www.billboard.com/charts/hot-100/')
    soup = BeautifulSoup(r.content, 'html.parser')
    result = soup.find_all('div', class_='o-chart-results-list-row-container')
    musicList = []
    for res in result:
        musicList += [res.find('h3').text.strip(), res.find('h3').find_next('span').text.strip()]
    return musicList

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
if category == 'movies':
    print("\nYou have selected Movies. (Please wait while it loads)\n")
    words = movieScraper()
elif category == 'music':
    print("\nYou have selected Music.\n")
    words = musicScraper()
else:
    print("Not a valid answer. Randomly selecting category. (Please wait while it loads)")
    if random.randint(0,1) == 0:
        words = movieScraper()
    else:
        words = musicScraper()

randomIndex = random.randint(1, len(words)) - 1
originalChoice = words[randomIndex]
choice = originalChoice.lower()
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
    guess = input("\nPick your next letter or type 'quit' to quit: ").lower()

    if guess == 'quit':
        quit()
    print("You guessed " + guess + ".")
    if not guess.isalpha() or len(guess)!=1:
        print("\nPlease guess a valid single letter.")
        continue
    
    indices = findIndexes(guess, choice)

    if guess in guesses:
        print("You have already guessed this letter.")
        continue
    guesses.add(guess) # track guessed letters
    if indices is None: # wrong
        hangman += limbs[wrongGuesses]
        print(hangman)
        wrongGuesses += 1
    else: # correct
        for i in indices:
            wordProgress[i] = guess

if wrongGuesses < 6:
    print("\n~ ~ ~ You win! The answer was", originalChoice, "~ ~ ~\n")
else:
    print("\n\t\tYou lose. The answer was", originalChoice, "\n")