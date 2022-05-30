import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd
import seaborn as sns
from locale import normalize

data = pd.read_csv("anime.csv")
df = pd.DataFrame(data)
print(df.head(10))
df['Episodes'] = df['Episodes'].replace('?', -1).replace(-1, np.nan)
df['Voters'] = df['Voters'].str.replace(",", "")
df = df.astype({'Episodes': 'float32', 'Title': 'string', 'Production': 'string', 'Source': 'string', 'Genre': 'string', 'Airdate': 'string','Voters': 'int32', 'Rating': 'float32', 'Theme': 'string'})
print(df.dtypes)
numerical = ['episodes', 'rating', 'airdate', 'voters']
categorical = ['title', 'production', 'source', 'genre', 'theme']
print("Numerical:", numerical, "\nCategorical:", categorical)
df.columns = df.columns.map(lambda name: name.lower())
print(df.columns)
print(df.describe())
for col in categorical:
    print(col, ':', df[col].unique())
