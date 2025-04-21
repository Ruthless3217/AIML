import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.read_csv('C:/Users/yashr/OneDrive/Desktop/Yash/AIML/Datasets/minihomeprices.csv')
df=df.dropna()
x=df[['area','bedrooms','age']]
y=df['price']

regr=LinearRegression()
regr.fit(x, y)

predicted_price=regr.predict([[2000,3,10]])
print(f'Predicted Price: {predicted_price}')