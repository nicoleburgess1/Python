#Nicole Burgess
#dice roll

import random

guess= int(input("what will the dice land on?\n"))



if guess <= 6 or guess>= 1:
    number= random.randint(1,6)
    if guess== number:
        print("yes")
    else:
        print("no it was " + str(number))
else: print("bad guess")
