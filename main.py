import random
import os
import sys
from hangman_words import word_list
from hangman_art import logo, stages

def clean_scean():
  try:
    from replit import clear
    clear()
  except ImportError:
    if os.name == 'nt': #for windows
      os.system('cls')
    else: #for macOS and linux
      os.system('clear')

chosen_word = random.choice(word_list)
length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

print(f"the solution is {chosen_word}.")

display = []
for _ in range(length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clean_scean()

    if guess in display:
      print(f"You've already guessed {guess}")
    
    for position in range(length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
          end_of_game = True
          print("You lose.")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])