import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.read_csv('CO2.csv')
df=df.dropna()

print(df)
x=df[['Volume','Weight']]
y=df['CO2']

regr=LinearRegression()
regr.fit(x, y)


predictedCO2=regr.predict([[2300,1300]])

print(f'Predicted CO2: {predictedCO2}')
