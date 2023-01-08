# Simple-Movie-Recommendation-Pipeline
Recommender system pipeline based on Collaborative Filtering

The final pipelines, **Recommendations**, take input from four repositories, new_users, new_user_features, models and existing_user_features.

The containerized code in the final pipeline uses a model to find the three users that are most similar to the new user whose data is in the user_path file. The similarity between users is determined using the features that were extracted from the movie rating data for each user.

Next, the model finds the three existing users that are most similar to the new user, based on the features of the movie rating data. It then creates a set of all the movies that have been rated by these similar users and a set of all the movies that have been rated by the new user. The code then finds the difference between these sets to obtain a list of movies that have been rated by the similar users but not by the new user. This list of movies is sorted and written to a file in the /pfs/out directory.
