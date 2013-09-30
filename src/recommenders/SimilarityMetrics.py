"""
All similarity metrics between users will be stored in this module. 
The similarity metrics will have two users as parameters and compute the similarity with
these users
"""
# Similarity matrix between users 
import math

def calculate_dot_product(user_u_rating, user_v_rating):
    """ calculates the dot product of two users """

    sum = 0
    for movie_u, rating_u in user_u_rating.iteritems():
        for movie_id_v, rating_v in user_v_rating.iteritems():
            if movie_u == movie_id_v:
                sum += rating_u.value * rating_v.value
    return sum


def calculate_abs_vector(ratings):
    """ calculates the absolute value of a vector (a user/item)"""

    sum = 0
    for movie_id, rating in ratings.iteritems():
        sum += rating.value ** 2
    return math.sqrt(sum)


def compute_cosine_similarity(u, v):
    """
    Cosine similarity:

    Standard metric in item-based recommendations.
    Take values from 0 to 1, where values near to 1 indicate strong similarity.
    Need only to do computing on movies users both have rated, since the dotproduct of other movies are 0
    """
    
    # cosine similarity function
    return calculate_dot_product(u.ratings, v.ratings)/(calculate_abs_vector(u.ratings)*calculate_abs_vector(v.ratings))


def compute_pearson_correlation_coefficient(u, v):
    """
    Pearson's correlation coefficient:

    Take values from +1 (strong positive correlation) to -1 (strong negative correlation).
    """
    avg_rating_u = u.get_rating_average()
    avg_rating_v = v.get_rating_average()

    numerator = 0

    squared_u = 0
    squared_v = 0
    denominator = 0

    for movie_id, rating in u.ratings.iteritems():
        if v.ratings.has_key(movie_id):
            numerator += (rating.value - avg_rating_u) * (v.ratings.get(movie_id).value - avg_rating_v)
            squared_u += (rating.value - avg_rating_u) ** 2
            squared_v += (v.ratings.get(movie_id).value - avg_rating_v) ** 2

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
    denomiator = 0

    for movie_id, rating in u.ratings.iteritems():
        if movie_id in v.ratings:
            numerator += (rating.value - avg_rating_u) * (v.ratings.get(movie_id).value - avg_rating_v)
            squared_u += (rating.value - avg_rating_u) ** 2
            squared_v += (v.ratings.get(movie_id).value - avg_rating_v) ** 2

    denomiator += math.sqrt(squared_u * squared_v)

    if denomiator == 0: 
        return 0 
    else: 
        return numerator / denomiator


def compute_mean_squared_difference(u, v):
    """
    Mean Squared Difference (MSD):

    Does not capture negative correlations between users.
    """
    denominator = 0
    number_of_corated_items = 0

    for movie_id, rating in u.ratings.iteritems():
        if movie_id in v.ratings:
            denominator += (rating.value - v.ratings.get(movie_id).value) ** 2
            number_of_corated_items += 1
    
    if denominator == 0:
        return denominator
    else:
        return number_of_corated_items