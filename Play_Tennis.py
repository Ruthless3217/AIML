import numpy as np
import pandas as pd


df=pd.read_csv('PlayTennis.csv')
print(df)
from sklearn.preprocessing import LabelEncoder,MinMaxScaler,StandardScaler
le=LabelEncoder()
df['Outlook']=le.fit_transform(df['Outlook'])
df['Temperature']=le.fit_transform(df['Temperature'])
df['Humidity']=le.fit_transform(df['Humidity'])
df['Wind']=le.fit_transform(df['Wind'])
df['Play Tennis']=le.fit_transform(df['Play Tennis'])

x=df.iloc[:,:-1]
y=df.iloc[:,4]

scaler=MinMaxScaler()
x_scaled=scaler.fit_transform(x)
print(x_scaled)

scaler_standard=StandardScaler()
x_standard_scale=scaler_standard.fit_transform(x)
print(x_standard_scale)
