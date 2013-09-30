# Frequency-based

def frequency_based(users, neighbors, item):
	"""
	The most frequently occurring items in the neighborhood are recommended.
	Shortcomming: Does not use the ratings to produce the recommendation, e.g. an item
	with rating 1 or 2 will be counted, but this is not optimal since the user did not like this item.
	"""
	weight = 0

	for user in neighbors:
		user_object = users[user]
		if item in user_object.ratings:
			weight += 1

	return weight

def frequency_based_with_rating_threshold(users, neighbors, item):
	"""
	The threshold, which is three in this implementation, guaranties that only popular items among 
	the users in the neighborhood are accounted. 
	"""
	weight = 0

	for user in neighbors:
		user_object = users[user]
		if item in user_object.ratings:
			# add weight if the users liked the item, i.e. gave it a rating of 4 or 5 out of 5
			if user_object.ratings.get(item).value > 3:
				weight += 1

	return weight

# Prediction-based

def prediction_based(similarity_vector, users, user, neighbors, movie):
    """
    Prediction:

    pred(a,p) = avg(rating a) + (for all N closest neighbours b: sim(a,b) * (r(b,p) - avg(rating b))
                                / (for all N closest neighbours b: sim(a,b))

    For this function, N will be 10, i.e. the ten closest neighbours
    """
    numerator = 0
    denominator = 0

    for neighbor in neighbors:
        neighbor_object = users[neighbor]

        # check if user has rated the movie, it not, rating is set to 0
        if movie in neighbor_object.ratings:
            neighbor_movie_rating = neighbor_object.ratings[movie].value
        else:
            neighbor_movie_rating = 0

        numerator += similarity_vector[neighbor_object.id] * (neighbor_movie_rating - neighbor_object.get_rating_average())
        denominator += similarity_vector[neighbor_object.id]

    return user.get_rating_average() + numerator / denominator

# Ratings-based

# Similarity-based
