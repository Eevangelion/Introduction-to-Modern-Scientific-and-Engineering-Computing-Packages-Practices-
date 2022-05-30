import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd
import seaborn as sns
from locale import normalize
data = pd.read_csv("titanic_corrupted.csv")

regex_list = [":", "_", "-", ";", " ", "."]
for element in regex_list:
    data.columns = data.columns.str.replace(element, "")
data.columns = data.columns.str.capitalize()
for nameCol in data.columns.arr:
    filter = data[nameCol] == np.NaN
    data.loc(filter)
print(data.head(420))