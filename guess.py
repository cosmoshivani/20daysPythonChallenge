#Guess the number (computer)
import random
num = int(input("guess the number between one to ten: "))
x = random.randint(1,10)
if num == x:
        print("You guessed it right!")        
atmpt = 4
for j in range(4):
    if num!= x:
        print(f"You have {atmpt-j} attempts remaining")
        num = input("guess the number: ")
print(f"the number is {x}, better luck next time")
