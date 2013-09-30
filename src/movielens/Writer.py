import calendar

delimiter = '::'


# UserID::Gender::Age::Occupation::Zip-code
def write_users(file, users):
    with open (file, 'w') as f:
        for user in users:
            # create data array
            data = 5*[None]
            data[0] = user.id
            data[1] = "M" if user.male else "F"
            data[2] = user.age
            data[3] = user.occupation
            data[4] = user.zipcode

            data = map(str, data)
            # append to file
            f.write ("::".join(data)+'\n')
        f.close()

# MovieID::Title::Genres
def write_movies(file, movies):
    with open (file, 'w') as f:
        for movie in movies:
            # create data array
            data = 3*[None]
            data[0] = movie.id
            data[1] = movie.title
            data[2] = "|".join(movie.genres)

            data = map(str, data)
            # append to file
            f.write ("::".join(data)+'\n')
        f.close();

# UserID::MovieID::Rating::Timestamp
def write_ratings(file, ratings):
    with open (file, 'w') as f:
        for rating in ratings:
            # create data array
            data = 4*[None]
            data[0] = rating.user.id
            data[1] = rating.movie.id
            data[2] = rating.value
            data[3] = calendar.timegm(rating.time.utctimetuple())

            data = map(str, data)
            # append to file
            f.write ("::".join(data)+'\n')
        f.close();

