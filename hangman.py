#hangman allows maximum 6 tries

#lets first define a list of words
word_list = ['python', 'pizza', 'java', 'fern', 'javascript', 'truffle', 'muse', 'hangman', 'godot', 'gofer', 'cryengine', 'unity', 'blender', 'google', 'firefox', 'chatgpt', 'youtube', 'netflix', 'retro', 'synthwave', 'cheez']

#now to guess a word from this list we need to import random module
import random

word = random.choice(word_list)

#now its our turn to guess the word
#we need to have a list where we store our guessed letters

letters = set(word)
correct_guesses = []
wrong_guesses = 0
attempts = 6
guess = input('guess the letter: ')
complete_word = set(correct_guesses)

#we also need to print dashes for the number of letters

hangman_word = ' - ' * len(word)
print(hangman_word)
while (letters != complete_word) and (attempts > wrong_guesses):
    if guess in letters:
        correct_guesses.append(guess)
        letters.remove(guess)
        print(correct_guesses)
        guess = input('correct! a few more letters left: ')
    else:
        wrong_guesses+= 1
        print(f'wrong guesses: {wrong_guesses}')
        guess = input('try again: ')
    if letters == complete_word:
        print('you did it!')
          
print(f'the word was: {word}')




