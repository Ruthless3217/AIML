import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing dataset
dataset = pd.read_csv('Mall_Customers.csv')
x=dataset.iloc[:,[3,4]].values

import scipy.cluster.hierarchy as sch
dendrogram=sch.dendrogram(sch.linkage(x,method='single'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()

from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=5,affinity='euclidean',linkage='single')
y_hc=hc.fit_predict(x)

plt.scatter(x[y_hc==0,0],x[y_hc==0,1],s=100,c='red',label='Cluster1')
plt.scatter(x[y_hc==1,0],x[y_hc==1,1],s=100,c='blue',label='Cluster2')
plt.scatter(x[y_hc==2,0],x[y_hc==2,1],s=100,c='green',label='Cluster3')
plt.scatter(x[y_hc==3,0],x[y_hc==3,1],s=100,c='cyan',label='Cluster4')
plt.scatter(x[y_hc==4,0],x[y_hc==4,1],s=100,c='magenta',label='Cluster5')
plt.title('Clusters of Customers')
plt.xlabel('Annual Income (Rs)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
