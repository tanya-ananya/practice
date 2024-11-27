import pandas as pd

data = pd.Series([1, 2, 3, 4], ['1', 'b', 'c', 'd'], dtype=int, name='sample_data')
data1 = pd.Series([1,2,3,4])
print(data)
print(data1)
