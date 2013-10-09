from collections import deque

def _chunks(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out


def cross_validate(ratings, recommender):
    """ do a cross validation on recommendation algorithm """
    num_folds = 10

    # divide items into 10 parts
    folds = _chunks(ratings, num_folds)
    queue = deque(folds)

    pairs = []
    for i in range(1, num_folds):
        # for each, take it out, train on the rest (load to memory)
        fold = queue.popleft()

        # predict rating for each item in the fold
        for rating in fold:
            prediction = recommender.get_rating(rating.user, rating.movie)
            pairs.append((rating.value, prediction))

        queue.append(fold)

    # return average error
#    return mean_absolute_error(pairs, range(1, 6))



