from importlib.machinery import WindowsRegistryFinder
import random

print("Welcome to Hangman")
response = input("Would you like to play? (y/n)")
if response != 'y':
    quit()

words = ["bear", "adieu", "wordle", "hello", "wordle", "fear the tree"]
randomIndex = random.randint(1, len(words)) - 1
word = words[randomIndex]
print(word)
