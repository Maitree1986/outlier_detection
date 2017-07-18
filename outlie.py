import pandas as pd
import xlrd
import numpy as np
## The main function to give the outlier list
def outlie(data,threshold=1):
        data=data.applymap(str)
## This line combines all the column values to one single array to find the pattern combination of all the columns          
        concat = data.apply(lambda x: ''.join(x),axis=1)
## This line gets a array with the frequency of each pattern in the file
        count=concat.apply(lambda x:list(concat).count(x))
## This line g
        result=count.apply(lambda x:1 if x>threshold else -1)
        return(result)
        




