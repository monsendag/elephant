from math import sqrt
from collections import deque


def _chunks(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out


def cross_validate(ratings, recommender):
    """ do a cross validation on recommendation algorithm """
    num_folds = 10

    # divide items into 10 parts
    folds = _chunks(ratings, num_folds)
    queue = deque(folds)

    pairs = []
    for i in range(1, num_folds):
        # for each, take it out, train on the rest (load to memory)
        fold = queue.popleft()

        # predict rating for each item in the fold
        for rating in fold:
            prediction = recommender.get_rating(rating.user, rating.movie)
            pairs.append((rating.value, prediction))

        queue.append(fold)

    # return average error
    return mean_absolute_error(pairs, range(1, 6))


def mean_absolute_error(ratings, range):
    """ measures average deviation (error) in the predicted rating compared to the true
        rating given by a user """

    def err(pair):
        (r, rP) = pair
        return abs(r-rP)

    return (1/len(ratings)) * sum(map(err, ratings))


def normalized_mean_absolute_error(ratings, range):
    """ normalizes mean absolute error with the range of available rating values """

    Rmax = max(range)
    Rmin = min(range)

    return mean_absolute_error(ratings, range) / (Rmax - Rmin)


def mean_squared_error(ratings, range):
    """ punishes higher errors more severely """

    def squared_err(pair):
        (r, rP) = pair
        return (r-rP)**2

    return (1/len(ratings)) * sum(map(squared_err, ratings))


def root_mean_squared_error(ratings, range):
    """ RMSE reflects the variance """

    return sqrt(mean_squared_error(ratings, range))
