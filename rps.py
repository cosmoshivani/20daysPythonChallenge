#without using function

import random
import time

#Rock beats scissors and loses to paper
#Scissors beat paper but loses to rock
#Paper beats rock, but loses to scissors

human_guess = input('rock, paper, or scissors: ')
computer_guess = random.choice(['rock', 'paper', 'scissors'])
print(human_guess)
time.sleep(0.5)
print(computer_guess)
time.sleep(0.5)

for i in range(5):
    if (human_guess == 'rock' and computer_guess == 'scissors') or (human_guess == 'scissors' and computer_guess == 'paper') or (human_guess == 'paper' and computer_guess == 'rock'):
        print('You win')
    elif (human_guess == 'rock' and computer_guess == 'paper') or (human_guess == 'paper' and computer_guess == 'scissors') or (human_guess == 'scissors' and computer_guess == 'rock'):
        print('You lose')
    elif human_guess == computer_guess:
        print('Tie')
    time.sleep(0.5)
    answer = input('try again?: ')
    if answer == 'y':
        time.sleep(0.5)
        human_guess = input('rock, paper, or scissors: ')
        computer_guess = random.choice(['rock', 'paper', 'scissors'])
        print(human_guess)
        time.sleep(0.5)
        print(computer_guess)
        time.sleep(0.5)
    else:
        time.sleep(0.5)
        print('thanks for playing')
    
