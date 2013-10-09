# Elephant [![Build Status](https://travis-ci.org/ntnu-smartmedia/elephant.png?branch=master)](https://travis-ci.org/ntnu-smartmedia/elephant) [![Coverage Status](https://coveralls.io/repos/ntnu-smartmedia/elephant/badge.png)](https://coveralls.io/r/ntnu-smartmedia/elephant)

A framework and library of Collaborative Recommendation algorithms.

The algorithms are written to support different kinds of datastructures. We have three kinds of model interfaces which needs to be implemented. These interfaces can be found in the documentation below. The Recommenders all implement the Recommender interface, and can be used both by in and with a Command Line Interface.  

## Installation

1. Clone the Elephant repository:
`git clone git@github.com:ntnu-smartmedia/elephant.git`

2. Install the required packages using pip:
`pip install -r requirements.txt`

## Usage

```
usage: main.py [-h] [-r RECOMMENDER] [-e]

Elephant recommender algorithm library

optional arguments:
  -h, --help            						show this help message and exit
  -r RECOMMENDER, --recommender RECOMMENDER	Input recommender algorithm
  -e, --evaluate        						Evaluate algorithm
```


## Documentation

### Recommender
* **init( \<datastore> datastore )** Initialise the recommender. Train models etcetera.
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


## Code style
We try to follow [Pep 8](http://www.python.org/dev/peps/pep-0008/) as much as possible, and use pylint to help enforce it.

## Release History
See commit history.
