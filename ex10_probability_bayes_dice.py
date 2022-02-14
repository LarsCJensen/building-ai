"""Your task: starting from the odds 1:1, use the naive Bayes method to update 
the odds after each outcome to decide which of the dice is more likely. 
Edit the function bayes so that it returns True if the most likely die is the 
loaded one, and False otherwise. Remember to be careful with the indices when 
accessing list elements!"""

import numpy as np

p1 = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]  # normal
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]  # loaded


def roll(loaded):
    if loaded:
        print("rolling a loaded die")
        p = p2
    else:
        print("rolling a normal die")
        p = p1

    # roll the dice 10 times
    # add 1 to get dice rolls from 1 to 6 instead of 0 to 5
    sequence = np.random.choice(6, size=10, p=p) + 1
    for roll in sequence:
        print("rolled %d" % roll)

    return sequence


def bayes(sequence):
    odds = 0.5  # start with odds 1:1
    for roll in sequence:
        ratio = p2[roll - 1] / p1[roll - 1]
        odds = odds * ratio
    if odds > 1:
        return True
    else:
        return False


sequence = roll(True)
if bayes(sequence):
    print("I think loaded")
else:
    print("I think normal")
