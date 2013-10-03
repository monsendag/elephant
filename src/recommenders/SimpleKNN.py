
import SimilarityMetrics
import ProduceRecommendation
from heapq import nlargest

_users = None
_items = None


def add_users(users):
    global _users
    _users = users


def add_items(items):
    global _items
    _items = items


# returns a dictionary user:similarity
def get_recommendations(user, num):
    """
    Recommendation algorithm - user-based nearest neighbor recommendation:

    Computes recommendation based on the neighborhood of the active user.
    Works in three steps: 
        1. Compute similarities for all users with respect to the active user
        2. Select a subset to use as a set of predictions (neighborhood)
        3. Compute predictions based on the neighborhood

    Step 1 and 2 is done together in # (1), while step 3 is done in # (2). 
    The third parameter in get_closest_neighbors in # (1) decides how to compute the similarities

    """
    global _users
    global _items

    # (1) Create the neighborhood of the 10 closest users
    neighbors = get_closest_neighbors(user, 10, SimilarityMetrics.compute_pearson_correlation_coefficient)

    # (2) Compute predictions
    predictions = {}
    for item in _items:
        predictions[item] = ProduceRecommendation.prediction_based(user, item, neighbors)

    # (3) get n highest rated items based on predicted rating (top-n recommendation)
    highest_rated_arr = nlargest(num, predictions, key=lambda k: predictions[k])

    # (4) create dictionary with item:rating pairs
    highest_rated = {}
    for item in highest_rated_arr:
        highest_rated[item] = predictions[item]

    return highest_rated


def get_rating(user, item):
    """ predicts what the user would give the item based on the ratings of its closest neighbors """
    global _users
    global _items

    # (2) Create the neighborhood of the 10 closest users
    neighbors = get_closest_neighbors(user, 10, SimilarityMetrics.compute_pearson_correlation_coefficient)

    # (3) Compute prediction
    return ProduceRecommendation.prediction_based(user, item, neighbors)


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
