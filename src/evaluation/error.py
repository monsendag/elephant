from math import sqrt


def MAE(ratings, range):
    """ Mean Absolute Error
    measures average deviation (error) in the predicted rating compared to the true
    rating given by a user """

    def err(pair):
        (r, rP) = pair
        return abs(r-rP)

    return (1/len(ratings)) * sum(map(err, ratings))


def NMAE(ratings, range):
    """ Normalized Mean Absolute Error
    normalizes mean absolute error with the range of available rating values """

    Rmax = max(range)
    Rmin = min(range)

    return MAE(ratings, range) / (Rmax - Rmin)


def MSE(ratings, range):
    """ Mean Squared Error
    punishes higher errors more severely """

    def squared_err(pair):
        (r, rP) = pair
        return (r-rP)**2

    return (1/len(ratings)) * sum(map(squared_err, ratings))


def RMSE(ratings, range):
    """ Root Mean Squared Error
     reflects the variance """

    return sqrt(MSE(ratings, range))
