import random

word_list = ['dileep','divya','archana']


chosen_word = random.choice(word_list)
print(f"the slotution is: {chosen_word}")
#ask user to guess the word

display = []
world_length = len(chosen_word)
for _ in range(world_length):
    display += '-'
    
print(display)
guess = input("Guess a word: ").lower()


for position in range(world_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter


print(display)
