import random

hangman = [
    """
     +---+
     |   |
         |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========
    """,
]
words = [
    "apple",
    "mountain",
    "python",
    "keyboard",
    "sunshine",
    "elephant",
    "garden",
    "rocket",
    "window",
    "adventure",
    "computer",
    "diamond",
    "football",
    "rainbow",
    "butterfly",
    "chocolate",
    "building",
    "journey",
    "knowledge",
    "friendship",
    "telephone",
    "watermelon",
    "universe",
    "programming",
    "discovery",
    "ocean",
    "library",
    "thunder",
    "pencil",
    "village",
    "forest",
    "calendar",
    "bicycle",
    "medicine",
    "festival",
    "language",
    "question",
    "solution",
    "creative",
    "imagination",
    "success",
    "picture",
    "engineer",
    "computer",
    "breakfast",
    "beautiful",
    "education",
    "challenge",
    "important",
    "experience",
]

word = random.choice(words)

to_guess = ""
for position in range(len(word)):
    to_guess += "_"
    

print(f"word to guess: {to_guess}\n")
print(f"the word has {len(word)} letters. \n")


game_over = False
correct = []
count = 0
live = 6
print(f"You have {live} lives.\n")
while not game_over:
    guess = input("enter the letter of your guess: \n").lower()

    display = ""

    for letter in word:
        if letter == guess:
            display += letter
            correct.append(letter)
        elif letter in correct:
            display += letter
            correct.append(letter)
        else:
            display += "_"

    print(display)

    if guess not in word:
        count += 1
        live -= 1
        if live == 0:
            game_over = True
            print(f"You lose. The word was {word}\n")
    print(hangman[count])
    print(f"You have {live} lives.\n")

    if "_" not in display:
        print(f"You guess the correct word right. You won.\n")
        game_over =  True
