"""
The program below uses the k-nearest neighbors algorithm. The idea is to not only look 
at the single nearest training data point (neighbor) but for example the five nearest 
points, if k=5. The normal nearest neighbor classifier amounts to using k=1.
Write a program that does the classification for some value of k and prints out the 
training and testing accuracy.

Hint: You can get the model accuracy for a given set using the function knn.score.
Try different values of k to answer the questions below.
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import numpy as np

# do not edit this
# create fake data
x, y = make_moons(
    n_samples=500, random_state=42, noise=0.3  # the number of observations
)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=42
)


training_k = [1, 10, 42, 100, 250]
for k in training_k:
    knn = KNeighborsClassifier(n_neighbors=k)

    knn.fit(x_train, y_train)

    train_acc = knn.score(x_train, y_train)
    print(f"training accuracy for k={k}: {train_acc}")

    test_acc = knn.score(x_test, y_test)
    print(f"testing accuracy for k={k}: {test_acc}")

# Questions to answer:
# What would be a reasonable baseline accuracy your model should outperform in order for it to be considered useful?
# 0,5
# Which of the following values of k do you think was "best"?
# 42
# Why?
# It gave the highest test result
# Is it possible to have a higher test set accuracy than training set accuracy?
# Yes
