from math import sqrt
from collections import deque

def _chunks(l, n):
    """ Yield successive n-sized chunks from l. """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def cross_validate(user, items, recommender):
    """ do a cross validation on recommendation algorithm """
    folds = 10

    # divide items into 10 parts
    folds = _chunks(items, len(items)/folds)
    queue = deque(folds)

    for i in range(1,folds):
        # for each, take it out, train on the rest (load to memory)
        fold = queue.popleft()

        sum_err = 0
        # predict rating for each item in the fold
        for item_id, item in fold:
            rating = recommender.get_rating(user, item)
            sum_err += root_mean_squared_error()

        # avg
        avg = sum_err / len(fold)

        queue.append(fold)

    # return average error



    return avg

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
