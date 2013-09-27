#!/usr/bin/env python

from src.data import Reader
from src import path
#

(users, movies, ratings) = Reader.read_data(path.get('data/sample100'))

print "##################################"
print "Loaded MovieLens data"
print "Users: %d" % (len(users))
print "Movies: %d" % (len(movies))
print "Ratings: %d" % (len(ratings))
print "##################################"

# make recommendations

# Profit!
