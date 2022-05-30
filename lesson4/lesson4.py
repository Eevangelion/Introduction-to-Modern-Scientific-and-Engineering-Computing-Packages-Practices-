import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd
import seaborn as sns
from locale import normalize
np.random.seed(228)

v1 = pd.Series(np.random.normal(0, 10, 1000), name='v1')
v2 = pd.Series(2*v1 + np.random.normal(60, 15, 1000), name='v2')

plt.figure()
plt.hist(v1, alpha=0.7, bins=np.arange(-50, 150, 5), label='v1')
plt.hist(v2, alpha=0.7, bins=np.arange(-50, 150, 5), label='v2')
plt.legend()

plt.figure()
sns.set_style('dark')
plt.hist([v1, v2], histtype='barstacked', density=True)
v3 = np.concatenate((v1, v2))
sns.kdeplot(v3)
plt.figure()
# sns.distplot(v3)  = 11-15 строчки

plt.figure()
sns.jointplot(v1, v2, alpha=0.4, kind='kde')
sns.set_style('white')
plt.show()

plt.figure()
sns.set_style('white')
data = sns.load_dataset('iris')
sns.jointplot(data=data, x="bill_length_mm", y="bill_depth_mm", kind='kde', hue='sex')

sns.pairplot(data, hue='species', diag_kind='kde')

plt.subplot(121)
sns.swarmplot('species', 'petal_length', data=data)
plt.subplot(122)
sns.violinplot('species', 'petal_length', data=data)
plt.show()
