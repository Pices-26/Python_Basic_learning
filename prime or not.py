def prime_or_not(usr_input):
    i = 0
    counter = 1
    while counter >= usr_input:
        ans = usr_input % counter
        if counter == usr_input:
            i = i + 1
    if i == 2:
        return(1)
    else:
        return(0)

ans = 1
counter = 1
result = 8
usr_input = int(input('pleas enter a number and I will tell you if it is prime or not: ')

output = prime_or_not(usr_input)
if output == 1:
    print('number is prime')
else:
    print('number is not prime')


