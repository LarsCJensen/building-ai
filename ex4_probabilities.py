"""Write a program that prints "I love" followed by one word: the additional word should be 'dogs' with 80% probability, 'cats' with 10% probability, and 'bats' with 10% probability."""

import random


def main():
    # For is for test
    for i in range(10):
        favourite = "dogs"  # change this
        rnd = random.random()
        if rnd <= 0.1:
            favourite = "cats"
        elif rnd > 0.1 and rnd <= 0.2:
            favourite = "bats"
        print(rnd)
        print("I love " + favourite)
    # Facit
    # import random

    # x = random.random()
    # if x < 0.8:
    #     favourite = "dogs"
    # elif x < 0.9:
    #     favourite = "cats"
    # else:
    #     favourite = "bats"

    # print("I love " + favourite)


main()
