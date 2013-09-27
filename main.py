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

# Prints out an user object, debugging purposes only
print users[1].id
print users[1].gender
print users[1].age
print users[1].occupation
print users[1].zipcode
for movie_id, rating in users[1].ratings.iteritems():
	print movie_id, ' ', rating.value

# make recommendations



# matrix = kNN.compute_recommendations(users, users[1])

# ???????

# Profit!
