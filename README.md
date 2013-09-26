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

* **elephant.load()** Load data into recommendation engine.
* **elephant.getRecommendation(user_id)** Retrieve recommendations for a user id. 
 
### Usage

```

```

## Release History
See commit history.
