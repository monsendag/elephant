
import src
from src.evaluation import predictiveAccuracy

from src.recommenders import SimpleKNN

import datetime

def time_get_rating():
    ratings = src.datastore.get_ratings()

    def func():
        for r in ratings:
            SimpleKNN.get_rating(r.user, r.movie)

    print timer(func).seconds


def timer(func):

    start = datetime.datetime.now()
    func()
    end = datetime.datetime.now()
    return (end-start)