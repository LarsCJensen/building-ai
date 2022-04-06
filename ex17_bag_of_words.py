"""our task is to write a program that calculates the distances (or differences) between
every pair of lines in the This Little Piggy rhyme and finds the most similar pair. Use 
the Manhattan distance (also called Taxicab distance) as your distance metric.

You can start by building a numpy array to store all the distances. Notice that the 
diagonal elements in the array (elements at positions [i, j] with i=j) will be equal to 
zero. This happens because the program will compare every row also with itself. To avoid 
selecting those elements, you can assign the value np.inf (the maximum possible floating 
point value). To do this, it's necessary to make sure the type of the array is float.

A quick way to get the index of the element with the lowest value in a 2D array (or in 
fact, any dimension) is by the function:
np.unravel_index(np.argmin(dist), dist.shape))
where dist is the 2D array. This will return the index as a list of length two. 
If you're curious, here's an intuitive explanation (
    https://stackoverflow.com/questions/48135736/what-is-an-intuitive-explanation-of-np-unravel-index
) 
of the function, and here's 
its documentation."""

import numpy as np

data = [
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
]


def find_nearest_pair(data):
    N = len(data)  # Number of rows
    # creates an empty array
    dist = np.empty((N, N), dtype=np.float)
    for i in range(N):
        for j in range(N):
            # Add values to the dist array 0,0 is the distance between 0,0
            dist[i, j] = _get_distance_between_rows(data[i], data[j])

    # To prevent diagonal lines in data set (which is 0 and lowest)
    np.fill_diagonal(dist, np.inf)
    print(np.unravel_index(np.argmin(dist), dist.shape))


def _get_distance_between_rows(row1, row2):
    dist = 0
    for i in range(len(row1)):
        dist += abs(row1[i] - row2[i])
    return dist


find_nearest_pair(data)
