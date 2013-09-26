#!/usr/bin/env python

from src import Reader
from src import SimpleKNN as kNN

#
(users, movies, ratings) = Reader.read_data('./data')

# print "##################################"
# print "Loaded MovieLens data"
# print "Users: %d" % (len(users))
# print "Movies: %d" % (len(movies))
# print "Ratings: %d" % (len(ratings))
# print "##################################"

# make recommendations

matrix = kNN.compute_recommendations(users)

# ???????

# Profit!
