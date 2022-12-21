import random

# The list of words or phrases for the game
words = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
    "mango",
    "nectarine",
    "orange",
    "peach",
    "plum",
    "raspberry",
    "strawberry",
    "watermelon",
]

# The list of taboo words for each word or phrase
taboos = [
    ["fruit", "red", "round"],
    ["fruit", "yellow", "banana-shaped"],
    ["fruit", "red", "cherry-shaped"],
    ["fruit", "brown", "sweet"],
    ["fruit", "purple", "berry"],
    ["fruit", "green", "pear-shaped"],
    ["fruit", "green", "grape-shaped"],
    ["fruit", "green", "melon"],
    ["fruit", "brown", "fur"],
    ["fruit", "yellow", "lemon-shaped"],
    ["fruit", "orange", "tropical"],
    ["fruit", "orange", "peach-shaped"],
    ["fruit", "yellow", "peach-shaped"],
    ["fruit", "purple", "plum-shaped"],
    ["fruit", "red", "berry"],
    ["fruit", "red", "berry"],
    ["fruit", "green", "melon"],
]

# The number of points needed to win the game
win_score = 5

# The current score for each team
scores = [0, 0]

# The current team and player
team = 0
player = 0

# The main game loop
while True:
    # Choose a random word or phrase
    word = random.choice(words)
    taboo_words = taboos[words.index(word)]

    # Print the word or phrase to the clue giver
    print(f"Team {team + 1}, player {player + 1}, your word is: {word}")

    # Print the taboo words to the clue giver
    print("Taboo words:")
    for taboo_word in taboo_words:
        print(taboo_word)

    # Get the clues from the clue giver
    clues = input("Enter your clues, separated by commas: ")

    # Split the clues into a list
    clue_list = clues.split(", ")

    # Print the clues to the guessers
    print("Clues:")
    for clue in clue_list:
        print(clue)

    # Get the guess from the guessers
    guess = input("Enter your guess: ")

    # Check if the guess is correct
    if guess.lower() == word.lower():
        # Update the score and print a message
        scores[team] += 1
        print(f"Correct! The score is now {scores[0]} to {scores[1]}")
    else:
        # Give the other team a chance to steal
        print("Incorrect! The other team has a chance to steal.")
        guess = input("Enter your guess: ")
        if guess.lower() == word.lower():
            scores[(team + 1) % 2] += 1
            print(f"Correct! The score is now {scores[0]} to {scores[1]}")
        else:
            print("Incorrect.")

    # Switch to the other team and player
    team = (team + 1) % 2
    player = (player + 1) % 2

    # Print the final score
    print(f"The final score is {scores[0]} to {scores[1]}")

    # Print the winning team
    if scores[0] > scores[1]:
        print("Team 1 wins!")
    elif scores[1] > scores[0]:
        print("Team 2 wins!")
    else:
        print("The game is a tie.")
