import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pickle
import os


def get_model(file):
	df = pd.read_csv(file, index_col=0)
	df = df.drop("title", axis=1)
	print(df.head())
	X = df.values
	print(df.shape, X.shape)
	classifier = NearestNeighbors(n_neighbors=5)
	classifier.fit(X)

	knnPickle = open('/pfs/out/model', 'wb')
	#knnPickle = open('./output/model', 'wb') 
	# source, destination
	pickle.dump(classifier, knnPickle)  
	# close the file
	knnPickle.close()


# walk /pfs/images and make predictions on every file found
#for dirpath, dirs, files in os.walk("./input"):
for dirpath, dirs, files in os.walk("/pfs/existing_user_features"):
    for file in files:
    	get_model(os.path.join(dirpath, file))

