import numpy as np
import pandas as pd
import os


def get_features(file):
	df = pd.read_csv(file, index_col=0)
	dfm = df.groupby("userId").title.apply(lambda x: set(x))
	df.genres = df.genres.apply(lambda x: str(x).split("|"))
	df = df.explode("genres")
	df_ = pd.pivot_table(df, index="userId", columns="genres", values="movieId", aggfunc="count").fillna(0)
	feature_df = pd.DataFrame(columns = ['(no genres listed)', 'Action', 'Adventure', 'Animation', 'Children',
       'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'IMAX', 'Musical', 'Mystery', 
	   'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'])
	for k in feature_df.columns:
		if k not in df_.columns:
			feature_df[k] = 0
		else:
			feature_df[k] = df_[k]
	feature_df = feature_df.fillna(0)
	feature_df = feature_df.join(dfm)
	feature_df = feature_df.dropna()
	#feature_df.to_csv("/pfs/out/{}.csv".format(os.path.split(file)[-1].split(".")[0]))
	feature_df.to_csv("/pfs/out/old_users.csv")
	#feature_df.to_csv("./output/result_{}.csv".format(os.path.split(file)[-1].split(".")[0]))

# walk /pfs/images and make predictions on every file found
#for dirpath, dirs, files in os.walk("./input"):
for dirpath, dirs, files in os.walk("/pfs/existing_users"):
    for file in files:
    	get_features(os.path.join(dirpath, file))

