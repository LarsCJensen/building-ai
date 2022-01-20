import math
import random  # just for generating random mountains

# generate random mountains

w = [0.05, random.random() / 3, random.random() / 3]
h = [
    1.0
    + math.sin(1 + x / 0.6) * w[0]
    + math.sin(-0.3 + x / 9.0) * w[1]
    + math.sin(-0.2 + x / 30.0) * w[2]
    for x in range(100)
]


def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    # Edit the program so that Venla doesn't stop climbing as long as she can go up by
    # moving up to five steps either left or right. If there are multiple choices within
    # five steps that go up, any one of them is good.
    while not summit:
        summit = True  # stop unless there's a way up
        for i in range(1, 5):
            if x + 1 < 99 and h[x + i] > h[x]:
                print("i = " + str(i) + " Going right")
                x = x + i  # right is higher, go there
                summit = False  # and keep going
            elif x - i > 0 and h[x - i] > h[x]:
                print("i = " + str(i) + " Going left")
                x = x - i  # left is higher, go there
                summit = False  # and keep going
    return x


# Facit
def climb_facit(x):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True
        for x_new in range(max(0, x - 5), min(99, x + 5)):
            print(x_new)
            if h[x_new] > h[x]:
                x = x_new  # here is higher, go here
                summit = False  # and keep going
    return x


def main(h):
    # start at a random place
    x0 = random.randint(1, 98)
    x = climb(x0, h)
    # x = climb_facit(x0)

    print("start=" + str(x0), "finish=" + str(x))
    return x0, x


main(h)
