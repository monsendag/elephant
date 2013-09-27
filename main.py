#!/usr/bin/env python

from src.data import Reader
from src import path
from src import SimpleKNN as kNN
#

(users, movies, ratings) = Reader.read_data(path.get('data/sample100'))

# print "##################################"
# print "Loaded MovieLens data"
# print "Users: %d" % (len(users))
# print "Movies: %d" % (len(movies))
# print "Ratings: %d" % (len(ratings))
# print "##################################"

# Prints out an user object, debugging purposes only
user = users.itervalues().next()

print user.id
print user.male
print user.age
print user.occupation
print user.zipcode
print "########"
for movie_id, rating in user.ratings.iteritems():
	print movie_id, ' ', rating.value

# make recommendations



# matrix = kNN.compute_recommendations(users, users[1])

# ???????

# Profit!
