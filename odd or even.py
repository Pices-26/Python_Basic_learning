number = int(input('enter a number to check if even or odd'))
outcome = 0

outcome = number % 2
if outcome == 0:
    print('this number is even')

else:
    print('this number is odd')
