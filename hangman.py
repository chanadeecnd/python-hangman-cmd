import random
import hangman_art
import hangman_word

HANGMAN = hangman_art.HANGMAN
STATE = hangman_art.STATE

print(HANGMAN)
word_list = hangman_word.words
random_word = random.choice(word_list)
chosen_word = str(random_word)
print(random_word)
life_over = 0
state = 0
len_word = len(random_word)


blanks = []
for blank in random_word:
    blanks.append("_")
print(blanks) # ['_', '_', '_', '_', '_']

while "_" in blanks and state <= 5:
    print(STATE[state])
    user_find = False
    user_input = str(input(">>guess a letter : ")).lower()
    for position in range(len_word):
        if blanks[position] != "_":
            continue
        letter = chosen_word[position]
        if letter == user_input:
            blanks[position] = letter
            user_find = True
            break
    if not user_find:
        state += 1
        print(state)

    print(blanks)
print(STATE[state])
result = "Game Over." if state >= 6 else "You Win!"
print(result)
