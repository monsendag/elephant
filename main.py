#!/usr/bin/env python

import argparse

from src import datastore
from src import util

# movielens specific data
from src import movielens

parser = argparse.ArgumentParser(description='Elephant recommender algorithm library')
parser.add_argument('-r', '--recommender', help='Input recommender algorithm', required=False)
parser.add_argument('-e', '--evaluate', action='store_true', help='Evaluate algorithm', required=False)
args = parser.parse_args()


# load data into datastore
datastore.add_users(movielens.load_users(util.path('data/sample100/users.dat')))
datastore.add_items(movielens.load_movies(util.path('data/sample100/movies.dat')))
datastore.add_ratings(movielens.load_ratings(util.path('data/sample100/ratings.dat')))

from src.recommenders import SimpleKNN

# switch recommender, default to SimpleKNN
recommender = {
    'SimpleKNN': SimpleKNN,
}.get(args.recommender, SimpleKNN)

recommender.add_users(datastore.get_users())
recommender.add_items(datastore.get_items())

# print time spent for estimating all ratings of a user
if args.evaluate:
    ratings = datastore.get_ratings()

    def func():
        for r in ratings:
            SimpleKNN.get_rating(r.user, r.movie)

    print "Predicting rating for all ratings:"
    print "Number of ratings: %d" % len(ratings)
    print "..."

    time = util.timer(func).seconds

    print "Total time spent: %d" % time
    print "Time spent per call: %.2f" % (time / float(len(ratings)))

else:
    # get random user
    user = datastore.get_random_user()
    recommendations = recommender.get_recommendations(user, 10)
    sorted = reversed(sorted(recommendations.items(), key=lambda (k, v): v))

    print 'Movie id     Rating      Movie title'
    for (r, rating) in sorted:
        print r.id, '             ', "{0:.2f}".format(rating), '      ', r.title


