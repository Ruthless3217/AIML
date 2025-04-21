from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris=datasets.load_iris()
x=iris.data; data =pd.DataFrame(x)

car=data.corr()
sns.heatmap(car,square=True);plt.show()

scaler=StandardScaler()
x_std=scaler.fit_transform(x)

clt=AgglomerativeClustering(linkage="complete",affinity="euclidean",n_clusters=5)
model=clt.fit(x_std)

clusters =pd.DataFrame(model.fit_predict(x_std))
data["Cluster"]=clusters

fig=plt.figure();ax=fig.add_subplot()
scatter=ax.scatter(data[0],data[1],c=data["Cluster"])
ax.set_title("Agglomerative Clustering")
ax.set_xlabel("X0"); ax.set_ylabel("X1")
plt.colorbar(scatter);
plt.show()
