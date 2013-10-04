# Elephant
[![Build Status](https://travis-ci.org/ntnu-smartmedia/elephant.png?branch=master)](https://travis-ci.org/ntnu-smartmedia/elephant)
[![Coverage Status](https://coveralls.io/repos/ntnu-smartmedia/elephant/badge.png)](https://coveralls.io/r/ntnu-smartmedia/elephant)


Implementation of a neighbour-based collaborative filtering algorithm.

Predicts the rating r<sub>ui</sub> of a user u for a new item i using the ratings given to i by users most similar to u, called nearest-neighbors. Suppose we have for each user v ≠ u a value w<sub>uv</sub> representing the preference similarity between u and v.


The kNN of u are the k users v with highest similarity w<sub>uv</sub> to u. However only the users who have rated item i can be used in the prediction, so we only consider the k users most similar to u, that have rated i.

Predict rating as average of ratings by the selected neighbours, weighted by their normalised similarity to u.



### Installation

Clone the Elephant repository:
`git clone git@github.com:ntnu-smartmedia/elephant.git`

Install required packages using pip:
`pip install -r requirements.txt`

### Usage

```
usage: main.py [-h] [-r RECOMMENDER] [-e]

Elephant recommender algorithm library

optional arguments:
  -h, --help            						show this help message and exit
  -r RECOMMENDER, --recommender RECOMMENDER	Input recommender algorithm
  -e, --evaluate        						Evaluate algorithm
```


### Documentation

### Recommender
* **init( \<datastore> datastore )**
* **train()** train the model. For memory based algorithms this does nothing.
* **get_recommendations(\<User> user, \<int> n)** returns n items which *should* be interesting to the user.
* **get_rating(item)** returns the predicted rating of an item.

### Datastore
* **get_users()** returns an iterator over user objects.
* **get_items()** returns an iterator over items.
* **get_ratings()** returns a list of ratings.

### Models

#### User
* **id** (int) the user id
* **male** (bool) True for male, False for female
* **age** (int)
* **ratings** (dict<(int)movie_id, Rating>)
* **get_rating_average()** (float) the average of all ratings given by the user

#### Item
* **id** (int)
* **title** (string)
* **ratings** dict(dict<(int) user_id, Rating>)
* **get_rating_average()** (float) the average of all ratings given to the item

#### Rating
* **value** (int) the rated value
* **user** (User) the user who did the rating
* **item** (Item) the item that was rated


### Code style
We try to follow [Pep 8](http://www.python.org/dev/peps/pep-0008/) as much as possible, and use pylint to help enforce it.

## Release History
See commit history.
