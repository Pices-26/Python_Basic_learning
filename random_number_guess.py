import random

num = (random.randint(0 , 10))
guess = 1
while guess != num:
    guess = int(input('enter a number'))
    if guess > num:
        print('the number you have entered is smaller')
    else:
        print('the number you have entered is bigger')
print('you have entered the right number')
