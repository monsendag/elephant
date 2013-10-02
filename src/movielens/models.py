
class User(object):

    def __init__(self):
        self._rating_average = -1
        self.ratings = {}

    """ returns the average of all ratings given by the user """
    def get_rating_average(self):
        return _get_rating_average(self)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id


class Movie(object):
    def __init__(self):
        self.ratings = {}

    """ returns the average of all ratings given of the movie """
    def get_rating_average(self):
        return _get_rating_average(self)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id


class Rating(object):
    def __init__(self):
        return


# dict for storing average ratings
_avg = {}


def _get_rating_average(obj):
    """ calculates an average of object ratings """
        # check for cached value
    if obj in _avg >= 0:
        return _avg[obj]

    # check for 0 ratings
    l = len(obj.ratings)
    if l == 0:
        return 0

    # calculate average
    if obj.ratings:
        s = sum([rating.value for rating in obj.ratings.values()])
        _avg[obj] = s/float(l)
        return _avg[obj]
    return 0