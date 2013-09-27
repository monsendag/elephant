
class User(object):

    _rating_average = -1

    def __init__(self):
        self.ratings = {}

    """ returns the average of all ratings given by the user
        and stores it for future lookup """
    def get_rating_average(self):
        # check for cached value
        if self._rating_average >= 0:
            return self._rating_average

        # check for 0 ratings
        l = len(self.ratings)
        if l == 0:
             return 0

        # calculate average
        if(self.ratings):
            s = sum([rating.value for rating in self.ratings.values()])
            self._rating_average = s/float(l)
            return self._rating_average

        return 0



class Movie(object):

    def __init__(self):
        self.ratings = {}

class Rating(object):

    def __init__(self):
        return
