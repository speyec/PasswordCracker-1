# Password cracker

import time

password = input("Enter a password (only lowercase letters):  ")
start = time.time()
chars = 'abcdefghijklmnopqrstuvwxyz'
guess = []
for value in range(10):
    a = [i for i in chars]
    # a = []
    # for i in chars:
    #     a.append(i)
    for y in range(value):
        a = [x+i for i in chars for x in a]
        # a_new = []
        # for i in chars:
        #     for x in a:
        #         a_new.append(x + i)
        # a = a_new
       
    guess = guess + a
    if password in guess:
        break

end = time.time()
clock = str(end - start)

print("Your password is: " + password)
print("Time taken: " + clock)
