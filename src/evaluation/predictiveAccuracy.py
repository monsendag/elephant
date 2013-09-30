from math import sqrt

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
