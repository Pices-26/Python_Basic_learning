# generate a password with length "passlen" with no duplicate characters in the password

import random
import string

s = ("abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?")
passlen = int(input('enter the lenght of passoword you want: '))
p ="".join(random.sample(s,passlen))
print(p)