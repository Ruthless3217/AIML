import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

df=pd.read_csv('groceries.csv')
records=[]

for i in range(0,9834):
    records.append([str(df.values[i,u]) for u in range(0,24)])
    
rules=apriori(records,min_support=0.0022,min_confidence=0.20,min_lift=3,min_length=4)

results=list(rules)

results_list=[]

for i in range(0,len(results)) :
    results_list.append('Rule:\t'+str(results[i][0])+'\nSupport:\t'+str(results[i][1]))
    
print(len(results_list)) 

print(f"Result list:{results_list[0]}")   
