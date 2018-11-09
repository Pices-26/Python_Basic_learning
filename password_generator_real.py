import random
b = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']
a = []
i = 0
l = 1
chr(l)
print('hello, I will generate a password for you: ')
l = int(input('how many letters would you like to have? : '))

while i <= l:
    letter = random.choice(b)
    a[i].append(letter)
    i = i + 1
print(a)
