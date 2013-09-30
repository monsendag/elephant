#!/usr/bin/env python

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
print SimpleKNN.get_recommendations(user)