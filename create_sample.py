#!/usr/bin/env python

from src.data import Reader, Writer
import src.util
from os.path import join
import random

#
(users, movies, ratings) = Reader.read_data(src.util.path('data/movielens-1m'))

print "##################################"
print "Loaded MovieLens data"
print "Users: %d" % (len(users))
print "Movies: %d" % (len(movies))
print "Ratings: %d" % (len(ratings))
print "##################################"

# get random sample of 100 users
users_sample = random.sample(users.values(), 100)

ratings_sample = []

for user in users_sample:
    ratings_sample += user.ratings.values()

movies_sample = {}

for rating in ratings_sample:
    movies_sample[rating.movie.id] = rating.movie


path_sample = src.util.path('data/sample100')

Writer.write_users(join(path_sample, 'users.dat'), users_sample)
Writer.write_movies(join(path_sample,'movies.dat'), movies_sample.values())
Writer.write_ratings(join(path_sample,'ratings.dat'), ratings_sample)

# Profit!
