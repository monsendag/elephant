## Simple kNN algorithm

# Similarity matrix between users 
import numpy as np
import math

# calculates the dot product of two users
def calculate_dot_product(user_u_rating, user_v_rating):
	sum = 0
	for movie_u, rating_u in user_u_rating.iteritems():
		for movie_id_v, rating_v in user_v_rating.iteritems():
			if movie_u == movie_id_v:
				sum = sum + rating_u.value * rating_v.value
	return sum

# calculates the absolute value of a vector (a user/item)
def calculate_abs_vector(user_rating):
	sum = 0
	for movie_id, rating in user_rating.iteritems():
		sum = sum + rating.value ** 2

	return math.sqrt(sum)

# User.ratings : hashmap movie_id:tuple(movie,rating)
# need only to do computing on movies users both have rated, since the dotproduct of other movies are 0
def compute_similarity_between_users(u,v):
	
	# cosine similarity function
	return 1 - calculate_dot_product(u.ratings, v.ratings)/(calculate_abs_vector(u.ratings)*calculate_abs_vector(v.ratings))

"""
Prediction:

pred(a,p) = avg(rating a) + (for all N closest neighbours b: sim(a,b) * (r(b,p) - avg(rating b)) 
							/ (for all N closest neighbours b: sim(a,b))

For this function, N will be 10, i.e. the ten closest neighbours
"""
def predict_new_movies(similarity_matrix, users, user):

	# calculate the average rating of user
	return -1

def compute_recommendations(users, user):
	# the similarity matrix
	sim = np.zeros(shape=(len(users),len(users)))

	# Compute similarities between users
	for user_u in users:
		for user_v in users:
			sim[user_u.id][user_v.id] = compute_similarity_between_users(user_u, user_v)

	# Create the neighborhood of the 10 closest users
	neighbors_list = sim[user.id,:]
	neighbors_dict = dict((i,neighbors_list[i]) for i in range(1,len(neighbors_list)))
	top_ten_neighbors = {}

	while len(top_ten_neighbors) < 10:
		highest_rating = -1

		for user_id, similarity_measure in neighbors_dict.iteritems():
			if highest_rating < similarity_measure:
				highest_rating = similarity_measure
				user_match = user_id

		top_ten_neighbors[user_match] = highest_rating
		



	# Compute predictions

	print 'Finished'


	return sim
