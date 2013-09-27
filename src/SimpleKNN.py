## Simple kNN algorithm

# Similarity matrix between users 
import numpy as np
import math

# calculates the dot product of two users
def calculate_dot_product(user_u_rating, user_v_rating):
	sum = 0
	for movie_u, rating_u in user_u_rating.iteritems():
		for movie_v, rating_v in user_v_rating.iteritems():
			if movie_u == movie_v:
				sum = sum + rating_u.value * rating_v.value
	return sum

# calculates the absolute value of a vector (a user/item)
def calculate_abs_vector(user_rating):
	sum = 0
	for key, rating in user_rating.iteritems():
		sum = sum + rating.value ** 2

	return math.sqrt(sum)

# User.ratings : hashmap movie_id:tuple(movie,rating)
# need only to do computing on movies users both have rated, since the dotproduct of other movies are 0
def compute_similarity_between_users(u,v):
	
	# cosine similarity function
	return 1 - calculate_dot_product(u.ratings, v.ratings)/(calculate_abs_vector(u.ratings)*calculate_abs_vector(v.ratings))

def compute_recommendations(users):
	sim = np.zeros(shape=(len(users),len(users)))

	# Compute similarities between users
	for key_u, user_u in users.iteritems():
		for key_v, user_v in users.iteritems():
			compute_similarity_between_users(user_u, user_v)

	print 'Finished'


	return sim
