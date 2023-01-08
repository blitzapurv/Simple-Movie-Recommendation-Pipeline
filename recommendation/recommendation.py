import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pickle, glob, os, shutil, sys, warnings
warnings.filterwarnings('ignore')


user_input_id = str(os.environ.get('PACH_DATUM_new_users_JOIN_ON'))

user_path  = os.path.join("/pfs/new_users",user_input_id)
user_feature_path = glob.glob(os.path.join("/pfs/new_user_features", "*"))[0]

existing_path = "/pfs/existing_user_features/old_users.csv"
model_path = "/pfs/models/model"

classifier = pickle.load(open(model_path, 'rb'))


si = pd.read_csv(user_path)	#new user raw data
fsi = pd.read_csv(user_feature_path, index_col=0)	#new user features
fsi = fsi.values[0]
user_movies = pd.read_csv(existing_path, index_col=False)["title"]	#set of unique movies watched by current user

li = classifier.kneighbors([fsi],n_neighbors=3,return_distance=False)[0]

current_user_movies = set(si["title"].to_list())
#print("current_user_movies : ", current_user_movies)
similar_user_movies = set()
for i in li:
	similar_user_movies = similar_user_movies.union(eval(user_movies.iloc[i]))
	#print(i, user_movies.iloc[i])
#print("similar_user_movies : ", similar_user_movies)
#print(list(similar_user_movies)[0])
#movies_list = [movie for movie in similar_user_movies if movie not in current_user_movies]
movies_list = similar_user_movies.difference(current_user_movies)
#print("movies_list : ", movies_list)
movies_list = sorted(list(movies_list))


with open("/pfs/out/recommendation_{}.txt".format(user_input_id.split(".")[0]), 'w') as location_file:
	location_file.write("RECOMMENDED MOVIES : \n"+str(len(movies_list))+"\n")
	location_file.write("\n".join(movies_list))
	location_file.close()

