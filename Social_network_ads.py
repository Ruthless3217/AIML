import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('C:/Users/yashr/OneDrive/Desktop/Yash/AIML/Datasets/Social_Network_Ads.csv')

x=df.iloc[:,[2,3]].values
y=df.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()

classifier.fit(x_train,y_train)
y_pred=classifier.predict(([[48,75000]]))

print(f'Predicted class: {y_pred[0]}')

