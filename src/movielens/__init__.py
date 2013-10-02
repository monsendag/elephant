import Parser

_users = {}
_movies = {}
_ratings = []

def load_users(file):
    """ read and parse users and append to dictionary """
    lines = _read_file(file)
    for line in lines:
        user = Parser.parse_user(line)
        _users[user.id] = user
    return _users

def load_movies(file):
    """ Read and parse movies and append to dictionary """
    lines = _read_file(file)
    for line in lines:
        movie = Parser.parse_movie(line)
        _movies[movie.id] = movie
    return _movies


def load_ratings(file):
    """ Read ratings, and assign two-way pointers from users and movies """
    lines = _read_file(file)
    for line in lines:
        _ratings.append(Parser.parse_rating(line, _users, _movies))
    return _ratings


def _read_file(file):
    """ read file as lines """
    with open(file) as f:
        return f.readlines()