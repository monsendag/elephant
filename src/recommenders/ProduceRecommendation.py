
def frequency_based(user, item, neighbors):
    """
    The most frequently occurring items in the neighborhood are recommended.
    Shortcoming: Does not use the ratings to produce the recommendation, e.g. an item
    with rating 1 or 2 will be counted, but this is not optimal since the user did not like this item.
    """
    weight = 0

    for neighbor in neighbors:
        if item in neighbor.ratings:
            weight += 1

    return weight


def frequency_based_with_rating_threshold(user, item, neighbors):
    """
    The threshold, which is three in this implementation, guaranties that only popular items among
    the users in the neighborhood are accounted.
    """
    weight = 0

    for neighbor in neighbors:
        if item in neighbor.ratings:
            # add weight if the users liked the item, i.e. gave it a rating of 4 or 5 out of 5
            if neighbor.ratings.get(item).value > 3:
                weight += 1
    return weight


def prediction_based(user, item, neighbors):
    """
    Prediction:

    pred(a,p) = avg(rating a) + (for all N closest neighbours b: sim(a,b) * (r(b,p) - avg(rating b))
                                / (for all N closest neighbours b: sim(a,b))

    For this function, N will be 10, i.e. the ten closest neighbours
    """
    numerator = 0
    denominator = 0

    for neighbor in neighbors:

        # check if user has rated the movie, it not, rating is set to 0
        if item.id in neighbor.ratings:
            rating = neighbor.ratings[item.id].value
        else:
            rating = 0

        similarity = neighbors[neighbor]
        numerator += similarity * (rating - neighbor.get_rating_average())
        denominator += similarity

    return 0 if denominator == 0 else user.get_rating_average() + numerator / denominator


def ratings_based(user, item, neighbors):
    """
    Sum the ratings of an item in a neighborhood.
    The weight then becomes: for all N closest neighbors: rating(i)
    """
    sum = 0

    for neighbor in neighbors:

        if item in neighbor.ratings:
            sum += neighbor.ratings[item].value

    return sum


def similarity_based(user, item, neighbors):
    """
    An items weight is the sum of all similarities between the active user and the users in the
    neighborhood that has the item in their ratings list
    """
    sum = 0

    for neighbor in neighbors:
        if item in neighbor.ratings:
            sum += neighbors[neighbor]

    return sum
