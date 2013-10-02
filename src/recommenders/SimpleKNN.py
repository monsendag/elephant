
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

    # (2) Create the neighborhood of the 10 closest users
    neighbors = get_closest_neighbors(user, 10, SimilarityMetrics.compute_pearson_correlation_coefficient)

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

    # (2) Create the neighborhood of the 10 closest users
    neighbors = get_closest_neighbors(user, 10, SimilarityMetrics.compute_pearson_correlation_coefficient)

    # (3) Compute prediction
    return ProduceRecommendation.prediction_based(sim, _users, user, neighbors, item)


def get_closest_neighbors(user, num, similarity_function):
    """ finds the ten closest neighbors and return a dictionary user:similarity """

    # the similarity vector
    similarity_vector = {}

    # (1) Compute similarities between users
    for other in _users:
        similarity_vector[other] = similarity_function(user, other)

    # get n closest neigbors based on similarity value
    closest_arr = nlargest(num, similarity_vector, key=lambda k: similarity_vector[k])

    # create dictionary with user:similarity pairs
    closest = {}
    for neighbor in closest_arr:
        closest[neighbor] = similarity_vector[neighbor]

    return closest
