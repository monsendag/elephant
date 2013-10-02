#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Elephant recommender algorithm library')
parser.add_argument('-r', '--recommender', help='Input recommender algorithm', required=False)
parser.add_argument('-e', '--evaluate', help='Evaluate algorithm', required=False)
args = parser.parse_args()

from src import datastore
from src import path

# movielens specific data
from src import movielens

# load data into datastore
datastore.add_users(movielens.load_users(path.get('data/sample100/users.dat')))
datastore.add_items(movielens.load_movies(path.get('data/sample100/movies.dat')))
datastore.add_ratings(movielens.load_ratings(path.get('data/sample100/ratings.dat')))


from src.recommenders import SimpleKNN

SimpleKNN.add_users(datastore.get_users())
SimpleKNN.add_items(datastore.get_items())

# get random user
user = datastore.get_random_user()
recommendations = SimpleKNN.get_recommendations(user, 10)

sorted = reversed(sorted(recommendations.items(), key=lambda (k, v): v))

print 'Movie id     Rating      Movie title'
for (r,rating) in sorted:
    print r.id, '             ', "{0:.2f}".format(rating), '      ', r.title


