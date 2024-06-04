# data_processing

import pandas as pd
import scipy
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt




# Load the dataset
df = pd.read_csv('C:\\Users\\HP\\Documents\\Repos\\june_2024\\GeeksForGeeks\\diabetes.csv')
print(df.head())



# print("Runs....")