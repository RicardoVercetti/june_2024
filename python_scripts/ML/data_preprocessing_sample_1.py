# importing libraries
import pandas as pd
import scipy
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt



# Load the dataset
df = pd.read_csv('res/diabetes.csv')
# print(df.head())
# print(df.isnull())
# print("Runs...")
# df.info()
# print(df.isnull().sum())
# print(df.describe())



# Box Plots
# fig, axs = plt.subplots(9,1,dpi=95, figsize=(7,15))
# i = 0
# for col in df.columns:
# 	axs[i].boxplot(df[col], vert=False)
# 	axs[i].set_ylabel(col)
# 	i+=1
# plt.show()


# for col in df.columns:
# 	print(col)



q1, q3 = np.percentile(df['Insulin'], [25, 75])
# print(q1, q3)
# print(df['Insulin'])
iqr = q3 - q1
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

clean_data = df[(df['Insulin'] >= lower_bound) 
                & (df['Insulin'] <= upper_bound)]

# print("lower_bound :", lower_bound)
# print("upper_bound :", upper_bound)

print()
print("=="*15)
print(clean_data)
