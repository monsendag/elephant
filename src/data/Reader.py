import Parser

users = {}
movies = {}
ratings = []

"""
read file as lines """
def read_file(file):
    with open(file) as f:
        return f.readlines()

def read_data(data_dir):
    """
    read and parse users and append to dictionary """
    lines = read_file(data_dir+'/users.dat')
    for line in lines:
        user = Parser.parse_user(line)
        users[user.id] = user

    """
    Read and parse movies and append to dictionary """
    lines = read_file(data_dir+'/movies.dat')
    for line in lines:
        movie = Parser.parse_movie(line)
        movies[movie.id] = movie

    """
    Read ratings, and assign two-way pointers from users and movies """
    lines = read_file(data_dir+'/ratings.dat')
    for line in lines:
        ratings.append(Parser.parse_rating(line, users, movies))


    return (users, movies, ratings)


