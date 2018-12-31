

# create function with this in recommender.py
#movie_content = np.array(movies.iloc[:,4:])
#movie_content_transpose = np.transpose(movie_content)
#dot_prod = movie_content.dot(movie_content_transpose)

# arguments for make_recommendations() to feed find_similar_items():
# df_items(movies), item_id_colname, dot_prod, item_name_colname

# arguments for make_recommendations() to feed get_item_names():
# df_items(movies), item_id_colname, item_name_colname

# arguments for make_recommendations() to feed ranked_df():
# df_reviews, item_id_colname, rating_col_name, date_col_name

# arguments for make_recommendations() to feed popular_recommendations():
# ranked_items(will be the name of the variable that store the ranked_df() in make rec,
# item_id_colname

import numpy as np
import pandas as pd
import recommender_functions as rf

class Recommender():

	def __init__(self, df_items, df_reviews):
		self.df_items = df_items
		self.df_reviews = df_reviews


	