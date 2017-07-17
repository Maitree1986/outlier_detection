import pandas as pd
import xlrd
import numpy as np

def outlie(data,threshold=1):
        data=data.applymap(str)
        concat = data.apply(lambda x: ''.join(x),axis=1)
        count=concat.apply(lambda x:list(concat).count(x))
        result=count.apply(lambda x:1 if x>threshold else -1)
        return(result)
        




