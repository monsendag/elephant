"""
A baseline estimate is the first estimate for a prediction of a user or item. 
It is used to adjust predictions for items that generally have higher or lower rating
than others, or adjust predictions for users that generally rates higher or lower than others.

Formula:
	b_ui = r_avg + b_u + b_i

		b_ui = baseline estimate for an unknown rating r_ui (user u and item i)
		r_avg = average overall rating
		b_u = observed deviations of user u
		b_i = observed deviations of item i

	b_i =	( for all known ratings r_ui, u : (r_ui - r_avg) ) / 
			( y_1 - number of different users that have given a rating )

	b_u = 	( for all known ratings r_ui, i : (r_ui - r_avg - b_i) ) / 
			( y_2 + number of different items that have been rated )

	y_1 and y_2 are regularization parameters and are determined by cross validation. Typical values
	in the Netflix dataset are: y_1 = 25, y_2 = 10

Source: Koren, Y. 2010. Factor in the neighbors: Scalable and accurate collaborative filtering. ACM Trans.
		Knowl. Discov. Data. 4, 1, Article 1 (January 2010), 24 pages.
"""

