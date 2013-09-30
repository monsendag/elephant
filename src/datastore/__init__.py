
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
    return _users


def get_random_user():
    return _users[random.choice(list(_users.keys()))]


def get_items():
    return _items


def get_ratings():
    return _ratings
