import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


df=pd.read_csv('C:/Users/yashr/OneDrive/Desktop/Yash/AIML/Datasets/Automobile_data.csv')
df.replace('?', np.nan, inplace=True)
df=df.dropna()
x=df[['engine-size','horsepower','curb-weight']]
y=df['price']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

poly=PolynomialFeatures(degree=2)
x_poly=poly.fit_transform(x_train)

model=LinearRegression()
model.fit(x_poly, y_train)

x_test_poly=poly.transform(x_test)
predictions=model.predict(x_test_poly)

new_data=[[2000,150,3000]]
new_data_poly=poly.transform(new_data)
predicted_price=model.predict(new_data_poly)

print(f'Predicted Price:{predicted_price}')