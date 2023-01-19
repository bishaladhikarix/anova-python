import random
gnumber = random.randint(0,9)
guess_count = 0
guess_limit = 3

print('Guess a number between 0 to 9 if you guess correctly you win! You have 3 chance :) ')

while guess_count < guess_limit:
    guess = int(input("Guess the number : "))
    guess_count += 1
    if guess == gnumber:
        print('Dyam Bradha how did you do daht!!!')

        break
    else:
        print('Incorrect!!')
else:
    print("Your chances are over YOU LOST!!! LOSER ")
    print('The numer was: ' , gnumber)

