#!/usr/bin/env python

from src import Reader

#
(users, movies, ratings) = Reader.read_data('./data')

print "##################################"
print "Loaded MovieLens data"
print "Users: %d" % (len(users))
print "Movies: %d" % (len(movies))
print "Ratings: %d" % (len(ratings))
print "##################################"

# make recommendations

# Profit!
