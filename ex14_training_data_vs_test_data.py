"""
Write a program that reads data about one set of cabins (training data), estimates linear regression coefficients based on it, then reads data about another set of cabins (test data), and predicts the prices in it. Note that both data sets contain the actual prices, but the program should ignore the prices in the second set. They are given only for comparison.
"""

import numpy as np
from io import StringIO
import itertools

train_string = """
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
"""

test_string = """
36 3 15 1 850 196000
75 5 18 2 540 290000
"""


def main():
    np.set_printoptions(
        precision=1
    )  # this just changes the output settings for easier reading

    # Please write your code inside this function
    input_file = StringIO(train_string)
    data = np.genfromtxt(input_file)
    x_train = np.delete(data, 5, axis=1)
    y_train = list(
        itertools.chain.from_iterable(np.delete(data, [0, 1, 2, 3, 4], axis=1))
    )
    # read in the training data and separate it to x_train and y_train

    # fit a linear regression model to the data and get the coefficients
    c = c = np.linalg.lstsq(x_train, y_train)[0]

    # read in the test data and separate x_test from it
    input_file = StringIO(test_string)
    test_data = np.genfromtxt(input_file)
    x_test = np.asarray(np.delete(test_data, 5, axis=1))

    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)


main()
