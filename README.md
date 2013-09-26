# Elephant

Implementation of a neighbour-based collaborative filtering algorithm.

Predicts the rating r<sub>ui</sub> of a user u for a new item i using the ratings given to i by users most similar to u, called nearest-neighbors. Suppose we have for each user v ≠ u a value w<sub>uv</sub> representing the preference similarity between u and v.


The kNN of u are the k users v with highest similarity w<sub>uv</sub> to u. However only the users who have rated item i can be used in the prediction, so we only consider the k users most similar to u, that have rated i.

Predict rating as average of ratings by the selected neighbours, weighted by their normalised similarity to u.



### Installation

Clone the Elephant repository:
`git clone git@github.com:ntnu-smartmedia/elephant.git`

Install required packages using pip:
`pip install -r requirements.txt`

### Documentation

See data/README for more information about the data. It's read into the following Python data structure:

#### User
* **id** (int) the user id
* **male** (bool) True for male, False for female
* **age** (int)
* **occupation** (string)
* **zipcode** (int)
* **ratings** hashmap movie_id:tuple(Movie,Rating)

#### Movie
* **id** (int)
* **title** (string)
* **genres** array(string)
* **ratings** hashmap user_id:tuple(User,Rating)

#### Rating
* **value** (int) the rated value
* **user** (User) the user who did the rating
* **movie** (Movie) the movie that was rated
* **time** (datetime) when the rating occured
#### MovieLens.Reader

#### MovieLens.Parser



### Usage

```

```

### Code style
We try to follow [Pep 8](http://www.python.org/dev/peps/pep-0008/) as much as possible, and use pylint to help enforce it.

## Release History
See commit history.
