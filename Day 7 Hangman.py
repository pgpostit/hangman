#Modules
import random
from hangman_art import stages, logo
from hangman_words import word_list

#Display Function
def print_display(display):
    for space in display:
        print(space, end=' ')
    print('')

#Parameters and game basic structure
life = 6
game_over = False
word = random.choice(word_list)
display = []
for letter in word:
    display.append('_')

#Interactire display
print(logo)
print(f'The word is: {word}')     #To test your code. If you want to play, delete this line.
print_display(display)


#Main Program
while game_over == False:
    guess = input('Guess a letter: ').lower()
    if len(guess) == 1:
        if guess.isalpha() == True:
            if guess in word:
                for i in range(len(word)):
                    char = word[i]
                    if char == guess:
                        print('Right guess!')
                        display[i] = char
                        print_display(display)
                        if '_' not in display:
                            print(f'You win! Remaining lives: {life}')
                            game_over = True
            else:
                print(f'You guessed {guess}! So wrong... Lost a life.')
                life-=1
                print(stages[life+1])
                if life == -1:
                    print('You lost!')
                    game_over = True
                else:
                    print(f'Lives: {life}')
                    print_display(display)
        else:
            print('Only letters, please.')
    else:
        print('Only 1 letter at time.')

