from datetime import datetime
import Models

delimiter = '::'

# UserID::Gender::Age::Occupation::Zip-code
def parse_user(line):
    # split line on delimiter
    data = line.split(delimiter)
    # create user object
    user = Models.User()

    # assign attributes
    user.id = int(data[0])
    user.gender = data[1] == "M"
    user.age = int(data[2])
    user.occupation = data[3]
    user.zipcode = data[4]

    return user


# MovieID::Title::Genres
def parse_movie(line):
    # split line on delimiter
    data = line.split(delimiter)
    # create movie object
    movie = Models.Movie()

    # assign attributes
    movie.id = int(data[0])
    movie.title = data[1]
    # genres are pipe separated, read into array
    movie.genres = data[2].split('|')

    return movie

# UserID::MovieID::Rating::Timestamp
def parse_rating(line, users, movies):
    # split line on delimiter
    data = line.split(delimiter)

    user_id = int(data[0])
    movie_id = int(data[1])


    rating = Models.Rating()

    rating.value = int(data[2])
    rating.time = datetime.fromtimestamp(int(data[3]))
    rating.user = users[user_id]
    rating.movie = movies[movie_id]

    # create pointer on user list
    users[user_id].ratings[movie_id] = rating
    # create pointer on movie list
    movies[movie_id].ratings[user_id] = rating

    return rating





