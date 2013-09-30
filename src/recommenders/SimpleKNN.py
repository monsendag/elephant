## Simple kNN algorithm

# Similarity matrix between users 
import SimilarityMetrics

_users = None
_items = None


def add_users(users):
    global _users
    _users = users


def add_items(items):
    global _items
    _items = items


def create_top_ten_neighborhood(similarity_vector):
    """ finds the ten closest neighbors and return a dictionary user_id:similarity_measure """
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


def make_prediction(similarity_vector, users, user, neighbors, movie):
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


# returns a dictionary user_id:similarity_measure
def get_recommendations(user):
    """
    Recommendation algorithm - user-based nearest neighbor recommendation:

    Computes recommendation based on the neighborhood of the active user.
    The similarity between users can the computed with either cosine similarity or
    Pearson's correlation (recommended for user-based), and the similarity measure is decided
    in step (1)
    """
    global _users
    global _items

    # the similarity matrix
    sim = {}

    # (1) Compute similarities between users
    for u, user_u in _users.iteritems():
        #sim[u] = SimilarityMetrics.compute_pearson_correlation_coefficient(user_u, user)
        #sim[u] = SimilarityMetrics.compute_spearman_correlation_coefficient(user_u, user)
        sim[u] = SimilarityMetrics.compute_cosine_similarity(user_u, user)
        #sim[u] = SimilarityMetrics.compute_mean_squeared_difference(user_u, user)

    # (2) Create the neighborhood of the 10 closest users
    neighbors = create_top_ten_neighborhood(sim)

    # (3) Compute predictions
    predictions = {}
    for item in _items:
        predictions[item] = make_prediction(sim, _users, user, neighbors, item)

    # (4) Get top N recommendations (N = 10, same size as neighborhood)
    predictions_sorted = sorted(predictions.items(), key=lambda (k, v): v)
    predictions_sorted.reverse()
    top_n_recommendations = predictions_sorted[0:10]

    print 'Movie id     Recommendation      Movie title'
    for rec in top_n_recommendations:
        print rec[0], '             ', "{0:.2f}".format(rec[1]), '      ', _items.get(rec[0]).title

    return top_n_recommendations
