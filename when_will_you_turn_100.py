#this will tell you when you will turn 100
name = input('input your name: ')
age = int(input('input your age: '))
year = int(input('what is the year? \n '))
add_age = 0
will_turn = 0

add_age = 100 - age
will_turn = year + add_age
print(name + ' you will turn 100 in:' + str(will_turn))

