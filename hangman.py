import random
from replit import clear
import hangman_art
import hangman_word

HANGMAN = hangman_art.HANGMAN
STATE = hangman_art.STATE

word_list = hangman_word.words
random_word = random.choice(word_list)
chosen_word = str(random_word)
life_over = 0
state = 0
len_word = len(random_word)


blanks = []
for blank in random_word:
    blanks.append("_")

def displayBlank(blanks):
    for blank in blanks:
        print(blank, end=' ')
    print('\n')


while "_" in blanks and state <= 5:
    clear()
    print(HANGMAN)
    try:
        find = f'You\'ve already guessed {user_input}' if user_find else f'You guessed {user_input}, that\'s not in the word. You lose a life.'
        print(find)
    except NameError:
        None
    print(random_word)
    displayBlank(blanks)
    print(STATE[state])
    user_input = str(input(">>guess a letter : ")).lower()
    user_find = False
    for position in range(len_word):
        if blanks[position] != "_":
            continue
        letter = chosen_word[position]
        if letter == user_input:
            blanks[position] = letter
            user_find = True
            print(f'You\'ve already guessed {user_input}')
            break
    if not user_find:
        state += 1
        print(f'You guessed {user_input}, that\'s not in the word. You lose a life.')

    displayBlank(blanks)
clear()
print(HANGMAN)
displayBlank(blanks)
print(hangman_art.winner)
result = "Game Over." if state >= 6 else "You Win!"
print(result)
