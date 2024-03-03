import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #visualize random distribution using  matplotlib underneath to plot garaphs 
import csv # it is required if the code is compiled on VS code 
from tqdm import tqdm #for output  progress bar 
sns.set()


data = pd.read_csv("D:\\DS PROJECT\\spotify1.csv") #pandas library is used for reading the csv file using the file location 
data = data.dropna()#this is drops the empty columns

############################################################################################################################################################################################################
#data transformation 
from sklearn.preprocessing import MinMaxScaler #MinMaxScaler method provided by the Scikit-learn library in Python,helps in removing the non float and int data types in the columuns
datatypes = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
normarization = data.select_dtypes(include=datatypes)
for col in normarization.columns:
    MinMaxScaler(col)
    
    
#The main objective of the K-Means algorithm is to minimize the sum of distances between the points and their respective cluster centroid.
from sklearn.cluster import KMeans # K means clustering algorithm helps in differentiating the songs from different categories by using normarization 
kmeans = KMeans(n_clusters=10)
features = kmeans.fit_predict(normarization)#with new k values, a new columun(features)is made which helps in recommandation 
data['features'] = features 
MinMaxScaler(data['features'])
############################################################################################################################################################################################################

#function for recommendations
class music_Recommend():
    def __init__(self, dataset):
        self.dataset = dataset
    def recommend(self, songs, amount=1):
        distance = []
        song = self.dataset[(self.dataset.name.str.lower() == songs.lower())].head(1).values[0]
        rec = self.dataset[self.dataset.name.str.lower() != songs.lower()]
        for songs in tqdm(rec.values):
            d = 0
            for col in np.arange(len(rec.columns)):
                if not col in [1, 6, 12, 14, 18]:#artist,song_id,name,relese_date,year ,all these columuns are not taken  because they don't belong to datatypes (int,float) 
                    d = d + np.absolute(float(song[col]) - float(songs[col]))
            distance.append(d)
        rec['distance'] = distance
        rec = rec.sort_values('distance')# songs close to the centroid are the songs which are recommended in this system, the k values(centroid) is 10 
        columns = ['artists', 'name']
        return rec[columns][:amount]

recommendations = music_Recommend(data)#function call 
print("The Song Recommend for 'A Little More' are:\n",recommendations.recommend("A Little More", 10))#songs recommended are in the format of number of songs in the list , the artist and name of the song    

############################################################################################################################################################################################################