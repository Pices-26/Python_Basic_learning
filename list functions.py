lucky_numbers = [2,5,7,9,5,]
friends = ['kevin', 'bob', 'steve', 'tim', 'frank', 'bob']

'''combines lists'''
friends.extend(lucky_numbers)

''' adds to the end of the list'''
friends.append('john')

print(friends)

'''values get pushed to he right'''
friends.insert(1, 'toby')
print(friends)

'''removes from the list'''
friends.remove('tim')
print(friends)

'''removes an item from the end of the list'''
friends.pop()

'''tells the location of the item from the list'''
print(friends.index('steve'))

'''tells you how many times the vale appears'''
print(friends.count('bob'))

'''puts it in ascending order'''
print(lucky_numbers.sort())
print(lucky_numbers)

'''prints from the back'''
print(lucky_numbers.reverse())
print(lucky_numbers)

'''copies the string into another string'''
friends2 = friends.copy()
print(friends2)


'''erases the list'''
friends.clear()

