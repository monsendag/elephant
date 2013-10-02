## Simple kNN algorithm

# Similarity matrix between users 
import SimilarityMetrics
import ProduceRecommendation

_users = None
_items = None


def add_users(users):
    global _users
    _users = users


def add_items(items):
    global _items
    _items = items


# returns a dictionary user_id:similarity_measure
def get_recommendations(user):
    """
    Recommendation algorithm - user-based nearest neighbor recommendation:

    Computes recommendation based on the neighborhood of the active user.
    The similarity between users can the computed with different similarity metrics,
    and the similarity metric is decided in step (1)
    It is also different ways of producing the recommendations, and this is decided
    in step (3)

    """
    global _users
    global _items

    # the similarity matrix
    sim = {}

    # (1) Compute similarities between users
    for u, user_u in _users.iteritems():
        sim[u] = SimilarityMetrics.compute_pearson_correlation_coefficient(user_u, user)
        #sim[u] = SimilarityMetrics.compute_spearman_correlation_coefficient(user_u, user)
        #sim[u] = SimilarityMetrics.compute_cosine_similarity(user_u, user)
        #sim[u] = SimilarityMetrics.compute_mean_squeared_difference(user_u, user)

    # (2) Create the neighborhood of the 10 closest users
    neighbors = get_closest_neighbors(sim, 10)

    # (3) Compute predictions
    predictions = {}
    for item in _items:
        predictions[item] = ProduceRecommendation.prediction_based(sim, _users, user, neighbors, item)
        #predictions[item] = ProduceRecommendation.frequency_based(_users, neighbors, item)
        #predictions[item] = ProduceRecommendation.frequency_based_with_rating_threshold(_users, neighbors, item)
        #predictions[item] = ProduceRecommendation.ratings_based(neighbors, _users, item)
        #predictions[item] = ProduceRecommendation.similarity_based(sim, neighbors, _users, item)

    # (4) Get top N recommendations (N = 10, same size as neighborhood)
    predictions_sorted = sorted(predictions.items(), key=lambda (k, v): v)
    predictions_sorted.reverse()
    top_n_recommendations = predictions_sorted[0:10]

    print 'Movie id     Recommendation      Movie title'
    for recommendation in top_n_recommendations:
        print recommendation[0], '             ', "{0:.2f}".format(recommendation[1]), '      ', _items.get(recommendation[0]).title

    return top_n_recommendations


def get_rating(user, item):
    """ predicts what the user would give the item based on the ratings of its closest neighbors """
    global _users
    global _items

    # the similarity matrix
    sim = {}

    # (1) Compute similarities between users
    for u, user_u in _users.iteritems():
        sim[u] = SimilarityMetrics.compute_pearson_correlation_coefficient(user_u, user)
        #sim[u] = SimilarityMetrics.compute_spearman_correlation_coefficient(user_u, user)
        #sim[u] = SimilarityMetrics.compute_cosine_similarity(user_u, user)
        #sim[u] = SimilarityMetrics.compute_mean_squared_difference(user_u, user)

    # (2) Create the neighborhood of the 10 closest users
    neighbors = get_closest_neighbors(sim, 10)

    # (3) Compute prediction
    return ProduceRecommendation.prediction_based(sim, _users, user, neighbors, item)


def get_closest_neighbors(similarity_vector, num):
    """ finds the ten closest neighbors and return a dictionary user_id:similarity_measure """
    neighbors_dict = similarity_vector.copy()
    closest = {}

    while len(closest) < num:
        highest_rating = -1

        for user_id, similarity_measure in neighbors_dict.iteritems():
            if highest_rating < similarity_measure:
                highest_rating = similarity_measure
                user_match = user_id

        closest[user_match] = highest_rating
        del neighbors_dict[user_match]

    return closest