#!/usr/bin/env python

import csv
from lib import MovieLensParser

users = []
movies = []
ratings = []

# read files in data
# read users
reader = csv.reader(open('./data/users.dat', 'rb'))
lines = list(reader)
for line in lines:
    users.append(MovieLensParser.parse_user(line))

reader = csv.reader(open('./data/movies.dat', 'rb'))
lines = list(reader)
for line in lines:
    movies.append(MovieLensParser.parse_movie(line))

reader = csv.reader(open('./data/ratings.dat', 'rb'))
lines = list(reader)
for line in lines:
    ratings.append(MovieLensParser.parse_rating(users, movies))
# read movies
# read ratings

# do collaborative filtering

# make recommendations

# success!
