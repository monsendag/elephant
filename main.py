#!/usr/bin/env python

users = []
movies = []
ratings = []

# read files in data
# read users
file = open('./data/users.dat', 'r')
for line in file:
    users.add(MovieLensParser.parseUser())

file = open('./data/movies.dat', 'r')
for line in file:
    movies.add(MovieLensParser.parseMovie())

for line in file:
    ratings.add(MovieLensParser.parseRating(users, movies))
# read movies
# read ratings


# do collaborative filtering

# make recommendations

# success!
