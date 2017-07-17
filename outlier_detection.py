import pandas as pd
import matplotlib.pyplot as plt
import random
import outlie as ou

file=pd.read_csv("/Users/maitree/countrycode.csv",sep=',',delimiter=None)
data = file[['Country','Countrycode']]
file['outlier']=ou.outlie(data,threshold=1)
print(file['outlier'])


