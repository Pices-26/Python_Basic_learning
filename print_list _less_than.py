'''
this will print all the nubers that are less than 5 from the list
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
print(a[:])
for i in a:
    if i <=10:
        b.append(i)

    else:
        break

number = int(input('enter a max number'))
for i in a[:]:
    if a[i] <= number:
        print(a[i])
    else:
        break
print(b[:])