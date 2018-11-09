number = int(input('enter a number you wish to see divisors of: '))
result = 0
divisor_list = []
i = 1
while number <= i:
    result = number % i
    if result == 0:
        divisor_list.append(i)
        print(result)
    i =i + 1

print(divisor_list[:])
