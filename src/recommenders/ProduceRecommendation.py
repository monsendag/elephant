# Frequency-based

def frequency_based(users, neighbors, item):
	weight = 0

	for user in neighbors:
		user_object = users[user]
		if item in user_object.ratings:
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
