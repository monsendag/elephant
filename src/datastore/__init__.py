
import random

_users = {}
_items = {}
_ratings = []


def add_users(users):
    """ adds a map of users to the datastore """
    global _users
    _users = dict(_users.items() + users.items())


def add_items(items):
    """ adds a map of items to the datastore """
    global _items
    _items = dict(_items.items() + items.items())


def add_ratings(ratings):
    """ adds a map of ratings to the datastore """
    global _ratings
    _ratings = _ratings + ratings


def get_users():
    return _users.itervalues()


def get_random_user():
    return _users[random.choice(list(_users.keys()))]


def get_items():
    return _items.itervalues()


def get_random_item():
    return _items[random.choice(list(_items.keys()))]


def get_item(key):
    return _items[key]


def get_ratings():
    return _ratings


def get_item_ratings(item):
    ratings = []
    for rating in _ratings:
        if item.id == rating.item.id:
            ratings.append(rating)

    return ratings