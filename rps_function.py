import random
def game():
    human_guess = input('choose r for rock, p for paper, s for scissors: ')
    computer_guess = random.choice(['r', 'p', 's'])
    if (human_guess == 'r' and computer_guess == 's') or (human_guess == 's' and computer_guess == 'p')\
    or (human_guess == 'p' and computer_guess == 'r'):
        return 'you win'
    elif human_guess == computer_guess:
        return 'tie'
    else:
        return 'you lost'
print(game())
