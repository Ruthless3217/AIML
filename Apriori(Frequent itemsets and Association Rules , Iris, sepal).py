import pandas as pd
from apyori import apriori

df=pd.read_csv('C:/Users/yashr/OneDrive/Desktop/Yash/AIML/Datasets/iris.csv')

df['sepal.length']=pd.cut(df['sepal.length'],bins=2,labels=["Short","long"])
df['sepal.width']=pd.cut(df['sepal.width'],bins=2,labels=["Narrow","wide"])

transactions=df[['sepal.length','sepal.width','variety']].astype(str).values.tolist()

frequent_itemsets=apriori(transactions,min_support=0.3)

rules=list(frequent_itemsets)

print("Frequent itemsets and Association Rules:")
for rule in rules:
    print(rule)