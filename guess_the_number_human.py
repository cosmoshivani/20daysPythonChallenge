import random

#we want the computer to guess the random number that we have guessed
#and we will tell if the number the computer guessed is lower or higher
#we choose the number from one to 10
#computer will randomly choose a number from 1 to ten

num = random.randint(1, 10)
print(f"is {num} the number you guessed?")

#then we will provide an input if its correct or how high or low the number was

assist = input()
for i in range(1, 10):
    if assist == str("too low"):
        print(f"is {num+i} the number you guessed?")
        assist = input()
    elif assist == str("too high"):
        print(f"is {num-i} the number you guessed?")
        assist = input()
if assist == str("yes"):
    print("great! you guessed it correctly")


