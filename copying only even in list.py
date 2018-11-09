a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
c = 0
for i in range(len(a)):
    ans = a[i] % 2
    if ans != 0:
        b.append(i)

print(b)


