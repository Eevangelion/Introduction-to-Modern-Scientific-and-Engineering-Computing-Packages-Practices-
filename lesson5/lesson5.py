import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd
import seaborn as sns
from locale import normalize
normal_sample = np.random.normal(loc=0.0, scale=1.9, size=10000)
random_sample = np.random.random(size=10000)
gamma_sample = np.random.gamma(2, size=10000)

df = pd.DataFrame({'normal': normal_sample, 'random': random_sample, 'gamma': gamma_sample })
print(df.describe())
plt.figure()
_ = plt.boxplot([df['normal'], df['random'], df['gamma']], whis=[50, 60])

plt.figure()
dff = pd.DataFrame(data=df, columns=['normal', 'random', 'gamma'])
bp = sns.boxplot(x="variable", y="value", data=pd.melt(dff), whis=[50, 60])
bp.axes.set_title("Распределения", fontsize=16)
bp.set_xlabel("Виды распределений", fontsize=14)
bp.set_ylabel("Значения", fontsize=14)
plt.show()
