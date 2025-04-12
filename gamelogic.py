import random

def load_words():
    with open("words.txt") as file:
        return [word.rstrip() for word in file if word.strip()]


def pick_random_word():
    words = load_words()
    return random.choice(words)


def jumble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def check_guess(actual_word, user_guess):
    return user_guess.lower() == actual_word.lower()