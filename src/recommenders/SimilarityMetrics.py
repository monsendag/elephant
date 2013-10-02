"""
All similarity metrics between users will be stored in this module. 
The similarity metrics will have two users as parameters and compute the similarity with
these users
"""
# Similarity matrix between users 
import math

def calculate_dot_product(user, other):
    """ calculates the dot product of two users """

    sum = 0
    for item_id_i, rating_i in user.ratings.iteritems():
        for item_id_j, rating_j in other.ratings.iteritems():
            if item_id_i == item_id_j:
                sum += rating_i.value * rating_j.value
    return sum


def calculate_abs_vector(ratings):
    """ calculates the absolute value of a vector (a user/item)"""

    sum = 0
    for movie_id, rating in ratings.iteritems():
        sum += rating.value ** 2
    return math.sqrt(sum)


def compute_cosine_similarity(user, other):
    """
    Cosine similarity:

    Standard metric in item-based recommendations.
    Take values from 0 to 1, where values near to 1 indicate strong similarity.
    Need only to do computing on movies users both have rated, since the dotproduct of other movies are 0
    """
    
    # cosine similarity function
    return calculate_dot_product(user, other)/(calculate_abs_vector(user.ratings)*calculate_abs_vector(other.ratings))


def compute_pearson_correlation_coefficient(user, other):
    """
    Pearson's correlation coefficient:

    Recommended similarity metric for user-based CF.
    Take values from +1 (strong positive correlation) to -1 (strong negative correlation).
    """
    user_average = user.get_rating_average()
    other_average = other.get_rating_average()

    numerator = 0

    squared_u = 0
    squared_v = 0
    denominator = 0

    for id, rating in user.ratings.iteritems():
        # check if other user has rated the item
        if id in other.ratings:
            numerator += (rating.value - user_average) * (other.ratings.get(id).value - other_average)
            squared_u += (rating.value - user_average) ** 2
            squared_v += (other.ratings.get(id).value - other_average) ** 2

    denominator += math.sqrt(squared_u) * math.sqrt(squared_v)

    if denominator == 0:
        return 0 
    else: 
        return numerator / denominator


def compute_spearman_correlation_coefficient(u, v):
    """
    Spearman's correlation coefficient:

    Take values from +1 (strong positive correlation) to -1 (strong negative correlation).
    """
    avg_rating_u = u.get_rating_average()
    avg_rating_v = v.get_rating_average()

    numerator = 0

    squared_u = 0
    squared_v = 0
    denominator = 0

    for id, rating in u.ratings.iteritems():
        if id in v.ratings:
            numerator += (rating.value - avg_rating_u) * (v.ratings.get(id).value - avg_rating_v)
            squared_u += (rating.value - avg_rating_u) ** 2
            squared_v += (v.ratings.get(id).value - avg_rating_v) ** 2

    denominator += math.sqrt(squared_u * squared_v)

    if denominator == 0:
        return 0 
    else: 
        return numerator / denominator


def compute_mean_squared_difference(u, v):
    """
    Mean Squared Difference (MSD):

    Does not capture negative correlations between users.
    """
    denominator = 0
    number_of_corated_items = 0

    for id, rating in u.ratings.iteritems():
        if id in v.ratings:
            denominator += (rating.value - v.ratings.get(id).value) ** 2
            number_of_corated_items += 1
    
    if denominator == 0:
        return denominator
    else:
        return number_of_corated_items