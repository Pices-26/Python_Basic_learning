import random
ans = ('rock', 'paper', 'scissors')
user = ''
while user is not 'enter':
    user = input('type enter to quit\notherwise input rock , paper or scissors and press enter \n good luck \n')
    pc = random.choice(ans)
    #rock
    if user == 'rock':
        if pc == 'rock':
            print('draw')
        elif pc == 'paper':
            print('you lost')
        else:
            print('you win')
    #paper
    if user == 'paper':
        if pc == 'rock':
            print('you win')
        elif pc == 'paper':
            print('draw')
        else:
            print('you lost')
    #scissors
    if user == 'scissors':
        if pc == 'rock':
            print('you lost')
        elif pc == 'paper':
            print('you win')
        else:
            print('draw')