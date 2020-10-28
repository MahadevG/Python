import pandas as pd
df=pd.read_csv('myfile.csv', sep=',',header=None)
df.values
array([[ 1. ,  2. ,  3. ],
       [ 4. ,  5.5,  6. ]])
