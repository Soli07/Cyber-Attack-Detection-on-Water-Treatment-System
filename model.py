import warnings
import pandas as pd
import numpy as np
import csv
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow
import keras
import keras.layers
from keras import Sequential
from keras.src.layers import TimeDistributed
from sklearn.model_selection import train_test_split
from keras.layers import Input, Dense, LSTM, RepeatVector
from keras.models import Model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from tensorflow.python.keras.layers import Dropout

warnings.filterwarnings("ignore", category=DeprecationWarning)

# # Load your data
df = pd.read_csv("C:/Users/DELL/Desktop/Graduation Project/dataset/SWaT_Dataset_Attack_v01.csv")
# to remove and clean any whitespaces in columns data
df.columns = df.columns.str.strip()


# Preprocess the data
df = df.drop(columns=['Timestamp'])
df['Normal/Attack'] = df['Normal/Attack'].map({'Normal': 0, 'Attack': 1})
target_label = df['Normal/Attack']
df_without_labels = df.drop(columns=['Normal/Attack'])

#df.to_csv('C:/Users/DELL/Desktop/Graduation Project/dataset/firstformatted.csv', index=False)

# for c in df.columns[:-2]:
#     df[c] = pd.to_numeric(df[c])

for col in df_without_labels.columns:
    if len(df_without_labels[col].unique()) == 1:
        df_without_labels.drop(col, inplace=True, axis=1)

# Feature engineering and scaling
cat_col = []
num_col = []

for column in df_without_labels.columns:
    unique_values = df_without_labels[column].nunique()
    if unique_values > 10:
        num_col.append(column)
    else:
        cat_col.append(column)
