# Hangman Game

## Description
The Hangman Game is a Python-based interactive game where players guess letters to complete a hidden word or phrase within a limited number of attempts. This particular version of the game includes categories such as movies and music, offering word options based on these themes.

## How to Play
1. Run the Python script `hangman.py`.
2. You'll be prompted to choose a category: movies or music.
3. Guess letters to reveal the hidden word or phrase.
4. You have six attempts to guess the word correctly before the game ends.

## Features
- Two categories: movies and music.
- Data scraped dynamically from:
  - [IMDb for Movies](https://www.imdb.com/list/ls055592025/)
  - [Billboard for Music](https://www.billboard.com/charts/hot-100/)
- Interactive gameplay with a hangman interface.

## Usage
1. Open a terminal or command prompt.
2. Run the game:
    ```
    python hangman.py
    ```
3. Follow the on-screen instructions to play the game.

## Game Logic
The game randomly selects a word or phrase from the chosen category. Players guess letters, and if the letter is in the word or phrase, it gets revealed. Otherwise, the hangman figure starts to form. Players win if they guess the word or phrase within six incorrect attempts.

## Dependencies
- [Requests](https://pypi.org/project/requests/): For making HTTP requests.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): For web scraping.