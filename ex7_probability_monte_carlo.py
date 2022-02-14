"""
Write a program that generates 10000 random zeros and ones where the probability of one is p1 and the probability of zero is 1-p1 (hint: np.random.choice([0,1], p=[1-p1, p1], size=10000)), counts the number of occurrences of 5 consecutive ones ("11111") in the sequence, and outputs this number as a return value. 
"""

import numpy as np


def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.empty(10000)
    seq = np.random.choice(
        [0, 1], p=[1 - p1, p1], size=10000
    )  # p = probability attachment for each value 0 == 1-0.6666
    return seq


def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    sequence_matches = 0
    i = 0
    while i < (len(seq) - 4):
        if (
            seq[i] == 1
            and seq[i + 1] == 1
            and seq[i + 2] == 1
            and seq[i + 3] == 1
            and seq[i + 4] == 1
        ):
            sequence_matches += 1
            # i += 5 Thought that it was exactly 5 and then start over, but it's not
            i += 1
            continue
        i += 1

    sequence_matches_for = 0
    number_of_matches = 0
    for i in seq:
        if i == 0:
            number_of_matches = 0
            continue
        if i == 1:
            number_of_matches += 1
            if number_of_matches >= 5:
                sequence_matches_for += 1

    return sequence_matches


def main(p1):
    seq = generate(p1)
    return count(seq)


print(main(2 / 3))  # The proability attachment for getting 1
