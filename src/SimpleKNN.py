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
def calculate_abs_vector(ratings):
	sum = 0
	for movie_id, rating in ratings.iteritems():
		sum = sum + rating.value ** 2

	return math.sqrt(sum)

# User.ratings : hashmap movie_id:Rating
# need only to do computing on movies users both have rated, since the dotproduct of other movies are 0
def compute_cosine_similarity_between_users(u,v):
	
	# cosine similarity function
	return 1 - calculate_dot_product(u.ratings, v.ratings)/(calculate_abs_vector(u.ratings)*calculate_abs_vector(v.ratings))

# Calculates the Pearson's correlation coefficient. It takes values from +1 to -1, 
# strong positive correlation to strong negative correlation.
def compute_pearson_correlation_coefficient(u, v):
    avg_rating_u = u.get_rating_average()
    avg_rating_v = v.get_rating_average()

    numerator = 0

    squared_u = 0
    squared_v = 0
    denomiator = 0

    for movie_id, rating in u.ratings.iteritems():
        if v.ratings.has_key(movie_id):
            numerator += (rating.value - avg_rating_u) * (v.ratings.get(movie_id).value - avg_rating_v)
            squared_u += (rating.value - avg_rating_u) ** 2
            squared_v += (v.ratings.get(movie_id).value - avg_rating_v) ** 2

    denomiator = math.sqrt(squared_u) * math.sqrt(squared_v)
    
    return numerator / denomiator

"""
Prediction:

pred(a,p) = avg(rating a) + (for all N closest neighbours b: sim(a,b) * (r(b,p) - avg(rating b)) 
							/ (for all N closest neighbours b: sim(a,b))

For this function, N will be 10, i.e. the ten closest neighbours
"""
def make_prediction(similarity_vector, users, user, neighbors, movie):
	print 'similarity_vector is : ', similarity_vector
	print 'movie : ',movie

	# calculate the average rating of user
	numerator = 0
	denomiator = 0
	for neighbor in neighbors:
		neighbor_object = users[neighbor]
		print 'noi : ',neighbor_object.id in similarity_vector
		
		# check if user has rated the movie, it not, rating is set to 0
		if( neighbor_object.ratings.has_key(movie) ):
			neighbor_movie_rating = neighbor_object.ratings[movie].value
		else:
			neighbor_movie_rating = 0
		
		numerator += similarity_vector[neighbor_object.id] * (neighbor_movie_rating - neighbor_object.get_rating_average())
		denomiator +=  similarity_vector[neighbor_object.id]

		print 'Average rating for active user : ', user.get_rating_average()
		print 'Numerator is : ', numerator
		print 'Denomiator is : ', denomiator

	return user.get_rating_average() + numerator / denomiator

def create_top_ten_neighborhood(similarity_vector, user_id):

	neighbors_dict = similarity_vector.copy()	
	top_ten_neighbors = {}

	while len(top_ten_neighbors) < 10:
		highest_rating = -1

		for user_id, similarity_measure in neighbors_dict.iteritems():
			if highest_rating < similarity_measure:
				highest_rating = similarity_measure
				user_match = user_id

		top_ten_neighbors[user_match] = highest_rating
		del neighbors_dict[user_match]

	return top_ten_neighbors

# returns a dictionary user_id:similarity_measure
def compute_recommendations(users, user, movies):

	print 'Active user id : ',user.id

	# the similarity matrix
	sim = {}

	# Compute similarities between users
	for u, user_u in users.iteritems():
			sim[u] = compute_cosine_similarity_between_users(user_u, user)

	print 'Similarity vector : ',sim
	print 'length : ', len(sim)
			
	# Create the neighborhood of the 10 closest users
	neighbors = create_top_ten_neighborhood(sim, user.id)

	print 'Top ten neighbors : ',neighbors
	print 'Similarity vector : ',sim
	print 'length : ', len(sim)

	# Compute predictions
	predictions = {}
	for movie in movies:
		predictions[movie] = make_prediction(sim, users, user, neighbors, movie)

	# get top N recommendations (N = 10, same size as neighborhood)
	predictions_sorted = sorted(predictions.items(), key = lambda (k,v): v)
	predictions_sorted.reverse()
	top_n_recommendations = predictions_sorted[0:10]

	return top_n_recommendations
