import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('C:/Users/yashr/OneDrive/Desktop/Yash/AIML/Datasets/credit card.csv')
x=dataset.iloc[:,1:].values

from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy='most_frequent')
imputer=imputer.fit(x)
x=imputer.transform(x)

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x=sc_x.fit_transform(x)

from sklearn.cluster import KMeans

kmeans=KMeans(n_clusters=8,init='k-means++',max_iter=200,n_init=10,random_state=0)
y_kmeans=kmeans.fit_predict(x)

dataset['Cluster']=y_kmeans
print(dataset.head())
