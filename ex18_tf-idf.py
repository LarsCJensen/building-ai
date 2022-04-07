"""
Let's combine two tasks: finding the most similar pair of lines and the tf-idf
representation.

Write a program that uses the tf-idf vectors to find the most similar pair of lines in a
given data set. You can test your solution with the example text below. Note, however,
that your solution will be tested on other data sets too, so make sure you don't make
use of any special properties of the example data (like there being four lines of text).

This exercise requires a bit more work than average but you should be able to benefit 
from what you have done in the previous exercises.
"""

import math
from typing import List
import numpy as np

text = """Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again"""


def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal
    # despite casing) can be done with
    # docs = [line.lower().split() for line in text.split('\n')]

    # 2. go over each unique word and calculate its term frequency, and its document frequency

    # 3. after you have your term frequencies and document frequencies, go over each
    # line in the text and calculate its TF-IDF representation, which will be a vector

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    docs = [line.lower().split() for line in text.splitlines()]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.lower().split()))

    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word) / len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs]) / N

    # loop through documents to calculate the tf-idf values¨
    # Create a vector for each document where all words in vocabulary is
    # present (0 if word doesnt exist) so the documents can be compared correctly
    tf_idf_list = []
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            if word in doc:
                test = _get_tf_idf_for_word(tf[word][doc_index], df[word])
            else:
                test = 0
            tfidf.append(test)
        tf_idf_list.append(tfidf)
    tf_idf_vector = np.array(tf_idf_list)
    find_nearest_pair(tf_idf_vector)


def find_nearest_pair(data):
    N = len(data)  # Number of rows
    # creates an empty array
    dist = np.empty((N, N), dtype=np.float)
    for i in range(N):
        for j in range(N):
            dist[i, j] = _get_distance_between_rows(data[i], data[j])

    # To prevent diagonal lines in data set (which is 0 and lowest)
    np.fill_diagonal(dist, np.inf)
    print(np.unravel_index(np.argmin(dist), dist.shape))


def _get_distance_between_rows(row1, row2):
    dist = 0
    for i in range(len(row1)):
        if i > len(row2) - 1:
            dist += 0
        else:
            dist += abs(row1[i] - row2[i])
    return dist


def _get_tf_idf_for_word(tf: float, df: float) -> float:
    return tf * math.log(df, 10)


main(text)
